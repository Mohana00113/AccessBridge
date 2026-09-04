// ============================================================
// script.js — AccessBridge
// ============================================================

let API = "http://127.0.0.1:5000";
let BLIND_API = API;

function normalizeBackendUrl(url) {
  if (!url) return API;
  let normalized = url.trim();
  if (!/^https?:\/\//i.test(normalized)) normalized = `http://${normalized}`;
  normalized = normalized.replace(/\/+$/, '');
  return normalized;
}

function setBackendUrl(url) {
  const normalized = normalizeBackendUrl(url);
  API = normalized;
  BLIND_API = normalized;
  const input = document.getElementById('settings-api-url');
  if (input) input.value = normalized;
  localStorage.setItem('sb-backend-url', normalized);
}

function loadBackendUrlFromSettings() {
  const saved = localStorage.getItem('sb-backend-url');
  const input = document.getElementById('settings-api-url');
  if (saved) {
    setBackendUrl(saved);
  } else if (input && input.value) {
    setBackendUrl(input.value);
  }
  if (input) {
    input.addEventListener('blur', () => setBackendUrl(input.value));
    input.addEventListener('change', () => setBackendUrl(input.value));
  }
}

// ── State ──
let appMode      = null;   // null | 'sign' | 'blind'
let signFeature  = null;    // null means no feature selected yet
let builtWord    = "";
let pollInterval = null;
let voiceActive  = false;
let recognition  = null;
let lastPredictionAt = 0;
let predictionWatchdogInterval = null;
let fetchAbortController = null;  // abort in-flight /predict requests
let isFetching = false;           // prevent overlapping fetches

// ── DOM refs ──
const bigLetter   = document.getElementById("big-letter");
const confFill    = document.getElementById("conf-fill");
const confText    = document.getElementById("conf-text");
const wordDisplay = document.getElementById("word-display");
const statusDot   = document.getElementById("status-dot");
const statusText  = document.getElementById("status-text");
const videoEl     = document.getElementById("cam-feed");
const placeholder = document.getElementById("cam-placeholder");

// ============================================================
// CENTRAL MODE SETTER — single source of truth
// ============================================================
function setAppMode(m) {
  if (appMode === m) return; // already in this mode — do nothing
  appMode = m;

  // ── Stop camera if switching away from sign ──
  if (m !== 'sign') {
    stopCamera();
    if (voiceActive && recognition) recognition.stop();
  }

  // ── Reset blind tool state if switching away from blind ──
  if (m !== 'blind') {
    activeTool = null;
  }

  // ── Show / hide sections ──
  const aboutSection = document.getElementById('about');
  const howSection = document.getElementById('how');
  const demoSection = document.getElementById('demo');
  const featuresSection = document.getElementById('features');
  const aslSection = document.getElementById('asl');
  const blindSection = document.getElementById('blind');

  if (aboutSection) aboutSection.style.display = (m === 'sign') ? '' : 'none';
  if (howSection) howSection.style.display = (m === 'sign') ? '' : 'none';
  if (demoSection) demoSection.style.display = (m === 'sign' && signFeature !== 'guide') ? '' : 'none';
  if (featuresSection) featuresSection.style.display = (m === 'sign') ? '' : 'none';
  if (aslSection) aslSection.style.display = (m === 'sign' && signFeature === 'guide') ? '' : 'none';
  if (blindSection) blindSection.style.display = (m === 'blind') ? '' : 'none';

  // ── Footer ──
  document.getElementById('footer').style.display = '';

  // ── Hero visibility ──
  const hero = document.getElementById('hero');
  if (hero) hero.style.display = (m === null) ? '' : 'none';

  // ── Back button visibility ──
  const backBtn = document.getElementById('mode-back');
  if (backBtn) backBtn.style.display = (m === 'sign' || m === 'blind') ? 'inline-flex' : 'none';

  // ── Nav links ──
  document.querySelectorAll('.nav-sign-only').forEach(el => {
    el.style.display = (m === 'sign') ? '' : 'none';
  });
  document.querySelectorAll('.nav-blind-only').forEach(el => {
    el.style.display = (m === 'blind') ? '' : 'none';
  });

  // ── Drawer links ──
  document.querySelectorAll('.drawer-sign-only').forEach(el => {
    el.style.display = (m === 'sign') ? '' : 'none';
  });

  // ── Mode button active state ──
  document.getElementById('mode-sign-btn').classList.toggle('active', m === 'sign');
  document.getElementById('mode-blind-btn').classList.toggle('active', m === 'blind');

  // ── Scroll to first section smoothly ──
  const targetId = (m === 'sign') ? 'features' : 'blind';
  setTimeout(() => {
    const target = document.getElementById(targetId);
    if (target) target.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }, 80);

  // ── Fresh start behaviour ──
  if (m === 'sign') {
    // reset word builder and predictions for a fresh UI
    builtWord = "";
    if (wordDisplay) wordDisplay.value = '';
    resetPrediction();
    stopCamera();
    setSignFeature('live');
    startCamera();
  }
  if (m === 'blind') {
    // reset blind UI state
    activeTool = null;
    const res = document.getElementById('blind-result'); if (res) res.style.display = 'none';
    const bat = document.getElementById('blind-active-tool'); if (bat) bat.style.display = 'none';
    const live = document.getElementById('blind-live-badge'); if (live) live.style.display = 'none';
  }
}

function openSignFeature(feature) {
  if (appMode !== 'sign') setAppMode('sign');
  setSignFeature(feature);
  if (feature !== 'guide') {
    startCamera();
  } else {
    stopCamera();
  }
}

function clearSignFeature() {
  signFeature = null;
  document.querySelectorAll(".feature-card").forEach(card => {
    card.classList.remove('active');
  });
  const demoSection = document.getElementById('demo');
  const aslSection  = document.getElementById('asl');
  if (demoSection) demoSection.style.display = 'none';
  if (aslSection)  aslSection.style.display = 'none';
}

function setSignFeature(feature) {
  signFeature = feature;
  document.querySelectorAll(".feature-card").forEach(card => {
    card.classList.toggle('active', card.dataset.feature === feature);
  });
  const demoSection = document.getElementById('demo');
  const aslSection  = document.getElementById('asl');
  if (demoSection) demoSection.style.display = (feature === 'guide') ? 'none' : '';
  if (aslSection)  aslSection.style.display = (feature === 'guide') ? '' : 'none';

  const label = document.getElementById('demo-feature-label');
  const desc  = document.getElementById('demo-feature-desc');
  if (label && desc) {
    if (feature === 'live') {
      label.textContent = 'Live Recognition';
      desc.textContent  = 'Open the camera and detect ASL letters in real time.';
    } else if (feature === 'word') {
      label.textContent = 'Live Word Formation';
      desc.textContent  = 'Add each detected letter to build your message and speak it aloud.';
    } else if (feature === 'tts') {
      label.textContent = 'Text-to-Speech';
      desc.textContent  = 'Convert your recognized text into speech instantly.';
    } else if (feature === 'snapshot') {
      label.textContent = 'Snapshot & Save';
      desc.textContent  = 'Save the current recognition result for later review.';
    } else if (feature === 'guide') {
      label.textContent = 'ASL Alphabet Guide';
      desc.textContent  = 'Learn every ASL letter with images and instructions.';
    }
  }

  setTimeout(() => {
    const targetId = feature === 'guide' ? 'asl' : 'demo';
    const target = document.getElementById(targetId);
    if (target) target.scrollIntoView({ behavior:'smooth', block:'start' });
  }, 80);
}

function saveSnapshot() {
  const text = builtWord.trim() || (bigLetter ? bigLetter.textContent : '');
  if (!text || text === '—') {
    alert('No recognition result yet to save.');
    return;
  }
  const snapshot = {
    text,
    timestamp: new Date().toLocaleString(),
  };
  const saved = JSON.parse(localStorage.getItem('aslSnapshots') || '[]');
  saved.unshift(snapshot);
  localStorage.setItem('aslSnapshots', JSON.stringify(saved.slice(0, 20)));
  alert('Snapshot saved locally.');
}

// Return to home (hide mode UIs and show hero)
function goHome() {
  // Stop ongoing processes
  stopCamera();
  stopPolling();
  if (recognition && typeof recognition.stop === 'function') try { recognition.stop(); } catch(e){}
  // Reset UI state
  builtWord = "";
  if (wordDisplay) wordDisplay.value = '';
  resetPrediction();
  activeTool = null;
  const aboutSection = document.getElementById('about');
  const howSection = document.getElementById('how');
  const demoSection = document.getElementById('demo');
  const aslSection = document.getElementById('asl');
  const blindSection = document.getElementById('blind');
  if (aboutSection) aboutSection.style.display = 'none';
  if (howSection) howSection.style.display = 'none';
  if (demoSection) demoSection.style.display = 'none';
  if (aslSection) aslSection.style.display = 'none';
  if (blindSection) blindSection.style.display = 'none';
  const featuresSection = document.getElementById('features'); if (featuresSection) featuresSection.style.display = 'none';
  const hero = document.getElementById('hero'); if (hero) hero.style.display = '';
  const backBtn = document.getElementById('mode-back'); if (backBtn) backBtn.style.display = 'none';
  appMode = null;
  // Hide footer if desired
  document.getElementById('footer').style.display = 'none';
  // Reset nav link visibility
  document.querySelectorAll('.nav-sign-only').forEach(el => el.style.display = 'none');
  document.querySelectorAll('.nav-blind-only').forEach(el => el.style.display = 'none');
  document.querySelectorAll('.drawer-sign-only').forEach(el => el.style.display = 'none');
  // Scroll to top of hero
  setTimeout(() => { window.scrollTo({ top: 0, behavior: 'smooth' }); }, 80);
}

// ============================================================
// CAMERA
// ============================================================
function startCamera() {
  if (statusText) statusText.textContent = "Connecting live recognition...";
  if (confText) confText.textContent = "Confidence: —";
  // use a timestamped src to avoid stale connections and allow easy reconnects
  videoEl.src = `${API}/video_feed?ts=${Date.now()}`;
  videoEl.style.display = "block";
  placeholder.style.display = "none";
  document.getElementById("start-btn").style.display = "none";
  document.getElementById("stop-btn").style.display  = "inline-flex";
  startPolling();

  // attach recovery handler on error — reconnect once, not in a tight loop
  try {
    let errorRetries = 0;
    videoEl.onerror = () => {
      errorRetries++;
      if (errorRetries > 3) return; // stop retrying to avoid infinite loop
      console.warn('Camera image error — attempting reconnect');
      setTimeout(() => {
        try { videoEl.src = `${API}/video_feed?ts=${Date.now()}`; } catch(e){}
      }, 1000);
    };
  } catch (e) {}

  // gentle prediction watchdog: only reload feed if no prediction for 10s (not 4s)
  try {
    if (predictionWatchdogInterval) clearInterval(predictionWatchdogInterval);
    predictionWatchdogInterval = setInterval(() => {
      try {
        if (!lastPredictionAt) return;
        if (Date.now() - lastPredictionAt > 10000) {
          console.warn('Prediction stale for 10s — reloading video feed');
          try { videoEl.src = `${API}/video_feed?ts=${Date.now()}`; } catch(e){}
          lastPredictionAt = Date.now();
        }
      } catch (e) {}
    }, 5000);
  } catch (e) {}
}

function stopCamera() {
  if (!videoEl) return;
  videoEl.src = "";
  videoEl.removeAttribute('src');
  try {
    videoEl.load();
  } catch (e) {
    // ignore if load is not supported for this element
  }
  videoEl.style.display = "none";
  if (placeholder) placeholder.style.display = "flex";
  const startBtn = document.getElementById("start-btn");
  const stopBtn  = document.getElementById("stop-btn");
  if (startBtn) startBtn.style.display = "inline-flex";
  if (stopBtn)  stopBtn.style.display  = "none";
  stopPolling();
  resetPrediction();
  // abort any in-flight prediction request
  if (fetchAbortController) { try { fetchAbortController.abort(); } catch(e){} fetchAbortController = null; }
  isFetching = false;
  fetch(`${API}/release_camera`, { method: 'POST' }).catch(() => {});

  // cleanup watchdog and event handlers
  try {
    if (predictionWatchdogInterval) { clearInterval(predictionWatchdogInterval); predictionWatchdogInterval = null; }
    if (videoEl) { videoEl.onerror = null; }
  } catch (e) {}
}

// ============================================================
// POLLING
// ============================================================
function startPolling() {
  if (pollInterval) return;
  // Poll every 500ms (smoother than 300ms, avoids request pile-up)
  pollInterval = setInterval(fetchPrediction, 500);
}

function stopPolling() {
  clearInterval(pollInterval);
  pollInterval = null;
}

async function fetchPrediction() {
  // Skip if a previous request is still in flight — prevents pile-up
  if (isFetching) return;
  isFetching = true;
  try {
    // Abort any lingering previous request
    if (fetchAbortController) { try { fetchAbortController.abort(); } catch(e){} }
    fetchAbortController = new AbortController();
    const res  = await fetch(`${API}/predict`, { signal: fetchAbortController.signal });
    const data = await res.json();
    // record time of last successful prediction so watchdog can detect stalls
    lastPredictionAt = Date.now();
    updatePrediction(data);
  } catch (e) {
    if (e.name === 'AbortError') { /* intentional abort — ignore */ }
    else {
      if (statusText) statusText.textContent = "Backend not running — start main.py";
      if (statusDot)  statusDot.className = "dot";
    }
  } finally {
    isFetching = false;
  }
}

function updatePrediction(data) {
  const hasLetter = data && data.letter && data.letter !== "";
  if (hasLetter) {
    if (bigLetter) bigLetter.textContent = data.letter;
    const pct = Math.round((data.confidence || 0) * 100);
    if (confFill) confFill.style.width = pct + "%";
    if (confText) confText.textContent = `Confidence: ${pct}%`;
    if (statusDot)  statusDot.className    = "dot on";
    if (statusText) statusText.textContent = data.hand_detected ? "Hand detected" : "Guessing gesture";
    highlightAlpha(data.letter);
  } else {
    resetPrediction();
  }
}

function resetPrediction() {
  if (bigLetter) bigLetter.textContent = "—";
  if (confFill)  confFill.style.width  = "0%";
  if (confText)  confText.textContent  = "Confidence: —";
  if (statusDot)  statusDot.className    = "dot";
  if (statusText) statusText.textContent = "No hand detected";
  document.querySelectorAll(".alpha-key").forEach(k => k.classList.remove("lit"));
}

// ============================================================
// WORD BUILDER
// ============================================================
function addLetter() {
  const letter = bigLetter ? bigLetter.textContent : "";
  if (letter && letter !== "—") {
    builtWord += letter;
    if (wordDisplay) wordDisplay.value = builtWord;
  }
}

function addSpace() {
  builtWord += " ";
  if (wordDisplay) wordDisplay.value = builtWord;
}

function clearWord() {
  builtWord = "";
  if (wordDisplay) wordDisplay.value = "";
}

async function speakWord() {
  const text = builtWord || (bigLetter ? bigLetter.textContent : "");
  if (!text || text === "—") return;
  try {
    await fetch(`${API}/speak`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text })
    });
  } catch (e) {
    if ("speechSynthesis" in window) {
      const utt = new SpeechSynthesisUtterance(text);
      utt.rate = 0.9;
      window.speechSynthesis.cancel();
      window.speechSynthesis.speak(utt);
    }
  }
}

// ============================================================
// ALPHA QUICK REFERENCE
// ============================================================
function buildAlphaGrid() {
  const grid = document.getElementById("alpha-grid");
  if (!grid) return;
  "ABCDEFGHIJKLMNOPQRSTUVWXYZ".split("").forEach(l => {
    const div = document.createElement("div");
    div.className = "alpha-key";
    div.id = "ak-" + l;
    div.textContent = l;
    grid.appendChild(div);
  });
}

function highlightAlpha(letter) {
  document.querySelectorAll(".alpha-key").forEach(k => k.classList.remove("lit"));
  const el = document.getElementById("ak-" + letter);
  if (el) el.classList.add("lit");
}

// ============================================================
// ASL ALPHABET GUIDE
// ============================================================
const aslData = [
  { l:"A", title:"Fist, thumb side",            desc:"Make a fist with thumb resting on the side of the index finger." },
  { l:"B", title:"Flat hand, thumb in",          desc:"Hold fingers straight up together, thumb tucked across palm." },
  { l:"C", title:"Curved hand",                  desc:"Curve all fingers and thumb to form a C shape." },
  { l:"D", title:"Index up, others touch thumb", desc:"Touch thumb to middle, ring, and pinky fingers. Index finger points up." },
  { l:"E", title:"Claw shape",                   desc:"Fold all fingers down so tips touch the base of the thumb in a claw-like shape." },
  { l:"F", title:"OK sign",                      desc:"Touch the tip of your index finger to your thumb. Keep other three fingers straight and spread." },
  { l:"G", title:"Pointing side",                desc:"Extend index finger and thumb forward parallel to each other, not touching." },
  { l:"H", title:"Two fingers side",             desc:"Extend index and middle fingers together horizontally. Place thumb over folded ring/pinky." },
  { l:"I", title:"Pinky up",                     desc:"Make a fist and extend only the pinky finger straight up." },
  { l:"J", title:"Pinky up, draw J",             desc:"Start with pinky up and draw a J shape in the air." },
  { l:"K", title:"Two fingers up with thumb",    desc:"Extend index and middle fingers up, place thumb between them." },
  { l:"L", title:"L shape",                      desc:"Extend thumb and index finger to form an L shape. Other fingers curled." },
  { l:"M", title:"Three fingers over thumb",     desc:"Tuck thumb under three fingers (index, middle, ring) held down." },
  { l:"N", title:"Two fingers over thumb",       desc:"Tuck thumb under index and middle fingers held down." },
  { l:"O", title:"O shape",                      desc:"Curve all fingers and thumb together to form a round O shape." },
  { l:"P", title:"K pointing down",              desc:"Like K hand shape but rotate the wrist so fingers point downward." },
  { l:"Q", title:"G pointing down",              desc:"Like G hand shape but rotate so the index finger points downward." },
  { l:"R", title:"Crossed fingers",              desc:"Cross the index finger over the middle finger, other fingers curled." },
  { l:"S", title:"Fist, thumb over fingers",     desc:"Make a fist with thumb wrapped over the fingers in front." },
  { l:"T", title:"Thumb between fingers",        desc:"Make a fist with thumb tucked between index and middle fingers." },
  { l:"U", title:"Two fingers up together",      desc:"Extend index and middle fingers straight up and together. Other fingers curled." },
  { l:"V", title:"Victory sign",                 desc:"Extend index and middle fingers up and spread apart like a V." },
  { l:"W", title:"Three fingers spread",         desc:"Extend index, middle, and ring fingers spread apart. Thumb and pinky touch." },
  { l:"X", title:"Hooked index finger",          desc:"Make a hook shape with the index finger. Other fingers curled into a fist." },
  { l:"Y", title:"Hang loose",                   desc:"Extend thumb and pinky finger outward. Other three fingers curled in." },
  { l:"Z", title:"Draw a Z",                     desc:"Extend index finger and draw a Z shape in the air." },
];

function buildASLGrid() {
  const grid = document.getElementById("asl-grid");
  if (!grid) return;
  aslData.forEach(item => {
    const card = document.createElement("div");
    card.className = "asl-card";
    card.dataset.letter = item.l;
    card.innerHTML = `
      <div class="asl-img-wrap">
        <img
          src="assets/${item.l.toLowerCase()}.svg"
          alt="ASL ${item.l}"
          onerror="if(!this._tried){this._tried=1;this.src='assets/${item.l.toLowerCase()}.png';}else{this.onerror=null;this.src='data:image/svg+xml;utf8,%3Csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20width=%27200%27%20height=%27200%27%3E%3Crect%20width=%27100%25%27%20height=%27100%25%27%20fill=%27%23f6f2ff%27/%3E%3Ctext%20x=%2750%25%27%20y=%2750%25%27%20dominant-baseline=%27middle%27%20text-anchor=%27middle%27%20fill=%27%23999%27%20font-size=%2720%27%3ENo%20image%3C/text%3E%3C/svg%3E';}"
        >
      </div>
      <div class="asl-letter">${item.l}</div>
      <div class="asl-title">${item.title}</div>
      <div class="asl-desc">${item.desc}</div>
    `;
    grid.appendChild(card);
  });
}

function filterASL(query) {
  const q = query.trim().toUpperCase();
  document.querySelectorAll(".asl-card").forEach(card => {
    card.style.display = (!q || card.dataset.letter.includes(q)) ? "block" : "none";
  });
}

// ============================================================
// VOICE MODE
// ============================================================
function toggleVoice() {
  if (!("webkitSpeechRecognition" in window || "SpeechRecognition" in window)) {
    document.getElementById("voice-output").textContent = "Not supported. Use Google Chrome.";
    return;
  }
  if (voiceActive) { recognition.stop(); return; }

  const SR = window.SpeechRecognition || window.webkitSpeechRecognition;
  recognition = new SR();
  recognition.continuous     = true;
  recognition.interimResults = true;
  recognition.lang           = "en-US";

  recognition.onresult = e => {
    let transcript = "";
    for (let i = e.resultIndex; i < e.results.length; i++) {
      transcript += e.results[i][0].transcript;
    }
    document.getElementById("voice-output").textContent = transcript;
  };
  recognition.onstart = () => {
    voiceActive = true;
    const btn = document.getElementById("voice-btn");
    if (btn) { btn.textContent = "⏹ Stop listening"; btn.classList.add("stop"); }
  };
  recognition.onend = () => {
    voiceActive = false;
    const btn = document.getElementById("voice-btn");
    if (btn) { btn.textContent = "🎙 Start listening"; btn.classList.remove("stop"); }
  };
  recognition.start();
}

// ============================================================
// BACKEND STATUS
// ============================================================
async function checkBackend() {
  try {
    const res  = await fetch(`${API}/status`, { signal: AbortSignal.timeout(2000) });
    const data = await res.json();
    const el   = document.getElementById("backend-status");
    if (el) {
      el.textContent = data.model_loaded
        ? "✅ Backend running — model loaded"
        : "⚠️ Backend running — no model (demo mode)";
      el.className = "b-pill ok";
    }
  } catch (e) {
    const el = document.getElementById("backend-status");
    if (el) {
      el.textContent = window.location.protocol === 'file:'
        ? "❌ Backend offline / file:// page detected — serve frontend over HTTP and run python main.py"
        : "❌ Backend offline — run: python main.py";
      el.className   = "b-pill err";
    }
  }
}

// ============================================================
// AUTH (client-side, stored in localStorage — demo/local use only,
// not a secure production login system)
// ============================================================
function getUsers() {
  return JSON.parse(localStorage.getItem("sb-users") || "{}");
}
function saveUsers(users) {
  localStorage.setItem("sb-users", JSON.stringify(users));
}
function getCurrentUser() {
  return localStorage.getItem("sb-current-user") || null;
}
function showAuthError(msg) {
  const el = document.getElementById("auth-error");
  if (!el) return;
  el.textContent = msg;
  el.style.display = "block";
}
function clearAuthError() {
  const el = document.getElementById("auth-error");
  if (el) { el.style.display = "none"; el.textContent = ""; }
}
function switchAuthView(view) {
  clearAuthError();
  document.getElementById("auth-login-view").style.display  = view === "login"  ? "block" : "none";
  document.getElementById("auth-signup-view").style.display = view === "signup" ? "block" : "none";
  document.getElementById("auth-modal-title").textContent   = view === "login" ? "👤 Login" : "👤 Sign up";
}

function handleSignup() {
  clearAuthError();
  const email     = document.getElementById("signup-email").value.trim().toLowerCase();
  const password  = document.getElementById("signup-password").value;
  const password2 = document.getElementById("signup-password2").value;

  if (!email || !/^\S+@\S+\.\S+$/.test(email)) return showAuthError("Enter a valid email address.");
  if (password.length < 6) return showAuthError("Password must be at least 6 characters.");
  if (password !== password2) return showAuthError("Passwords do not match.");

  const users = getUsers();
  if (users[email]) return showAuthError("An account with this email already exists.");

  users[email] = { password }; // NOTE: plaintext, client-side only — swap for a real backend for production
  saveUsers(users);
  localStorage.setItem("sb-current-user", email);
  document.getElementById("auth-modal").style.display = "none";
  renderAuthUI();
}

function handleLogin() {
  clearAuthError();
  const email    = document.getElementById("login-email").value.trim().toLowerCase();
  const password = document.getElementById("login-password").value;

  const users = getUsers();
  if (!users[email] || users[email].password !== password) {
    return showAuthError("Incorrect email or password.");
  }
  localStorage.setItem("sb-current-user", email);
  document.getElementById("auth-modal").style.display = "none";
  renderAuthUI();
}

function handleLogout() {
  localStorage.removeItem("sb-current-user");
  renderAuthUI();
}

function renderAuthUI() {
  const area = document.getElementById("nav-auth-area");
  if (!area) return;
  const user = getCurrentUser();
  if (user) {
    area.innerHTML = `
      <span class="nav-user-pill" title="${user}">${user}</span>
      <button class="nav-logout-btn" onclick="handleLogout()">Logout</button>
    `;
  } else {
    area.innerHTML = `<button class="nav-auth-btn" id="nav-auth-btn" onclick="openAuth()">Login / Sign up</button>`;
  }
}

// ============================================================
// INIT
// ============================================================
document.addEventListener("DOMContentLoaded", () => {
  loadBackendUrlFromSettings();
  buildAlphaGrid();
  buildASLGrid();
  checkBackend();
  renderAuthUI();
  setInterval(checkBackend, 15000);
});