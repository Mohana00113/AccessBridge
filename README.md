sign_language_project
│
├── backend
│   ├── data
│   │   ├── train
│   │   └── test
│   │
│   ├── model
│   │   └── sign_model.h5
│   │
│   ├── app.py
│   ├── collect_data.py
│   ├── train_model.py
│   ├── predict_camera.py
│   └── demo_system.py
│
├── frontend
│   ├── index.html
│   ├── style.css
│   ├── script.js
│   │
│   └── assets
│       ├── images
│       └── icons
│
├── requirements.txt
└── README.md
 
#Install Correct Libraries
pip install opencv-python
pip install mediapipe
pip install tensorflow
pip install numpy
pip install flask
pip install pyttsx3



# SignBridge
## Enhancing Accessibility using Sign Language Recognition with ML & DL
**B.Tech Final Year Project — 2024–25**

---

## Project Structure

```
sign_language_project/
│
├── backend/
│   ├── data/
│   │   ├── train/          ← gesture images for training (auto-created)
│   │   └── test/           ← gesture images for testing  (auto-created)
│   ├── model/
│   │   ├── sign_model.h5   ← trained model (created after training)
│   │   └── encoder.pkl     ← label encoder (created after training)
│   ├── app.py              ← Flask API server
│   ├── collect_data.py     ← Step 1: collect gesture images
│   ├── train_model.py      ← Step 2: train the CNN model
│   ├── predict_camera.py   ← quick test (no server needed)
│   └── demo_system.py      ← full demo for presentation
│
├── frontend/
│   ├── index.html          ← main website
│   ├── style.css           ← all styles
│   ├── script.js           ← connects website to backend
│   └── assets/
│       ├── images/
│       └── icons/
│
├── venv/                   ← virtual environment
├── requirements.txt        ← Python packages
├── main.py                 ← starts the Flask server
└── README.md
```

---

## Setup (First Time Only)

Open terminal in Cursor and run:
```bash
pip install -r requirements.txt
```

---

## How to Run

### Step 1 — Collect gesture data
```bash
python backend/collect_data.py
```
Show each letter A–Z to your camera when prompted.
Press SPACE to start collecting each letter.

### Step 2 — Train the model
```bash
python backend/train_model.py
```
This reads your images, extracts hand landmarks,
trains the CNN, and saves `sign_model.h5`.

### Step 3 — Start the backend server
```bash
python main.py
```
Server starts at http://localhost:5000

### Step 4 — Open the website
Open `http://127.0.0.1:5000` in your browser.

> The backend now also serves the frontend directly, so you do not need a separate live server.

---

## Quick Demo (No website needed)
```bash
python backend/demo_system.py
```
Runs the full system in a camera window.
Good for college presentation / demo day.

---

## Controls (in demo_system.py and predict_camera.py)

| Key   | Action                        |
|-------|-------------------------------|
| SPACE | Add detected letter to word   |
| ENTER | Speak the full word           |
| C     | Clear the word                |
| M     | Switch to voice mode          |
| Q     | Quit                          |

---

## Technologies

| Tool              | Purpose                    |
|-------------------|----------------------------|
| Python            | Core language              |
| OpenCV            | Camera capture             |
| MediaPipe         | Hand landmark detection    |
| TensorFlow/Keras  | CNN model training         |
| Flask             | Backend API server         |
| pyttsx3           | Text to speech             |
| SpeechRecognition | Voice to text              |
| HTML/CSS/JS       | Website frontend           |

## html (Rose gold)

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>SignBridge — Sign Language Recognition</title>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;1,400;1,600&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css">
</head>
<body>

<canvas id="particles"></canvas>

<nav>
  <div class="nav-logo">✋ SignBridge</div>
  <div class="nav-links">
    <a href="#about">About</a>
    <a href="#how">How it works</a>
    <a href="#demo">Live demo</a>
    <a href="#team">Team</a>
  </div>
</nav>

<section id="hero">
  <div class="hero-ring"></div>
  <div class="hero-ring"></div>
  <div class="hero-ring"></div>
  <div class="hero-tag"><span class="tag-dot"></span> B.Tech Project — ML &amp; DL</div>
  <h1>
    <span class="h1-w">Sign language</span><br>
    <span class="h1-g">meets intelligence</span>
  </h1>
  <p class="hero-sub">Real-time gesture recognition using computer vision and deep learning — bridging communication between deaf, mute, and blind individuals.</p>
  <div class="hero-btns">
    <a href="#demo" class="btn-primary">Try live demo</a>
    <a href="#how"  class="btn-secondary">How it works ↓</a>
  </div>
  <div class="hero-stats">
    <div class="stat-card"><span class="stat-n">26+</span><span class="stat-l">Gestures</span></div>
    <div class="stat-card"><span class="stat-n">96%</span><span class="stat-l">Accuracy</span></div>
    <div class="stat-card"><span class="stat-n">21</span><span class="stat-l">Landmarks</span></div>
    <div class="stat-card"><span class="stat-n">&lt;100ms</span><span class="stat-l">Response</span></div>
  </div>
</section>

<section id="about" class="section glass-section">
  <div class="section-inner">
    <div class="s-label">About</div>
    <h2>Who does this <em>help?</em></h2>
    <div class="cards-3">
      <div class="g-card">
        <div class="g-icon">🤟</div>
        <h3>Deaf &amp; mute users</h3>
        <p>Show a hand gesture to the camera. MediaPipe detects your landmarks, the CNN model recognizes the sign, and pyttsx3 speaks it out loud instantly.</p>
      </div>
      <div class="g-card">
        <div class="g-icon">🎙️</div>
        <h3>Blind users</h3>
        <p>Speak naturally into the microphone. SpeechRecognition converts your voice to text in real-time displayed clearly on screen for others to read.</p>
      </div>
      <div class="g-card">
        <div class="g-icon">🔁</div>
        <h3>Two-way communication</h3>
        <p>Switch between sign-to-voice and voice-to-text with one tap — enabling complete two-way conversations for everyone.</p>
      </div>
    </div>
  </div>
</section>

<section id="how" class="section">
  <div class="section-inner">
    <div class="s-label">Technology</div>
    <h2>How it <em>works</em></h2>
    <p class="s-sub">Five modules working together — from gesture to spoken word in under 100ms.</p>
    <div class="steps-row">
      <div class="step-item">
        <div class="step-num">01</div>
        <div class="step-tech">OpenCV</div>
        <h3>Camera capture</h3>
        <p>Opens webcam at 30fps and passes each frame to MediaPipe for hand detection.</p>
      </div>
      <div class="step-item">
        <div class="step-num">02</div>
        <div class="step-tech">MediaPipe</div>
        <h3>Hand detection</h3>
        <p>Maps 21 landmark points per hand as precise x, y, z coordinates.</p>
      </div>
      <div class="step-item">
        <div class="step-num">03</div>
        <div class="step-tech">TensorFlow</div>
        <h3>Recognition</h3>
        <p>CNN model identifies the gesture from 63 coordinates with a confidence score.</p>
      </div>
      <div class="step-item">
        <div class="step-num">04</div>
        <div class="step-tech">pyttsx3</div>
        <h3>Speech output</h3>
        <p>Converts predicted text to natural voice output instantly.</p>
      </div>
      <div class="step-item">
        <div class="step-num">05</div>
        <div class="step-tech">SpeechRecog</div>
        <h3>Voice to text</h3>
        <p>Mic input transcribed in real-time and shown on screen for blind users.</p>
      </div>
    </div>
  </div>
</section>

<section id="demo" class="section glass-section">
  <div class="section-inner">
    <div class="s-label">Interactive demo</div>
    <h2>Try it <em>live</em></h2>
    <p class="s-sub">
      Start the camera, show your hand — predictions in real-time.<br>
      <span id="backend-status" class="b-pill">Checking backend...</span>
    </p>
    <div class="demo-layout">
      <div>
        <div class="cam-box">
          <img id="cam-feed" style="width:100%;height:100%;object-fit:cover;display:none;border-radius:20px;" alt="feed">
          <div id="cam-placeholder" class="cam-ph">
            <div style="font-size:52px">📷</div>
            <p>Camera not started</p>
            <button class="btn-primary" id="start-btn" onclick="startCamera()">Start camera</button>
          </div>
        </div>
        <div class="cam-foot">
          <div class="s-row"><div class="dot" id="status-dot"></div><span id="status-text">No hand detected</span></div>
          <button class="stop-btn" id="stop-btn" onclick="stopCamera()" style="display:none">Stop</button>
        </div>
      </div>
      <div class="d-panel">
        <div class="d-block">
          <div class="d-label">Mode</div>
          <div class="mode-row">
            <button class="mode-btn active" id="mode-sign"  onclick="setMode('sign')">✋ Sign → Voice</button>
            <button class="mode-btn"        id="mode-voice" onclick="setMode('voice')">🎙 Voice → Text</button>
          </div>
        </div>
        <div class="d-block">
          <div class="d-label">Detected gesture</div>
          <div style="display:flex;align-items:center;gap:16px">
            <div id="big-letter" class="big-l">—</div>
            <div style="flex:1">
              <div class="c-track"><div id="conf-fill" class="c-fill"></div></div>
              <div id="conf-text" style="font-size:12px;color:var(--muted);margin-top:5px">—</div>
            </div>
          </div>
        </div>
        <div class="d-block">
          <div class="d-label">Word builder</div>
          <div id="word-display" class="word-d">—</div>
          <div class="w-btns">
            <button class="w-btn" onclick="addLetter()">Add</button>
            <button class="w-btn" onclick="clearWord()">Clear</button>
            <button class="w-btn green" onclick="speakWord()">🔊 Speak</button>
          </div>
        </div>
        <div class="d-block">
          <div class="d-label">ASL reference</div>
          <div class="a-grid" id="alpha-grid"></div>
        </div>
      </div>
    </div>
    <div id="voice-panel" style="display:none;margin-top:24px">
      <div class="d-block" style="max-width:540px">
        <div class="d-label">Voice to text — blind user mode</div>
        <div id="voice-output" style="font-size:18px;min-height:46px;color:var(--text);padding:8px 0">Speak into your microphone...</div>
        <button class="btn-primary" id="voice-btn" onclick="toggleVoice()" style="margin-top:14px">🎙 Start listening</button>
      </div>
    </div>
  </div>
</section>

<section id="team" class="section">
  <div class="section-inner">
    <div class="s-label">Our team</div>
    <h2>The <em>builders</em></h2>
    <p class="s-sub">B.Tech students making communication accessible for everyone.</p>
    <div class="team-g" id="team-grid"></div>
  </div>
</section>

<footer>
  <div class="foot-inner">
    <div class="foot-logo">✋ SignBridge</div>
    <p>Enhancing Accessibility using Sign Language Recognition with ML &amp; DL</p>
    <p class="foot-sub">B.Tech · Academic Project</p>
    <div class="foot-tech">
      <span>Python</span><span>OpenCV</span><span>MediaPipe</span><span>TensorFlow</span><span>Flask</span><span>pyttsx3</span>
    </div>
  </div>
</footer>

<script src="script.js"></script>
<script>
// ── Particles ──
const canvas = document.getElementById('particles');
const ctx = canvas.getContext('2d');
let W, H, pts = [];
function resize(){ W = canvas.width = window.innerWidth; H = canvas.height = window.innerHeight; }
resize(); window.addEventListener('resize', resize);

class Dot {
  constructor(){ this.reset(); }
  reset(){
    this.x = Math.random()*W; this.y = Math.random()*H;
    this.r = Math.random()*1.8+0.3;
    this.vx = (Math.random()-.5)*.25; this.vy = (Math.random()-.5)*.25;
    this.a = Math.random()*.35+0.08;
    this.c = Math.random()>.5 ? '255,179,71' : '255,107,157';
  }
  update(){ this.x+=this.vx; this.y+=this.vy; if(this.x<0||this.x>W||this.y<0||this.y>H) this.reset(); }
  draw(){ ctx.beginPath(); ctx.arc(this.x,this.y,this.r,0,Math.PI*2); ctx.fillStyle=`rgba(${this.c},${this.a})`; ctx.fill(); }
}
for(let i=0;i<80;i++) pts.push(new Dot());
function loop(){
  ctx.clearRect(0,0,W,H);
  for(let i=0;i<pts.length;i++){
    pts[i].update(); pts[i].draw();
    for(let j=i+1;j<pts.length;j++){
      const dx=pts[i].x-pts[j].x, dy=pts[i].y-pts[j].y;
      const d=Math.sqrt(dx*dx+dy*dy);
      if(d<110){
        ctx.beginPath(); ctx.moveTo(pts[i].x,pts[i].y); ctx.lineTo(pts[j].x,pts[j].y);
        ctx.strokeStyle=`rgba(255,143,171,${0.04*(1-d/110)})`; ctx.lineWidth=0.5; ctx.stroke();
      }
    }
  }
  requestAnimationFrame(loop);
}
loop();

// ── Team ──
const team = [
  {name:"Member 1",role:"ML Engineer",       contrib:"CNN model & training",  color:"#ffb347",bg:"rgba(255,179,71,0.1)"},
  {name:"Member 2",role:"Computer Vision",   contrib:"MediaPipe integration", color:"#ff8fab",bg:"rgba(255,143,171,0.1)"},
  {name:"Member 3",role:"Backend Developer", contrib:"Flask API & Python",    color:"#ff6b9d",bg:"rgba(255,107,157,0.1)"},
  {name:"Member 4",role:"Frontend Developer",contrib:"UI & website",          color:"#ffd0bb",bg:"rgba(255,208,187,0.1)"},
  {name:"Member 5",role:"Data Engineer",     contrib:"Dataset & collection",  color:"#ffb347",bg:"rgba(255,179,71,0.1)"},
];
const grid = document.getElementById("team-grid");
team.forEach(m => {
  const initials = m.name.split(" ").map(w=>w[0]).join("");
  grid.innerHTML += `
    <div class="t-card">
      <div class="t-avatar" style="background:${m.bg};color:${m.color}">${initials}</div>
      <h3>${m.name}</h3>
      <div class="t-role">${m.role}</div>
      <div class="t-contrib" style="color:${m.color}">${m.contrib}</div>
    </div>`;
});
</script>
</body>
</html>

 # CSS

@import url('https://fonts.googleapis.com/css2?family=Clash+Display:wght@400;500;600;700&family=Satoshi:wght@300;400;500;700&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;1,400;1,600&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');

:root {
  --bg:      #120810;
  --bg2:     #1a0d14;
  --bg3:     #200f18;
  --card:    rgba(255,255,255,0.04);
  --border:  rgba(255,180,120,0.1);
  --border2: rgba(255,180,120,0.2);
  --text:    #f5ede8;
  --muted:   #8a6a70;
  --gold:    #ffb347;
  --pink:    #ff6b9d;
  --rose:    #ff8fab;
  --cream:   #ffecd2;
}

*{margin:0;padding:0;box-sizing:border-box;}
html{scroll-behavior:smooth;}

body{
  background:var(--bg);
  color:var(--text);
  font-family:'Plus Jakarta Sans',sans-serif;
  font-size:16px;line-height:1.7;
  overflow-x:hidden;
}

/* mesh background */
body::before{
  content:'';
  position:fixed;inset:0;z-index:0;pointer-events:none;
  background:
    radial-gradient(ellipse 80% 60% at 100% 0%,   rgba(255,179,71,0.08) 0%,transparent 60%),
    radial-gradient(ellipse 60% 50% at 0%   100%, rgba(255,107,157,0.07) 0%,transparent 60%),
    radial-gradient(ellipse 40% 40% at 50%  50%,  rgba(255,143,171,0.04) 0%,transparent 70%);
}

#particles{position:fixed;top:0;left:0;width:100%;height:100%;z-index:0;pointer-events:none;}
nav,section,footer{position:relative;z-index:1;}

/* ── NAV ── */
nav{
  position:fixed;top:0;left:0;right:0;z-index:100;
  display:flex;align-items:center;justify-content:space-between;
  padding:0 64px;height:68px;
  background:rgba(18,8,16,0.85);
  backdrop-filter:blur(24px);
  border-bottom:1px solid var(--border);
}
.nav-logo{
  font-size:18px;font-weight:700;
  background:linear-gradient(135deg,#ffb347,#ff6b9d);
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;
  background-clip:text;letter-spacing:-0.3px;
}
.nav-links{display:flex;gap:36px;}
.nav-links a{
  color:var(--muted);text-decoration:none;
  font-size:14px;font-weight:400;transition:color .2s;
}
.nav-links a:hover{color:var(--rose);}

/* ── HERO ── */
#hero{
  min-height:100vh;
  display:flex;flex-direction:column;
  align-items:center;justify-content:center;
  padding:100px 64px 80px;
  text-align:center;
  position:relative;
}

/* decorative rings */
.hero-ring{
  position:absolute;border-radius:50%;
  border:1px solid rgba(255,179,71,0.06);
  pointer-events:none;
  animation:ringPulse 4s ease-in-out infinite;
}
.hero-ring:nth-child(1){width:400px;height:400px;top:50%;left:50%;transform:translate(-50%,-50%);}
.hero-ring:nth-child(2){width:600px;height:600px;top:50%;left:50%;transform:translate(-50%,-50%);animation-delay:1s;border-color:rgba(255,107,157,0.05);}
.hero-ring:nth-child(3){width:800px;height:800px;top:50%;left:50%;transform:translate(-50%,-50%);animation-delay:2s;border-color:rgba(255,143,171,0.04);}
@keyframes ringPulse{0%,100%{opacity:.5}50%{opacity:.15}}

.hero-tag{
  display:inline-flex;align-items:center;gap:8px;
  font-size:11px;font-weight:600;letter-spacing:1.5px;
  text-transform:uppercase;
  background:linear-gradient(135deg,rgba(255,179,71,0.1),rgba(255,107,157,0.1));
  border:1px solid rgba(255,179,71,0.25);
  color:var(--gold);padding:7px 20px;border-radius:100px;
  margin-bottom:36px;
  animation:fadeUp .6s ease both;
}
.tag-dot{width:5px;height:5px;border-radius:50%;background:var(--gold);animation:tagPulse 2s infinite;}
@keyframes tagPulse{0%,100%{opacity:1;transform:scale(1)}50%{opacity:.4;transform:scale(.8)}}

h1{
  font-family:'Cormorant Garamond',serif;
  font-size:clamp(52px,7vw,96px);
  font-weight:600;line-height:1.0;
  letter-spacing:-2px;margin-bottom:28px;
  animation:fadeUp .6s .1s ease both;
}
.h1-w{color:var(--text);}
.h1-g{
  font-style:italic;
  background:linear-gradient(135deg,#ffb347 0%,#ff8fab 50%,#ff6b9d 100%);
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;
  background-clip:text;
}

.hero-sub{
  max-width:540px;color:var(--muted);font-size:17px;
  font-weight:300;margin:0 auto 48px;line-height:1.8;
  animation:fadeUp .6s .2s ease both;
}

.hero-btns{
  display:flex;gap:14px;justify-content:center;
  margin-bottom:64px;
  animation:fadeUp .6s .3s ease both;
}
.btn-primary{
  background:linear-gradient(135deg,#ffb347,#ff6b9d);
  color:#120810;padding:14px 36px;border-radius:100px;
  font-size:14px;font-weight:700;letter-spacing:0.3px;
  text-decoration:none;border:none;cursor:pointer;
  font-family:'Plus Jakarta Sans',sans-serif;
  transition:transform .2s,box-shadow .2s;display:inline-block;
}
.btn-primary:hover{
  transform:translateY(-2px);
  box-shadow:0 12px 40px rgba(255,107,157,0.4);
}
.btn-secondary{
  background:rgba(255,255,255,0.04);color:var(--rose);
  padding:14px 36px;border-radius:100px;
  font-size:14px;font-weight:500;
  text-decoration:none;
  border:1px solid rgba(255,143,171,0.2);
  cursor:pointer;font-family:'Plus Jakarta Sans',sans-serif;
  transition:.2s;display:inline-block;
}
.btn-secondary:hover{background:rgba(255,143,171,0.06);border-color:rgba(255,143,171,0.35);}

.hero-stats{
  display:flex;gap:0;
  border:1px solid var(--border);
  border-radius:20px;overflow:hidden;
  animation:fadeUp .6s .4s ease both;
  backdrop-filter:blur(10px);
}
.stat-card{
  padding:24px 40px;text-align:center;
  border-right:1px solid var(--border);
  transition:background .2s;
  background:rgba(255,255,255,0.02);
}
.stat-card:last-child{border-right:none;}
.stat-card:hover{background:rgba(255,179,71,0.04);}
.stat-n{
  font-family:'Cormorant Garamond',serif;
  font-size:36px;font-weight:600;
  background:linear-gradient(135deg,#ffb347,#ff6b9d);
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;
  background-clip:text;display:block;line-height:1;
}
.stat-l{font-size:11px;color:var(--muted);margin-top:6px;display:block;letter-spacing:1px;text-transform:uppercase;}

@keyframes fadeUp{from{opacity:0;transform:translateY(24px)}to{opacity:1;transform:translateY(0)}}

/* ── SECTIONS ── */
.section{padding:100px 64px;}
.section-inner{max-width:1160px;margin:0 auto;}
.glass-section{
  background:rgba(255,179,71,0.02);
  border-top:1px solid var(--border);
  border-bottom:1px solid var(--border);
}

.s-label{
  font-size:11px;font-weight:600;letter-spacing:2.5px;
  text-transform:uppercase;color:var(--gold);margin-bottom:14px;
}
h2{
  font-family:'Cormorant Garamond',serif;
  font-size:clamp(32px,4vw,56px);
  font-weight:600;letter-spacing:-1px;line-height:1.05;margin-bottom:16px;
  color:var(--text);
}
h2 em{font-style:italic;color:var(--gold);}
.s-sub{color:var(--muted);font-size:16px;font-weight:300;max-width:480px;margin-bottom:52px;line-height:1.8;}

/* ── ABOUT ── */
.cards-3{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin-top:48px;}
.g-card{
  background:rgba(255,255,255,0.03);
  border:1px solid var(--border);
  border-radius:20px;padding:36px 28px;
  backdrop-filter:blur(10px);
  transition:border-color .3s,transform .2s;
  position:relative;overflow:hidden;
}
.g-card::before{
  content:'';position:absolute;
  top:0;left:0;right:0;height:1px;
  background:linear-gradient(90deg,transparent,var(--gold),transparent);
  opacity:0;transition:opacity .3s;
}
.g-card:hover{border-color:rgba(255,179,71,0.25);transform:translateY(-4px);}
.g-card:hover::before{opacity:1;}
.g-icon{font-size:32px;margin-bottom:18px;}
.g-card h3{font-size:17px;font-weight:600;margin-bottom:10px;color:var(--text);}
.g-card p{color:var(--muted);font-size:14px;line-height:1.75;}

/* ── HOW IT WORKS ── */
.steps-row{
  display:grid;grid-template-columns:repeat(5,1fr);
  gap:0;margin-top:48px;
  border:1px solid var(--border);border-radius:20px;overflow:hidden;
}
.step-item{
  padding:32px 24px;
  border-right:1px solid var(--border);
  background:rgba(255,255,255,0.02);
  transition:background .2s;
}
.step-item:last-child{border-right:none;}
.step-item:hover{background:rgba(255,179,71,0.04);}
.step-num{
  font-size:11px;font-weight:700;letter-spacing:2px;
  background:linear-gradient(135deg,#ffb347,#ff6b9d);
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;
  background-clip:text;margin-bottom:14px;
}
.step-tech{
  display:inline-block;font-size:10px;font-weight:600;
  background:rgba(255,143,171,0.08);color:var(--rose);
  border:1px solid rgba(255,143,171,0.2);
  padding:2px 10px;border-radius:6px;margin-bottom:12px;
}
.step-item h3{font-size:14px;font-weight:600;margin-bottom:8px;color:var(--text);}
.step-item p{color:var(--muted);font-size:12px;line-height:1.7;}

/* ── DEMO ── */
.demo-layout{display:grid;grid-template-columns:1fr 340px;gap:24px;align-items:start;}
.cam-box{
  background:var(--bg3);border:1px solid var(--border);
  border-radius:20px;overflow:hidden;aspect-ratio:4/3;position:relative;
}
.cam-ph{
  position:absolute;inset:0;
  display:flex;flex-direction:column;
  align-items:center;justify-content:center;gap:14px;
}
.cam-ph p{color:var(--muted);font-size:14px;}
.cam-foot{display:flex;align-items:center;justify-content:space-between;margin-top:10px;}
.s-row{display:flex;align-items:center;gap:7px;font-size:13px;color:var(--muted);}
.dot{width:7px;height:7px;border-radius:50%;background:#333;}
.dot.on{background:var(--gold);box-shadow:0 0 8px rgba(255,179,71,0.5);animation:glow 1.5s infinite;}
@keyframes glow{0%,100%{opacity:1}50%{opacity:.5}}
.stop-btn{
  font-size:12px;font-weight:600;color:var(--pink);
  background:rgba(255,107,157,.08);border:1px solid rgba(255,107,157,.2);
  padding:7px 16px;border-radius:100px;cursor:pointer;
  font-family:'Plus Jakarta Sans',sans-serif;transition:.2s;
}
.stop-btn:hover{background:rgba(255,107,157,.12);}

.d-panel{display:flex;flex-direction:column;gap:12px;}
.d-block{
  background:rgba(255,255,255,0.03);border:1px solid var(--border);
  border-radius:16px;padding:20px 22px;backdrop-filter:blur(10px);
}
.d-label{
  font-size:10px;font-weight:600;text-transform:uppercase;
  letter-spacing:2px;color:var(--muted);margin-bottom:12px;
}
.mode-row{display:flex;gap:8px;}
.mode-btn{
  flex:1;padding:10px 8px;border-radius:100px;
  border:1px solid var(--border);background:transparent;
  color:var(--muted);font-size:12px;font-weight:500;
  cursor:pointer;font-family:'Plus Jakarta Sans',sans-serif;transition:.2s;
}
.mode-btn:hover{border-color:var(--border2);color:var(--rose);}
.mode-btn.active{
  background:linear-gradient(135deg,rgba(255,179,71,0.12),rgba(255,107,157,0.12));
  border-color:rgba(255,179,71,0.3);color:var(--gold);
}
.big-l{
  font-family:'Cormorant Garamond',serif;
  font-size:76px;font-weight:600;line-height:1;
  background:linear-gradient(135deg,#ffb347,#ff6b9d);
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;
  background-clip:text;
}
.c-track{height:3px;background:rgba(255,255,255,.05);border-radius:2px;overflow:hidden;}
.c-fill{height:100%;background:linear-gradient(90deg,#ffb347,#ff6b9d);border-radius:2px;width:0%;transition:width .3s;}
.word-d{
  font-family:'Cormorant Garamond',serif;
  font-size:26px;font-weight:600;color:var(--text);
  min-height:36px;word-break:break-all;margin-bottom:14px;
}
.w-btns{display:flex;gap:8px;}
.w-btn{
  flex:1;padding:10px 8px;border:1px solid var(--border);
  border-radius:100px;background:transparent;color:var(--muted);
  font-size:12px;font-weight:500;cursor:pointer;
  font-family:'Plus Jakarta Sans',sans-serif;transition:.2s;
}
.w-btn:hover{border-color:var(--border2);color:var(--text);}
.w-btn.green{
  background:linear-gradient(135deg,rgba(255,179,71,0.1),rgba(255,107,157,0.1));
  border-color:rgba(255,179,71,0.3);color:var(--gold);
}
.w-btn.green:hover{background:linear-gradient(135deg,rgba(255,179,71,0.15),rgba(255,107,157,0.15));}
.a-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(34px,1fr));gap:4px;}
.alpha-key{
  background:rgba(255,255,255,.03);border:1px solid var(--border);
  border-radius:7px;padding:6px 4px;text-align:center;
  font-size:12px;font-weight:600;color:var(--muted);transition:.15s;
}
.alpha-key.lit{
  background:linear-gradient(135deg,rgba(255,179,71,.15),rgba(255,107,157,.15));
  border-color:rgba(255,179,71,.4);
  background:rgba(255,179,71,.12);
  color:var(--gold);transform:scale(1.1);
}
.b-pill{
  display:inline-block;font-size:11px;font-weight:500;
  padding:3px 12px;border-radius:100px;
  background:rgba(255,255,255,.03);border:1px solid var(--border);
  color:var(--muted);margin-top:8px;
}
.b-pill.ok{background:rgba(255,179,71,.08);border-color:rgba(255,179,71,.2);color:var(--gold);}
.b-pill.err{background:rgba(255,107,157,.06);border-color:rgba(255,107,157,.15);color:var(--pink);}

/* ── TEAM ── */
.team-g{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:18px;margin-top:48px;}
.t-card{
  background:rgba(255,255,255,.03);border:1px solid var(--border);
  border-radius:18px;padding:28px 22px;text-align:center;
  backdrop-filter:blur(10px);transition:border-color .2s,transform .2s;
}
.t-card:hover{border-color:rgba(255,179,71,.25);transform:translateY(-4px);}
.t-avatar{
  width:60px;height:60px;border-radius:16px;
  display:flex;align-items:center;justify-content:center;
  font-family:'Cormorant Garamond',serif;
  font-size:22px;font-weight:600;margin:0 auto 14px;
}
.t-card h3{font-size:15px;font-weight:600;margin-bottom:4px;color:var(--text);}
.t-role{font-size:13px;color:var(--muted);}
.t-contrib{font-size:12px;margin-top:8px;font-weight:600;}

/* ── FOOTER ── */
footer{
  border-top:1px solid var(--border);
  padding:60px 64px;text-align:center;
  background:rgba(0,0,0,0.3);backdrop-filter:blur(10px);
}
.foot-inner{max-width:600px;margin:0 auto;}
.foot-logo{
  font-size:22px;font-weight:600;margin-bottom:14px;
  font-family:'Cormorant Garamond',serif;
  background:linear-gradient(135deg,#ffb347,#ff6b9d);
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;
  background-clip:text;
}
footer p{font-size:14px;color:var(--muted);margin-bottom:6px;}
.foot-sub{font-size:12px;color:rgba(255,255,255,.2)!important;}
.foot-tech{display:flex;flex-wrap:wrap;gap:8px;justify-content:center;margin-top:24px;}
.foot-tech span{
  font-size:11px;font-weight:500;
  background:rgba(255,179,71,.05);
  border:1px solid rgba(255,179,71,.1);
  color:rgba(255,179,71,.5);padding:4px 12px;border-radius:100px;
}

@media(max-width:900px){
  nav{padding:0 24px;}
  .nav-links{display:none;}
  .section{padding:60px 24px;}
  #hero{padding:100px 24px 60px;}
  .cards-3{grid-template-columns:1fr;}
  .steps-row{grid-template-columns:1fr;}
  .step-item{border-right:none;border-bottom:1px solid var(--border);}
  .demo-layout{grid-template-columns:1fr;}
  footer{padding:48px 24px;}
  .hero-stats{flex-wrap:wrap;}
}


# html(Black background)
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>SignBridge — Sign Language Recognition</title>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css">
</head>
<body>

<nav>
  <div class="nav-logo">✋ SignBridge</div>
  <div class="nav-links">
    <a href="#about">About</a>
    <a href="#how">How it works</a>
    <a href="#demo">Live demo</a>
    <a href="#team">Team</a>
  </div>
</nav>

<!-- HERO -->
<section id="hero">
  <div class="hero-dots"></div>
  <div class="hero-inner">
    <div class="hero-left">
      <div class="hero-tag"><span class="hero-tag-dot"></span> B.Tech Project</div>
      <h1>Breaking the<br><em>communication</em><br><span class="tl">barrier</span></h1>
      <p class="hero-desc">Real-time sign language recognition using ML &amp; DL — bridging the gap between deaf, mute, and blind individuals.</p>
      <div class="hero-btns">
        <a href="#demo" class="btn-fill">Try live demo</a>
        <a href="#how"  class="btn-ghost">How it works</a>
      </div>
    </div>
    <div class="hero-right">
      <div class="hero-card">
        <div class="hero-card-icon">🤟</div>
        <div class="hero-card-stats">
          <div class="hstat"><span class="hstat-num">26+</span><span class="hstat-label">Gestures</span></div>
          <div class="hstat-div"></div>
          <div class="hstat"><span class="hstat-num">96%</span><span class="hstat-label">Accuracy</span></div>
          <div class="hstat-div"></div>
          <div class="hstat"><span class="hstat-num">21</span><span class="hstat-label">Landmarks</span></div>
        </div>
        <div class="hero-card-tags">
          <span>OpenCV</span><span>MediaPipe</span><span>TensorFlow</span><span>Flask</span>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ABOUT -->
<section id="about">
  <div class="section-inner">
    <div class="label">About</div>
    <h2>Who does this help?</h2>
    <div class="about-grid">
      <div class="about-card">
        <div class="about-num">01</div>
        <div class="about-icon">🤟</div>
        <h3>Deaf &amp; mute users</h3>
        <p>Show a hand gesture to the camera. The system reads your hand, identifies the sign, and speaks it out loud instantly.</p>
      </div>
      <div class="about-card">
        <div class="about-num">02</div>
        <div class="about-icon">🎙️</div>
        <h3>Blind users</h3>
        <p>Speak naturally into the microphone. The system converts your voice to text on screen so others can read it easily.</p>
      </div>
      <div class="about-card">
        <div class="about-num">03</div>
        <div class="about-icon">🔁</div>
        <h3>Two-way communication</h3>
        <p>Both modes work together — switch between sign-to-voice and voice-to-text with a single tap for full conversations.</p>
      </div>
    </div>
  </div>
</section>

<!-- HOW IT WORKS -->
<section id="how" class="bg-soft">
  <div class="section-inner">
    <div class="label">Technology</div>
    <h2>How it works</h2>
    <p class="section-sub">Five modules working together in under 100ms.</p>
    <div class="how-list">
      <div class="how-item">
        <div class="how-dot">01</div>
        <div class="how-content">
          <h3>Camera capture <span class="tech">OpenCV</span></h3>
          <p>Opens your webcam and reads every frame at 30fps — passing each one to MediaPipe for hand analysis.</p>
        </div>
      </div>
      <div class="how-item">
        <div class="how-dot">02</div>
        <div class="how-content">
          <h3>Hand detection <span class="tech">MediaPipe</span></h3>
          <p>Detects your hand and maps 21 precise landmark points — one per joint and fingertip — as x, y, z coordinates.</p>
        </div>
      </div>
      <div class="how-item">
        <div class="how-dot">03</div>
        <div class="how-content">
          <h3>Gesture recognition <span class="tech">TensorFlow · Keras</span></h3>
          <p>The 63 coordinates are fed into a trained CNN model which identifies the gesture and returns a confidence score.</p>
        </div>
      </div>
      <div class="how-item">
        <div class="how-dot">04</div>
        <div class="how-content">
          <h3>Text to speech <span class="tech">pyttsx3</span></h3>
          <p>The predicted letter or word is converted to natural audio output using the pyttsx3 speech engine.</p>
        </div>
      </div>
      <div class="how-item last">
        <div class="how-dot">05</div>
        <div class="how-content">
          <h3>Voice to text <span class="tech">SpeechRecognition</span></h3>
          <p>For blind users, mic input is transcribed in real-time and displayed clearly on screen for others to read.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- LIVE DEMO -->
<section id="demo">
  <div class="section-inner">
    <div class="label">Interactive</div>
    <h2>Try it live</h2>
    <p class="section-sub">Start the camera and show your hand — the system predicts your gesture in real-time.<br>
    <span id="backend-status" class="status-pill">Checking backend...</span></p>

    <div class="demo-wrap">
      <div class="demo-cam-wrap">
        <div class="cam-box">
          <img id="cam-feed" alt="Camera feed" style="width:100%;height:100%;object-fit:cover;display:none;border-radius:16px;">
          <div id="cam-placeholder" class="cam-ph">
            <div style="font-size:48px">📷</div>
            <p>Camera not started</p>
            <button class="btn-fill" id="start-btn" onclick="startCamera()">Start camera</button>
          </div>
        </div>
        <div class="cam-footer">
          <div class="status-row">
            <div class="dot" id="status-dot"></div>
            <span id="status-text">No hand detected</span>
          </div>
          <button class="btn-stop" id="stop-btn" onclick="stopCamera()" style="display:none">Stop</button>
        </div>
      </div>

      <div class="demo-panel">
        <div class="panel-block">
          <div class="block-label">Mode</div>
          <div class="mode-row">
            <button class="mode-btn active" id="mode-sign"  onclick="setMode('sign')">✋ Sign → Voice</button>
            <button class="mode-btn"        id="mode-voice" onclick="setMode('voice')">🎙 Voice → Text</button>
          </div>
        </div>

        <div class="panel-block">
          <div class="block-label">Detected gesture</div>
          <div class="letter-display">
            <div id="big-letter">—</div>
            <div class="conf-wrap">
              <div class="conf-track"><div id="conf-fill" class="conf-bar"></div></div>
              <span id="conf-text">—</span>
            </div>
          </div>
        </div>

        <div class="panel-block">
          <div class="block-label">Word builder</div>
          <div id="word-display" class="word-out">—</div>
          <div class="word-btns">
            <button class="wb-btn" onclick="addLetter()">Add</button>
            <button class="wb-btn" onclick="clearWord()">Clear</button>
            <button class="wb-btn speak" onclick="speakWord()">🔊 Speak</button>
          </div>
        </div>

        <div class="panel-block">
          <div class="block-label">ASL reference</div>
          <div class="alpha-grid" id="alpha-grid"></div>
        </div>
      </div>
    </div>

    <div id="voice-panel" style="display:none;margin-top:32px">
      <div class="panel-block" style="max-width:560px">
        <div class="block-label">Voice to text — blind user mode</div>
        <div id="voice-output" class="voice-out">Press the button and speak...</div>
        <button class="btn-fill" id="voice-btn" onclick="toggleVoice()" style="margin-top:16px">🎙 Start listening</button>
      </div>
    </div>
  </div>
</section>

<!-- TEAM -->
<section id="team" class="bg-soft">
  <div class="section-inner">
    <div class="label">Our team</div>
    <h2>The builders</h2>
    <p class="section-sub">B.Tech students building technology that makes communication truly accessible.</p>
    <div class="team-grid" id="team-grid"></div>
  </div>
</section>

<!-- FOOTER -->
<footer>
  <div class="footer-inner">
    <div class="footer-logo">✋ SignBridge</div>
    <p>Enhancing Accessibility using Sign Language Recognition with ML &amp; DL</p>
    <p class="footer-sub">B.Tech · Academic Project</p>
    <div class="footer-tech">
      <span>Python</span><span>OpenCV</span><span>MediaPipe</span><span>TensorFlow</span><span>Flask</span><span>pyttsx3</span>
    </div>
  </div>
</footer>

<script src="script.js"></script>
<script>
const team = [
  { name: "Member 1", role: "ML Engineer",        contrib: "CNN model & training",   color:"#0ea874", bg:"#e6f9f2" },
  { name: "Member 2", role: "Computer Vision",    contrib: "MediaPipe integration",  color:"#2563eb", bg:"#eff6ff" },
  { name: "Member 3", role: "Backend Developer",  contrib: "Flask API & Python",     color:"#dc2626", bg:"#fef2f2" },
  { name: "Member 4", role: "Frontend Developer", contrib: "UI & website",           color:"#d97706", bg:"#fffbeb" },
  { name: "Member 5", role: "Data Engineer",      contrib: "Dataset & collection",   color:"#7c3aed", bg:"#f5f3ff" },
];
const grid = document.getElementById("team-grid");
team.forEach(m => {
  const initials = m.name.split(" ").map(w=>w[0]).join("");
  grid.innerHTML += `
    <div class="team-card">
      <div class="avatar" style="background:${m.bg};color:${m.color}">${initials}</div>
      <h3>${m.name}</h3>
      <div class="team-role">${m.role}</div>
      <div class="team-contrib" style="color:${m.color}">${m.contrib}</div>
    </div>`;
});
</script>
</body>
</html>

#Css

@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600&family=DM+Sans:wght@300;400;500&display=swap');

:root {
  --bg:      #0d0d0f;
  --bg2:     #111114;
  --bg3:     #16161a;
  --card:    #1a1a1f;
  --border:  rgba(255,255,255,0.08);
  --border2: rgba(255,255,255,0.12);
  --text:    #f0ede8;
  --muted:   #8a8780;
  --gold:    #c9a96e;
  --gold2:   #e8c99a;
  --teal:    #4ecdc4;
  --teal2:   #38b2ac;
  --white:   #ffffff;
}

* { margin:0; padding:0; box-sizing:border-box; }
html { scroll-behavior:smooth; }

body {
  background: var(--bg);
  color: var(--text);
  font-family: 'DM Sans', sans-serif;
  font-size: 16px;
  line-height: 1.7;
  overflow-x: hidden;
}

/* ===== NAV ===== */
nav {
  position:fixed; top:0; left:0; right:0; z-index:100;
  display:flex; align-items:center; justify-content:space-between;
  padding:22px 64px;
  background: rgba(13,13,15,0.85);
  backdrop-filter: blur(20px);
  border-bottom: 1px solid var(--border);
}
.nav-logo {
  font-family:'DM Sans',sans-serif;
  font-weight:500; font-size:18px; color:var(--gold);
  letter-spacing:0.5px;
}
.nav-links { display:flex; gap:36px; }
.nav-links a {
  color:var(--muted); text-decoration:none;
  font-size:14px; font-weight:400; transition:color .2s;
  letter-spacing:0.3px;
}
.nav-links a:hover { color:var(--text); }

/* ===== HERO ===== */
#hero {
  min-height: 100vh;
  display: flex; align-items: center;
  padding: 100px 64px 80px;
  position: relative; overflow: hidden;
}

/* Animated background orbs */
#hero::before {
  content:'';
  position:absolute; top:-200px; left:-200px;
  width:700px; height:700px; border-radius:50%;
  background: radial-gradient(circle, rgba(201,169,110,0.07) 0%, transparent 70%);
  animation: orb1 8s ease-in-out infinite;
  pointer-events:none;
}
#hero::after {
  content:'';
  position:absolute; bottom:-200px; right:-100px;
  width:600px; height:600px; border-radius:50%;
  background: radial-gradient(circle, rgba(78,205,196,0.06) 0%, transparent 70%);
  animation: orb2 10s ease-in-out infinite;
  pointer-events:none;
}
@keyframes orb1 { 0%,100%{transform:translate(0,0)} 50%{transform:translate(60px,40px)} }
@keyframes orb2 { 0%,100%{transform:translate(0,0)} 50%{transform:translate(-40px,-60px)} }

/* Dot grid overlay */
.hero-dots {
  position:absolute; inset:0;
  background-image: radial-gradient(rgba(255,255,255,0.06) 1px, transparent 1px);
  background-size: 40px 40px;
  mask-image: radial-gradient(ellipse 70% 70% at 50% 50%, black 30%, transparent 100%);
  pointer-events:none;
}

.hero-inner {
  max-width:1200px; margin:0 auto; width:100%;
  display:grid; grid-template-columns:1fr 400px;
  gap:80px; align-items:center; position:relative; z-index:1;
}
.hero-tag {
  display:inline-flex; align-items:center; gap:8px;
  font-size:11px; font-weight:500; letter-spacing:2px;
  text-transform:uppercase; color:var(--gold);
  border:1px solid rgba(201,169,110,0.25);
  background: rgba(201,169,110,0.06);
  padding:6px 16px; border-radius:100px;
  margin-bottom:32px;
  animation:fadeUp .6s ease both;
}
.hero-tag-dot { width:5px;height:5px;border-radius:50%;background:var(--gold);animation:pulse 2s infinite; }
@keyframes pulse { 0%,100%{opacity:1}50%{opacity:.3} }

h1 {
  font-family:'Cormorant Garamond',serif;
  font-size: clamp(48px,5.5vw,80px);
  font-weight:700; line-height:1.0;
  letter-spacing:-1px; margin-bottom:28px;
  animation:fadeUp .6s .1s ease both;
}
h1 em { font-style:italic; color:var(--gold); }
h1 .tl { color:var(--teal); font-style:normal; }

.hero-desc {
  color:var(--muted); font-size:17px; font-weight:300;
  max-width:460px; margin-bottom:44px; line-height:1.8;
  animation:fadeUp .6s .2s ease both;
}
.hero-btns { display:flex; gap:12px; animation:fadeUp .6s .3s ease both; }

/* ===== BUTTONS ===== */
.btn-fill {
  background:var(--gold); color:#0d0d0f;
  padding:13px 28px; border-radius:8px;
  font-size:14px; font-weight:500;
  text-decoration:none; border:none; cursor:pointer;
  font-family:'DM Sans',sans-serif;
  transition:background .2s, transform .2s;
  display:inline-block; letter-spacing:0.3px;
}
.btn-fill:hover { background:var(--gold2); transform:translateY(-2px); }
.btn-ghost {
  background:transparent; color:var(--text);
  padding:13px 28px; border-radius:8px;
  font-size:14px; font-weight:400;
  text-decoration:none; border:1px solid var(--border2);
  cursor:pointer; font-family:'DM Sans',sans-serif;
  transition:.2s; display:inline-block;
}
.btn-ghost:hover { border-color:rgba(255,255,255,.25); background:rgba(255,255,255,.04); }

/* ===== HERO CARD ===== */
.hero-card {
  background: linear-gradient(145deg, #1e1e24, #16161a);
  border:1px solid var(--border2);
  border-radius:24px; padding:40px 36px;
  position:relative; overflow:hidden;
  animation:fadeUp .6s .2s ease both;
}
.hero-card::before {
  content:'';
  position:absolute; top:-40px; right:-40px;
  width:200px; height:200px; border-radius:50%;
  background: radial-gradient(circle, rgba(201,169,110,0.08) 0%, transparent 70%);
  pointer-events:none;
}
.hero-card-icon { font-size:44px; margin-bottom:28px; }
.hero-card-stats {
  display:flex; align-items:center;
  border:1px solid var(--border); border-radius:12px;
  overflow:hidden; margin-bottom:28px;
}
.hstat { flex:1; padding:18px 0; text-align:center; }
.hstat-num {
  display:block;
  font-family:'Cormorant Garamond',serif;
  font-size:30px; font-weight:700; color:var(--gold); line-height:1;
}
.hstat-label {
  display:block; font-size:11px; color:var(--muted);
  margin-top:5px; text-transform:uppercase; letter-spacing:1px;
}
.hstat-div { width:1px; background:var(--border); align-self:stretch; }
.hero-card-tags { display:flex; flex-wrap:wrap; gap:8px; }
.hero-card-tags span {
  font-size:11px; font-weight:500;
  background:rgba(255,255,255,0.05);
  border:1px solid var(--border);
  color:var(--muted); padding:4px 12px; border-radius:100px;
}

@keyframes fadeUp {
  from{opacity:0;transform:translateY(24px)}
  to{opacity:1;transform:translateY(0)}
}

/* ===== SECTIONS ===== */
section { padding:100px 64px; }
.section-inner { max-width:1200px; margin:0 auto; }
.bg-soft { background:var(--bg2); }

.label {
  font-size:11px; font-weight:500; color:var(--gold);
  text-transform:uppercase; letter-spacing:2.5px; margin-bottom:14px;
}
h2 {
  font-family:'Cormorant Garamond',serif;
  font-size:clamp(32px,3.5vw,52px);
  font-weight:700; line-height:1.05;
  letter-spacing:-0.5px; margin-bottom:16px;
}
.section-sub {
  color:var(--muted); font-size:16px; font-weight:300;
  max-width:500px; margin-bottom:56px; line-height:1.8;
}

/* ===== ABOUT ===== */
.about-grid {
  display:grid; grid-template-columns:repeat(3,1fr);
  gap:20px; margin-top:48px;
}
.about-card {
  background:var(--card); border:1px solid var(--border);
  border-radius:18px; padding:36px 28px;
  position:relative; overflow:hidden;
  transition:border-color .2s, transform .2s;
}
.about-card::before {
  content:'';
  position:absolute; top:0; left:0; right:0; height:2px;
  background: linear-gradient(90deg, var(--gold), transparent);
  opacity:0; transition:opacity .3s;
}
.about-card:hover { border-color:rgba(201,169,110,0.3); transform:translateY(-4px); }
.about-card:hover::before { opacity:1; }
.about-num {
  font-family:'Cormorant Garamond',serif;
  font-size:60px; font-weight:700;
  color:rgba(255,255,255,0.04);
  position:absolute; top:12px; right:18px; line-height:1;
}
.about-icon { font-size:30px; margin-bottom:18px; }
.about-card h3 {
  font-family:'DM Sans',sans-serif;
  font-size:16px; font-weight:500; margin-bottom:10px; color:var(--text);
}
.about-card p { color:var(--muted); font-size:14px; line-height:1.75; }

/* ===== HOW IT WORKS ===== */
.how-list {
  margin-top:48px; display:flex; flex-direction:column;
  border:1px solid var(--border); border-radius:18px; overflow:hidden;
}
.how-item {
  display:flex; align-items:flex-start; gap:28px;
  padding:30px 36px; border-bottom:1px solid var(--border);
  transition:background .2s; cursor:default;
}
.how-item:last-child { border-bottom:none; }
.how-item:hover { background:rgba(255,255,255,0.02); }
.how-dot {
  width:42px; height:42px; border-radius:10px;
  background: linear-gradient(135deg, rgba(201,169,110,0.15), rgba(201,169,110,0.05));
  border:1px solid rgba(201,169,110,0.2);
  color:var(--gold); font-size:12px; font-weight:500;
  display:flex; align-items:center; justify-content:center;
  flex-shrink:0; letter-spacing:0.5px;
}
.how-content h3 {
  font-size:15px; font-weight:500; margin-bottom:6px;
  display:flex; align-items:center; gap:10px; flex-wrap:wrap;
  color:var(--text);
}
.tech {
  font-size:11px; font-weight:500;
  background:rgba(78,205,196,0.08);
  color:var(--teal);
  border:1px solid rgba(78,205,196,0.2);
  padding:2px 10px; border-radius:100px;
}
.how-content p { color:var(--muted); font-size:14px; font-weight:300; line-height:1.7; }

/* ===== DEMO ===== */
.demo-wrap { display:grid; grid-template-columns:1fr 360px; gap:28px; align-items:start; }
.cam-box {
  background:var(--bg3);
  border:1px solid var(--border);
  border-radius:18px; overflow:hidden;
  aspect-ratio:4/3; position:relative;
}
.cam-ph {
  position:absolute; inset:0;
  display:flex; flex-direction:column;
  align-items:center; justify-content:center; gap:14px;
}
.cam-ph p { color:var(--muted); font-size:14px; }
.cam-footer { display:flex; align-items:center; justify-content:space-between; margin-top:10px; }
.status-row { display:flex; align-items:center; gap:7px; font-size:13px; color:var(--muted); }
.dot { width:7px;height:7px;border-radius:50%;background:#333; }
.dot.on { background:var(--teal); animation:pulse 1.5s infinite; }
.btn-stop {
  font-size:13px; font-weight:500; color:#f87171;
  background:rgba(248,113,113,.08); border:1px solid rgba(248,113,113,.15);
  padding:7px 16px; border-radius:8px; cursor:pointer;
  font-family:'DM Sans',sans-serif; transition:.2s;
}
.btn-stop:hover { background:rgba(248,113,113,.12); }

/* ===== PANEL ===== */
.demo-panel { display:flex; flex-direction:column; gap:12px; }
.panel-block {
  background:var(--card); border:1px solid var(--border);
  border-radius:14px; padding:20px 22px;
}
.block-label {
  font-size:10px; font-weight:500; text-transform:uppercase;
  letter-spacing:2px; color:var(--muted); margin-bottom:12px;
}
.mode-row { display:flex; gap:8px; }
.mode-btn {
  flex:1; padding:10px 8px; border-radius:8px;
  border:1px solid var(--border); background:transparent;
  color:var(--muted); font-size:13px; font-weight:400;
  cursor:pointer; font-family:'DM Sans',sans-serif; transition:.2s;
}
.mode-btn:hover { border-color:var(--border2); color:var(--text); }
.mode-btn.active {
  background:rgba(201,169,110,0.1);
  border-color:rgba(201,169,110,0.3);
  color:var(--gold);
}
.letter-display { display:flex; align-items:center; gap:20px; }
#big-letter {
  font-family:'Cormorant Garamond',serif;
  font-size:76px; font-weight:700; color:var(--gold); line-height:1;
}
.conf-wrap { flex:1; }
.conf-track { height:3px;background:rgba(255,255,255,.06);border-radius:2px;margin-bottom:6px;overflow:hidden; }
.conf-bar { height:100%;background:var(--teal);border-radius:2px;width:0%;transition:width .3s; }
#conf-text { font-size:12px;color:var(--muted); }
.word-out {
  font-family:'Cormorant Garamond',serif;
  font-size:26px; font-weight:700; color:var(--text);
  min-height:36px; word-break:break-all; margin-bottom:14px;
}
.word-btns { display:flex; gap:8px; }
.wb-btn {
  flex:1; padding:10px 8px; border:1px solid var(--border);
  border-radius:8px; background:transparent; color:var(--muted);
  font-size:13px; font-weight:400; cursor:pointer;
  font-family:'DM Sans',sans-serif; transition:.2s;
}
.wb-btn:hover { border-color:var(--border2); color:var(--text); }
.wb-btn.speak {
  background:rgba(78,205,196,.1); border-color:rgba(78,205,196,.25); color:var(--teal);
}
.wb-btn.speak:hover { background:rgba(78,205,196,.15); }

.alpha-grid { display:grid; grid-template-columns:repeat(auto-fill,minmax(38px,1fr)); gap:5px; }
.alpha-key {
  background:rgba(255,255,255,.04); border:1px solid var(--border);
  border-radius:6px; padding:7px 4px; text-align:center;
  font-size:13px; font-weight:500; color:var(--muted); transition:.15s;
}
.alpha-key.lit {
  background:rgba(201,169,110,.12); border-color:rgba(201,169,110,.3);
  color:var(--gold); transform:scale(1.1);
}
.voice-out { font-size:18px; min-height:48px; color:var(--text); padding:8px 0; }
.status-pill {
  display:inline-block; font-size:12px; font-weight:400;
  padding:3px 12px; border-radius:100px;
  background:rgba(255,255,255,.04); border:1px solid var(--border);
  color:var(--muted); margin-top:8px;
}
.status-pill.ok  { background:rgba(78,205,196,.08); border-color:rgba(78,205,196,.2); color:var(--teal); }
.status-pill.err { background:rgba(248,113,113,.06); border-color:rgba(248,113,113,.15); color:#f87171; }

/* ===== TEAM ===== */
.team-grid {
  display:grid; grid-template-columns:repeat(auto-fill,minmax(200px,1fr));
  gap:18px; margin-top:48px;
}
.team-card {
  background:var(--card); border:1px solid var(--border);
  border-radius:18px; padding:28px 22px; text-align:center;
  transition:border-color .2s, transform .2s;
}
.team-card:hover { border-color:rgba(201,169,110,.25); transform:translateY(-4px); }
.avatar {
  width:64px; height:64px; border-radius:50%;
  display:flex; align-items:center; justify-content:center;
  font-family:'Cormorant Garamond',serif;
  font-size:22px; font-weight:700; margin:0 auto 14px;
}
.team-card h3 { font-size:15px; font-weight:500; margin-bottom:4px; color:var(--text); }
.team-role { font-size:13px; color:var(--muted); }
.team-contrib { font-size:12px; margin-top:8px; font-weight:500; }

/* ===== FOOTER ===== */
footer {
  background:var(--bg); border-top:1px solid var(--border);
  padding:60px 64px; text-align:center;
}
.footer-inner { max-width:600px; margin:0 auto; }
.footer-logo {
  font-family:'DM Sans',sans-serif;
  font-size:20px; font-weight:500; color:var(--gold); margin-bottom:14px;
}
footer p { font-size:14px; color:var(--muted); margin-bottom:6px; }
.footer-sub { font-size:13px; color:rgba(255,255,255,.2) !important; }
.footer-tech { display:flex; flex-wrap:wrap; gap:8px; justify-content:center; margin-top:24px; }
.footer-tech span {
  font-size:11px; background:rgba(255,255,255,.04);
  border:1px solid var(--border); color:var(--muted);
  padding:4px 12px; border-radius:100px;
}

/* ===== RESPONSIVE ===== */
@media(max-width:900px) {
  nav { padding:16px 24px; }
  .nav-links { display:none; }
  section { padding:60px 24px; }
  #hero { padding:100px 24px 60px; }
  .hero-inner { grid-template-columns:1fr; gap:40px; }
  .about-grid { grid-template-columns:1fr; }
  .demo-wrap { grid-template-columns:1fr; }
  .hero-right { display:none; }
}

# bubbles html

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>SignBridge — Sign Language Recognition</title>
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800;900&family=Crimson+Pro:ital,wght@1,400;1,600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css">
</head>
<body>

<!-- PARTICLE CANVAS -->
<canvas id="particles"></canvas>

<nav>
  <div class="nav-logo"><span class="nav-icon">✋</span> SignBridge</div>
  <div class="nav-links">
    <a href="#about">About</a>
    <a href="#how">How it works</a>
    <a href="#demo">Live demo</a>
    <a href="#team">Team</a>
  </div>
</nav>

<!-- HERO -->
<section id="hero">
  <div class="hero-content">
    <div class="hero-tag"><span class="pulse-dot"></span> B.Tech Project — ML &amp; DL</div>
    <h1>Sign language<br>meets <em>intelligence</em></h1>
    <p class="hero-sub">Real-time gesture recognition that bridges communication between deaf, mute, and blind individuals using computer vision and deep learning.</p>
    <div class="hero-btns">
      <a href="#demo" class="btn-primary">Try live demo</a>
      <a href="#how"  class="btn-secondary">How it works ↓</a>
    </div>
    <div class="hero-chips">
      <span>OpenCV</span><span>MediaPipe</span><span>TensorFlow</span><span>Flask</span><span>pyttsx3</span>
    </div>
  </div>
  <div class="hero-stats">
    <div class="stat-card"><div class="stat-n">26+</div><div class="stat-l">Gestures</div></div>
    <div class="stat-card"><div class="stat-n">96%</div><div class="stat-l">Accuracy</div></div>
    <div class="stat-card"><div class="stat-n">21</div><div class="stat-l">Landmarks</div></div>
    <div class="stat-card"><div class="stat-n">2</div><div class="stat-l">Modes</div></div>
  </div>
</section>

<!-- ABOUT -->
<section id="about" class="section glass-section">
  <div class="section-inner">
    <div class="s-label">About</div>
    <h2>Who does this help?</h2>
    <div class="cards-3">
      <div class="g-card"><div class="g-icon">🤟</div><h3>Deaf &amp; mute users</h3><p>Show a hand gesture to the camera. The system detects it, recognizes the sign, and speaks it out loud instantly using pyttsx3.</p></div>
      <div class="g-card"><div class="g-icon">🎙️</div><h3>Blind users</h3><p>Speak naturally into the microphone. The system transcribes your speech to text on screen in real-time using SpeechRecognition.</p></div>
      <div class="g-card"><div class="g-icon">🔁</div><h3>Two-way communication</h3><p>Both modes work together. Switch between sign-to-voice and voice-to-text with one tap for complete conversations.</p></div>
    </div>
  </div>
</section>

<!-- HOW IT WORKS -->
<section id="how" class="section">
  <div class="section-inner">
    <div class="s-label">Technology</div>
    <h2>How it works</h2>
    <p class="s-sub">Five modules working together in under 100ms.</p>
    <div class="steps-row">
      <div class="step-item"><div class="step-num">01</div><div class="step-tech">OpenCV</div><h3>Camera capture</h3><p>Reads webcam frames at 30fps and passes each to MediaPipe.</p></div>
      <div class="step-arrow">→</div>
      <div class="step-item"><div class="step-num">02</div><div class="step-tech">MediaPipe</div><h3>Hand detection</h3><p>Maps 21 landmark points per hand as x, y, z coordinates.</p></div>
      <div class="step-arrow">→</div>
      <div class="step-item"><div class="step-num">03</div><div class="step-tech">TensorFlow</div><h3>Recognition</h3><p>CNN model identifies the gesture from 63 coordinates.</p></div>
      <div class="step-arrow">→</div>
      <div class="step-item"><div class="step-num">04</div><div class="step-tech">pyttsx3</div><h3>Speech output</h3><p>Converts predicted text to natural voice instantly.</p></div>
    </div>
  </div>
</section>

<!-- DEMO -->
<section id="demo" class="section glass-section">
  <div class="section-inner">
    <div class="s-label">Interactive demo</div>
    <h2>Try it live</h2>
    <p class="s-sub">Start camera, show your hand — predictions happen in real-time.<br>
    <span id="backend-status" class="b-pill">Checking backend...</span></p>
    <div class="demo-layout">
      <div>
        <div class="cam-box">
          <img id="cam-feed" style="width:100%;height:100%;object-fit:cover;display:none;border-radius:16px;" alt="feed">
          <div id="cam-placeholder" class="cam-ph">
            <div style="font-size:52px">📷</div>
            <p>Camera not started</p>
            <button class="btn-primary" id="start-btn" onclick="startCamera()">Start camera</button>
          </div>
        </div>
        <div class="cam-foot">
          <div class="s-row"><div class="dot" id="status-dot"></div><span id="status-text">No hand detected</span></div>
          <button class="stop-btn" id="stop-btn" onclick="stopCamera()" style="display:none">Stop</button>
        </div>
      </div>
      <div class="d-panel">
        <div class="d-block">
          <div class="d-label">Mode</div>
          <div class="mode-row">
            <button class="mode-btn active" id="mode-sign"  onclick="setMode('sign')">✋ Sign → Voice</button>
            <button class="mode-btn"        id="mode-voice" onclick="setMode('voice')">🎙 Voice → Text</button>
          </div>
        </div>
        <div class="d-block">
          <div class="d-label">Detected gesture</div>
          <div style="display:flex;align-items:center;gap:16px">
            <div id="big-letter" class="big-l">—</div>
            <div style="flex:1">
              <div class="c-track"><div id="conf-fill" class="c-fill"></div></div>
              <div id="conf-text" style="font-size:12px;color:var(--muted);margin-top:5px">—</div>
            </div>
          </div>
        </div>
        <div class="d-block">
          <div class="d-label">Word builder</div>
          <div id="word-display" class="word-d">—</div>
          <div class="w-btns">
            <button class="w-btn" onclick="addLetter()">Add</button>
            <button class="w-btn" onclick="clearWord()">Clear</button>
            <button class="w-btn green" onclick="speakWord()">🔊 Speak</button>
          </div>
        </div>
        <div class="d-block">
          <div class="d-label">ASL reference</div>
          <div class="a-grid" id="alpha-grid"></div>
        </div>
      </div>
    </div>
    <div id="voice-panel" style="display:none;margin-top:24px">
      <div class="d-block" style="max-width:540px">
        <div class="d-label">Voice to text — blind user mode</div>
        <div id="voice-output" style="font-size:18px;min-height:46px;color:var(--text);padding:8px 0">Speak into your microphone...</div>
        <button class="btn-primary" id="voice-btn" onclick="toggleVoice()" style="margin-top:14px">🎙 Start listening</button>
      </div>
    </div>
  </div>
</section>

<!-- TEAM -->
<section id="team" class="section">
  <div class="section-inner">
    <div class="s-label">Our team</div>
    <h2>The builders</h2>
    <p class="s-sub">B.Tech students making communication accessible for everyone.</p>
    <div class="team-g" id="team-grid"></div>
  </div>
</section>

<footer>
  <div class="foot-inner">
    <div class="foot-logo">✋ SignBridge</div>
    <p>Enhancing Accessibility using Sign Language Recognition with ML &amp; DL</p>
    <p class="foot-sub">B.Tech · Academic Project</p>
    <div class="foot-tech">
      <span>Python</span><span>OpenCV</span><span>MediaPipe</span><span>TensorFlow</span><span>Flask</span><span>pyttsx3</span>
    </div>
  </div>
</footer>

<script src="script.js"></script>
<script>
// ---- Particle background ----
const canvas = document.getElementById('particles');
const ctx = canvas.getContext('2d');
let W, H, particles = [];

function resize() {
  W = canvas.width  = window.innerWidth;
  H = canvas.height = window.innerHeight;
}
resize();
window.addEventListener('resize', resize);

class Particle {
  constructor() { this.reset(); }
  reset() {
    this.x  = Math.random() * W;
    this.y  = Math.random() * H;
    this.r  = Math.random() * 2 + 0.5;
    this.vx = (Math.random() - 0.5) * 0.4;
    this.vy = (Math.random() - 0.5) * 0.4;
    this.a  = Math.random() * 0.5 + 0.1;
    this.color = Math.random() > 0.5 ? '139,92,246' : '56,189,248';
  }
  update() {
    this.x += this.vx; this.y += this.vy;
    if (this.x < 0 || this.x > W || this.y < 0 || this.y > H) this.reset();
  }
  draw() {
    ctx.beginPath();
    ctx.arc(this.x, this.y, this.r, 0, Math.PI * 2);
    ctx.fillStyle = `rgba(${this.color},${this.a})`;
    ctx.fill();
  }
}

for (let i = 0; i < 120; i++) particles.push(new Particle());

function drawConnections() {
  for (let i = 0; i < particles.length; i++) {
    for (let j = i + 1; j < particles.length; j++) {
      const dx = particles[i].x - particles[j].x;
      const dy = particles[i].y - particles[j].y;
      const dist = Math.sqrt(dx*dx + dy*dy);
      if (dist < 100) {
        ctx.beginPath();
        ctx.moveTo(particles[i].x, particles[i].y);
        ctx.lineTo(particles[j].x, particles[j].y);
        ctx.strokeStyle = `rgba(139,92,246,${0.06 * (1 - dist/100)})`;
        ctx.lineWidth = 0.5;
        ctx.stroke();
      }
    }
  }
}

function animate() {
  ctx.clearRect(0, 0, W, H);
  particles.forEach(p => { p.update(); p.draw(); });
  drawConnections();
  requestAnimationFrame(animate);
}
animate();

// ---- Team ----
const team = [
  { name:"Member 1", role:"ML Engineer",       contrib:"CNN model & training",  color:"#a78bfa", bg:"rgba(167,139,250,0.12)" },
  { name:"Member 2", role:"Computer Vision",   contrib:"MediaPipe integration", color:"#38bdf8", bg:"rgba(56,189,248,0.12)"  },
  { name:"Member 3", role:"Backend Dev",       contrib:"Flask API & Python",    color:"#34d399", bg:"rgba(52,211,153,0.12)"  },
  { name:"Member 4", role:"Frontend Dev",      contrib:"UI & website",          color:"#fb923c", bg:"rgba(251,146,60,0.12)"  },
  { name:"Member 5", role:"Data Engineer",     contrib:"Dataset & collection",  color:"#f472b6", bg:"rgba(244,114,182,0.12)" },
];
const grid = document.getElementById("team-grid");
team.forEach(m => {
  const initials = m.name.split(" ").map(w=>w[0]).join("");
  grid.innerHTML += `
    <div class="t-card">
      <div class="t-avatar" style="background:${m.bg};color:${m.color}">${initials}</div>
      <h3>${m.name}</h3>
      <div class="t-role">${m.role}</div>
      <div class="t-contrib" style="color:${m.color}">${m.contrib}</div>
    </div>`;
});
</script>
</body>
</html>

# css
 
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800;900&family=Crimson+Pro:ital,wght@1,400;1,600&display=swap');

:root {
  --bg:     #080810;
  --bg2:    #0e0e1a;
  --bg3:    #13131f;
  --card:   rgba(255,255,255,0.04);
  --glass:  rgba(255,255,255,0.03);
  --border: rgba(255,255,255,0.08);
  --border2:rgba(255,255,255,0.12);
  --text:   #f0eeff;
  --muted:  #7a7a9a;
  --purple: #a78bfa;
  --blue:   #38bdf8;
  --green:  #34d399;
  --pink:   #f472b6;
}

*{margin:0;padding:0;box-sizing:border-box;}
html{scroll-behavior:smooth;}

body {
  background: var(--bg);
  color: var(--text);
  font-family: 'Outfit', sans-serif;
  font-size: 16px; line-height: 1.7;
  overflow-x: hidden;
}

/* particle canvas fixed behind everything */
#particles {
  position: fixed; top:0; left:0;
  width:100%; height:100%;
  z-index: 0; pointer-events: none;
}

/* all content above canvas */
nav, section, footer { position: relative; z-index: 1; }

/* ── NAV ── */
nav {
  position: fixed; top:0; left:0; right:0; z-index: 100;
  display: flex; align-items: center; justify-content: space-between;
  padding: 0 64px; height: 68px;
  background: rgba(8,8,16,0.8);
  backdrop-filter: blur(20px);
  border-bottom: 1px solid var(--border);
}
.nav-logo {
  display: flex; align-items: center; gap: 10px;
  font-size: 18px; font-weight: 700; color: var(--text);
  letter-spacing: -0.3px;
}
.nav-icon {
  width: 32px; height: 32px; border-radius: 9px;
  background: linear-gradient(135deg, var(--purple), var(--blue));
  display: flex; align-items: center; justify-content: center;
  font-size: 16px;
}
.nav-links { display: flex; gap: 36px; }
.nav-links a {
  color: var(--muted); text-decoration: none;
  font-size: 14px; font-weight: 400; transition: color .2s;
}
.nav-links a:hover { color: var(--text); }

/* ── HERO ── */
#hero {
  min-height: 100vh;
  display: flex; flex-direction: column;
  align-items: center; justify-content: center;
  padding: 100px 64px 60px; text-align: center;
}
.hero-tag {
  display: inline-flex; align-items: center; gap: 8px;
  font-size: 12px; font-weight: 500; letter-spacing: 1px;
  color: var(--purple);
  background: rgba(167,139,250,0.08);
  border: 1px solid rgba(167,139,250,0.2);
  padding: 6px 18px; border-radius: 100px;
  margin-bottom: 36px;
  animation: fadeUp .6s ease both;
}
.pulse-dot {
  width: 6px; height: 6px; border-radius: 50%;
  background: var(--purple); animation: pulse 2s infinite;
}
@keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.3} }

h1 {
  font-size: clamp(48px, 7vw, 90px);
  font-weight: 900; line-height: 1.0;
  letter-spacing: -3px; margin-bottom: 28px;
  animation: fadeUp .6s .1s ease both;
  background: linear-gradient(135deg, #ffffff 0%, #c4b5fd 50%, #38bdf8 100%);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
  background-clip: text;
}
h1 em {
  font-family: 'Crimson Pro', serif;
  font-style: italic; font-weight: 600;
  font-size: 1.05em;
}

.hero-sub {
  max-width: 560px; color: var(--muted);
  font-size: 17px; font-weight: 300;
  margin: 0 auto 44px; line-height: 1.8;
  animation: fadeUp .6s .2s ease both;
}
.hero-btns {
  display: flex; gap: 14px; justify-content: center;
  margin-bottom: 48px;
  animation: fadeUp .6s .3s ease both;
}

/* buttons */
.btn-primary {
  background: linear-gradient(135deg, var(--purple), var(--blue));
  color: #fff; padding: 14px 32px; border-radius: 100px;
  font-size: 14px; font-weight: 600; letter-spacing: 0.3px;
  text-decoration: none; border: none; cursor: pointer;
  font-family: 'Outfit', sans-serif;
  transition: transform .2s, box-shadow .2s; display: inline-block;
}
.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 30px rgba(167,139,250,0.4);
}
.btn-secondary {
  background: transparent; color: var(--text);
  padding: 14px 32px; border-radius: 100px;
  font-size: 14px; font-weight: 500;
  text-decoration: none; border: 1px solid var(--border2);
  cursor: pointer; font-family: 'Outfit', sans-serif;
  transition: .2s; display: inline-block;
}
.btn-secondary:hover { border-color: rgba(255,255,255,.25); background: var(--glass); }

.hero-chips {
  display: flex; gap: 10px; justify-content: center; flex-wrap: wrap;
  animation: fadeUp .6s .4s ease both;
}
.hero-chips span {
  font-size: 12px; font-weight: 500;
  background: rgba(255,255,255,0.05);
  border: 1px solid var(--border);
  color: var(--muted); padding: 5px 14px; border-radius: 100px;
}

.hero-stats {
  display: flex; gap: 16px; justify-content: center;
  margin-top: 60px; flex-wrap: wrap;
  animation: fadeUp .6s .5s ease both;
}
.stat-card {
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: 16px; padding: 20px 28px;
  text-align: center; min-width: 110px;
  backdrop-filter: blur(10px);
  transition: border-color .2s, transform .2s;
}
.stat-card:hover { border-color: rgba(167,139,250,0.3); transform: translateY(-3px); }
.stat-n {
  font-size: 32px; font-weight: 800; color: var(--purple);
  display: block; line-height: 1; letter-spacing: -1px;
}
.stat-l { font-size: 12px; color: var(--muted); margin-top: 5px; display: block; }

@keyframes fadeUp {
  from{opacity:0;transform:translateY(24px)}
  to{opacity:1;transform:translateY(0)}
}

/* ── SECTIONS ── */
.section { padding: 100px 64px; }
.section-inner { max-width: 1160px; margin: 0 auto; }

.glass-section {
  background: rgba(255,255,255,0.01);
  border-top: 1px solid var(--border);
  border-bottom: 1px solid var(--border);
  backdrop-filter: blur(10px);
}

.s-label {
  font-size: 11px; font-weight: 600; letter-spacing: 2.5px;
  text-transform: uppercase; color: var(--purple); margin-bottom: 14px;
}
h2 {
  font-size: clamp(28px, 3.5vw, 48px); font-weight: 800;
  letter-spacing: -1.5px; line-height: 1.05; margin-bottom: 16px;
  background: linear-gradient(135deg, #fff 40%, #c4b5fd 100%);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
  background-clip: text;
}
.s-sub {
  color: var(--muted); font-size: 16px; font-weight: 300;
  max-width: 480px; margin-bottom: 52px; line-height: 1.8;
}

/* ── ABOUT CARDS ── */
.cards-3 {
  display: grid; grid-template-columns: repeat(3,1fr);
  gap: 20px; margin-top: 48px;
}
.g-card {
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: 20px; padding: 36px 28px;
  backdrop-filter: blur(10px);
  transition: border-color .2s, transform .2s;
  position: relative; overflow: hidden;
}
.g-card::before {
  content:''; position:absolute; top:0; left:0; right:0; height:1px;
  background: linear-gradient(90deg, transparent, var(--purple), transparent);
  opacity: 0; transition: opacity .3s;
}
.g-card:hover { border-color: rgba(167,139,250,0.25); transform: translateY(-4px); }
.g-card:hover::before { opacity: 1; }
.g-icon { font-size: 32px; margin-bottom: 18px; }
.g-card h3 { font-size: 17px; font-weight: 700; margin-bottom: 10px; letter-spacing: -0.3px; }
.g-card p { color: var(--muted); font-size: 14px; line-height: 1.75; }

/* ── HOW IT WORKS ── */
.steps-row {
  display: flex; align-items: flex-start;
  gap: 0; margin-top: 48px;
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: 20px; overflow: hidden;
  backdrop-filter: blur(10px);
}
.step-item {
  flex: 1; padding: 36px 28px;
  border-right: 1px solid var(--border);
  transition: background .2s;
}
.step-item:last-child { border-right: none; }
.step-item:hover { background: rgba(255,255,255,0.03); }
.step-arrow {
  display: flex; align-items: center; justify-content: center;
  padding: 0 0; color: var(--muted); font-size: 20px;
  align-self: center; flex-shrink: 0;
  display: none;
}
.step-num {
  font-size: 11px; font-weight: 700; letter-spacing: 2px;
  color: var(--purple); margin-bottom: 12px;
}
.step-tech {
  display: inline-block; font-size: 11px; font-weight: 600;
  background: rgba(56,189,248,0.1); color: var(--blue);
  border: 1px solid rgba(56,189,248,0.2);
  padding: 3px 10px; border-radius: 6px; margin-bottom: 12px;
}
.step-item h3 { font-size: 15px; font-weight: 700; margin-bottom: 8px; letter-spacing: -0.2px; }
.step-item p { color: var(--muted); font-size: 13px; line-height: 1.7; }

/* ── DEMO ── */
.demo-layout { display: grid; grid-template-columns: 1fr 340px; gap: 24px; align-items: start; }
.cam-box {
  background: var(--bg3); border: 1px solid var(--border);
  border-radius: 20px; overflow: hidden; aspect-ratio: 4/3; position: relative;
}
.cam-ph {
  position: absolute; inset: 0;
  display: flex; flex-direction: column;
  align-items: center; justify-content: center; gap: 14px;
}
.cam-ph p { color: var(--muted); font-size: 14px; }
.cam-foot { display: flex; align-items: center; justify-content: space-between; margin-top: 10px; }
.s-row { display: flex; align-items: center; gap: 7px; font-size: 13px; color: var(--muted); }
.dot { width: 7px; height: 7px; border-radius: 50%; background: #333; }
.dot.on { background: var(--green); animation: pulse 1.5s infinite; }
.stop-btn {
  font-size: 12px; font-weight: 600; color: #f87171;
  background: rgba(248,113,113,.08); border: 1px solid rgba(248,113,113,.15);
  padding: 7px 16px; border-radius: 100px; cursor: pointer;
  font-family: 'Outfit', sans-serif; transition: .2s;
}
.stop-btn:hover { background: rgba(248,113,113,.12); }

.d-panel { display: flex; flex-direction: column; gap: 12px; }
.d-block {
  background: var(--card); border: 1px solid var(--border);
  border-radius: 14px; padding: 20px 22px;
  backdrop-filter: blur(10px);
}
.d-label {
  font-size: 10px; font-weight: 700; text-transform: uppercase;
  letter-spacing: 2px; color: var(--muted); margin-bottom: 12px;
}
.mode-row { display: flex; gap: 8px; }
.mode-btn {
  flex: 1; padding: 10px 8px; border-radius: 100px;
  border: 1px solid var(--border); background: transparent;
  color: var(--muted); font-size: 12px; font-weight: 600;
  cursor: pointer; font-family: 'Outfit', sans-serif;
  letter-spacing: 0.3px; transition: .2s;
}
.mode-btn:hover { border-color: var(--border2); color: var(--text); }
.mode-btn.active {
  background: linear-gradient(135deg, rgba(167,139,250,0.2), rgba(56,189,248,0.2));
  border-color: rgba(167,139,250,0.4); color: var(--purple);
}
.big-l {
  font-size: 72px; font-weight: 900; color: var(--purple);
  line-height: 1; letter-spacing: -3px;
}
.c-track { height: 3px; background: rgba(255,255,255,.06); border-radius: 2px; overflow: hidden; }
.c-fill { height: 100%; background: linear-gradient(90deg, var(--purple), var(--blue)); border-radius: 2px; width: 0%; transition: width .3s; }
.word-d {
  font-size: 24px; font-weight: 800; letter-spacing: -1px;
  color: var(--text); min-height: 36px; word-break: break-all; margin-bottom: 14px;
}
.w-btns { display: flex; gap: 8px; }
.w-btn {
  flex: 1; padding: 10px 8px; border: 1px solid var(--border);
  border-radius: 100px; background: transparent; color: var(--muted);
  font-size: 12px; font-weight: 600; cursor: pointer;
  font-family: 'Outfit', sans-serif; transition: .2s;
}
.w-btn:hover { border-color: var(--border2); color: var(--text); }
.w-btn.green {
  background: rgba(52,211,153,.12); border-color: rgba(52,211,153,.3); color: var(--green);
}
.w-btn.green:hover { background: rgba(52,211,153,.18); }
.a-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(34px,1fr)); gap: 4px; }
.alpha-key {
  background: rgba(255,255,255,.04); border: 1px solid var(--border);
  border-radius: 7px; padding: 6px 4px; text-align: center;
  font-size: 12px; font-weight: 700; color: var(--muted); transition: .15s;
}
.alpha-key.lit {
  background: rgba(167,139,250,.15); border-color: rgba(167,139,250,.4);
  color: var(--purple); transform: scale(1.1);
}
.b-pill {
  display: inline-block; font-size: 11px; font-weight: 500;
  padding: 3px 12px; border-radius: 100px;
  background: rgba(255,255,255,.04); border: 1px solid var(--border);
  color: var(--muted); margin-top: 8px;
}
.b-pill.ok { background: rgba(52,211,153,.08); border-color: rgba(52,211,153,.2); color: var(--green); }
.b-pill.err { background: rgba(248,113,113,.06); border-color: rgba(248,113,113,.15); color: #f87171; }

/* ── TEAM ── */
.team-g {
  display: grid; grid-template-columns: repeat(auto-fill, minmax(200px,1fr));
  gap: 16px; margin-top: 48px;
}
.t-card {
  background: var(--card); border: 1px solid var(--border);
  border-radius: 18px; padding: 28px 22px; text-align: center;
  backdrop-filter: blur(10px);
  transition: border-color .2s, transform .2s;
}
.t-card:hover { border-color: rgba(167,139,250,0.25); transform: translateY(-4px); }
.t-avatar {
  width: 60px; height: 60px; border-radius: 16px;
  display: flex; align-items: center; justify-content: center;
  font-size: 20px; font-weight: 800; margin: 0 auto 14px;
}
.t-card h3 { font-size: 15px; font-weight: 700; margin-bottom: 4px; }
.t-role { font-size: 13px; color: var(--muted); }
.t-contrib { font-size: 12px; margin-top: 8px; font-weight: 600; }

/* ── FOOTER ── */
footer {
  border-top: 1px solid var(--border);
  padding: 60px 64px; text-align: center;
  background: rgba(0,0,0,0.4); backdrop-filter: blur(10px);
}
.foot-inner { max-width: 600px; margin: 0 auto; }
.foot-logo {
  font-size: 20px; font-weight: 800; letter-spacing: -0.5px;
  margin-bottom: 14px;
  background: linear-gradient(135deg, var(--purple), var(--blue));
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
  background-clip: text;
}
footer p { font-size: 14px; color: var(--muted); margin-bottom: 6px; }
.foot-sub { font-size: 12px; color: rgba(255,255,255,.2) !important; }
.foot-tech { display: flex; flex-wrap: wrap; gap: 8px; justify-content: center; margin-top: 24px; }
.foot-tech span {
  font-size: 11px; font-weight: 600;
  background: rgba(255,255,255,.04); border: 1px solid var(--border);
  color: var(--muted); padding: 4px 12px; border-radius: 100px;
}

/* ── RESPONSIVE ── */
@media(max-width:900px) {
  nav { padding: 0 24px; }
  .nav-links { display: none; }
  .section { padding: 60px 24px; }
  #hero { padding: 100px 24px 60px; }
  .cards-3 { grid-template-columns: 1fr; }
  .steps-row { flex-direction: column; }
  .step-item { border-right: none; border-bottom: 1px solid var(--border); }
  .demo-layout { grid-template-columns: 1fr; }
  footer { padding: 48px 24px; }
}
 # GREEN

 <!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>SignBridge — Sign Language Recognition</title>
<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=DM+Sans:ital,wght@0,300;0,400;0,500;0,700;1,300&family=DM+Serif+Display:ital@0;1&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css">
</head>
<body>

<nav>
  <div class="nav-logo">SignBridge</div>
  <div class="nav-links">
    <a href="#about">About</a>
    <a href="#how">How it works</a>
    <a href="#demo">Live demo</a>
    <a href="#team">Team</a>
    <a href="#demo" class="nav-cta">Try now</a>
  </div>
</nav>

<!-- HERO -->
<section id="hero">
  <div class="hero-l">
    <div class="hero-eyebrow">
      <div class="hero-eyebrow-line"></div>
      <span>B.Tech Project — ML &amp; DL</span>
    </div>
    <div class="hero-h1">
      SIGN<br>
      <span class="outline">LANGUAGE</span><br>
      <span class="lime">MEETS AI</span>
    </div>
    <p class="hero-desc">Real-time gesture recognition bridging communication between deaf, mute, and blind individuals using computer vision and deep learning.</p>
    <div class="hero-btns">
      <a href="#demo" class="btn-lime">Try live demo</a>
      <a href="#how"  class="btn-outline-w">Learn more</a>
    </div>
  </div>
  <div class="hero-r">
    <div class="hero-big-num">96</div>
    <div class="hero-stats-grid">
      <div class="hsg-item"><span class="hsg-n">26+</span><span class="hsg-l">ASL Gestures</span></div>
      <div class="hsg-item"><span class="hsg-n">96%</span><span class="hsg-l">Accuracy</span></div>
      <div class="hsg-item"><span class="hsg-n">21</span><span class="hsg-l">Hand Landmarks</span></div>
      <div class="hsg-item"><span class="hsg-n">2</span><span class="hsg-l">User Modes</span></div>
    </div>
  </div>
</section>

<!-- TICKER -->
<div class="ticker">
  <div class="ticker-track">
    <span>OpenCV</span><span class="ticker-dot">✦</span>
    <span>MediaPipe</span><span class="ticker-dot">✦</span>
    <span>TensorFlow</span><span class="ticker-dot">✦</span>
    <span>Flask</span><span class="ticker-dot">✦</span>
    <span>pyttsx3</span><span class="ticker-dot">✦</span>
    <span>SpeechRecognition</span><span class="ticker-dot">✦</span>
    <span>Sign Language Recognition</span><span class="ticker-dot">✦</span>
    <span>Deep Learning</span><span class="ticker-dot">✦</span>
    <span>OpenCV</span><span class="ticker-dot">✦</span>
    <span>MediaPipe</span><span class="ticker-dot">✦</span>
    <span>TensorFlow</span><span class="ticker-dot">✦</span>
    <span>Flask</span><span class="ticker-dot">✦</span>
    <span>pyttsx3</span><span class="ticker-dot">✦</span>
    <span>SpeechRecognition</span><span class="ticker-dot">✦</span>
    <span>Sign Language Recognition</span><span class="ticker-dot">✦</span>
    <span>Deep Learning</span><span class="ticker-dot">✦</span>
  </div>
</div>

<!-- ABOUT -->
<section id="about">
  <div class="section-inner">
    <div class="s-header">
      <div>
        <div class="s-num">01</div>
      </div>
      <div>
        <h2>Who does<br>this <em>help?</em></h2>
        <p class="s-sub">Designed for deaf, mute, and blind individuals — making communication barrier-free.</p>
      </div>
    </div>
    <div class="about-row">
      <div class="a-card">
        <div class="a-tag">Mode 01</div>
        <h3>Deaf &amp; mute users</h3>
        <p>Show a hand gesture to the camera. MediaPipe detects your landmarks, the CNN model recognizes the sign, and pyttsx3 speaks it out loud instantly.</p>
      </div>
      <div class="a-card">
        <div class="a-tag">Mode 02</div>
        <h3>Blind users</h3>
        <p>Speak naturally into the microphone. SpeechRecognition converts your voice to text displayed clearly on screen in real-time for others to read.</p>
      </div>
      <div class="a-card">
        <div class="a-tag">Feature</div>
        <h3>Two-way communication</h3>
        <p>Both modes work together. Switch between sign-to-voice and voice-to-text with a single tap for complete two-way conversations.</p>
      </div>
    </div>
  </div>
</section>

<!-- HOW IT WORKS -->
<section id="how">
  <div class="section-inner">
    <div class="s-header">
      <div><div class="s-num">02</div></div>
      <div>
        <h2>How it<br><em>works</em></h2>
        <p class="s-sub">Five modules working together in under 100ms — from hand gesture to spoken word.</p>
      </div>
    </div>
    <div class="how-row">
      <div class="how-card">
        <span class="hc-num">01</span>
        <div class="hc-tech">OpenCV</div>
        <h3>Camera capture</h3>
        <p>Opens webcam and reads frames at 30fps, passing each to MediaPipe.</p>
      </div>
      <div class="how-card">
        <span class="hc-num">02</span>
        <div class="hc-tech">MediaPipe</div>
        <h3>Hand detection</h3>
        <p>Maps 21 landmark points per hand as x, y, z coordinates.</p>
      </div>
      <div class="how-card">
        <span class="hc-num">03</span>
        <div class="hc-tech">TensorFlow</div>
        <h3>Gesture recognition</h3>
        <p>CNN model identifies gesture from 63 coordinates with confidence score.</p>
      </div>
      <div class="how-card">
        <span class="hc-num">04</span>
        <div class="hc-tech">pyttsx3</div>
        <h3>Text to speech</h3>
        <p>Converts predicted text to natural audio output instantly.</p>
      </div>
      <div class="how-card">
        <span class="hc-num">05</span>
        <div class="hc-tech">SpeechRecognition</div>
        <h3>Voice to text</h3>
        <p>Transcribes mic input in real-time for blind users.</p>
      </div>
    </div>
  </div>
</section>

<!-- DEMO -->
<section id="demo">
  <div class="section-inner">
    <div class="s-header">
      <div><div class="s-num">03</div></div>
      <div>
        <h2>Try it<br><em>live</em></h2>
        <p class="s-sub">Start camera, show your hand — predictions happen in real-time.<br>
        <span id="backend-status" class="b-pill">Checking backend...</span></p>
      </div>
    </div>
    <div class="demo-wrap">
      <div>
        <div class="cam-box">
          <img id="cam-feed" style="width:100%;height:100%;object-fit:cover;display:none;border-radius:12px;" alt="feed">
          <div id="cam-placeholder" class="cam-ph">
            <div style="font-size:52px">📷</div>
            <p>Camera not started</p>
            <button class="btn-lime" id="start-btn" onclick="startCamera()">Start camera</button>
          </div>
        </div>
        <div class="cam-foot">
          <div class="s-row"><div class="dot" id="status-dot"></div><span id="status-text">No hand detected</span></div>
          <button class="stop-btn" id="stop-btn" onclick="stopCamera()" style="display:none">Stop</button>
        </div>
      </div>
      <div class="d-panel">
        <div class="d-block">
          <div class="d-label">Mode</div>
          <div class="mode-row">
            <button class="mode-btn active" id="mode-sign"  onclick="setMode('sign')">✋ Sign → Voice</button>
            <button class="mode-btn"        id="mode-voice" onclick="setMode('voice')">🎙 Voice → Text</button>
          </div>
        </div>
        <div class="d-block">
          <div class="d-label">Detected gesture</div>
          <div style="display:flex;align-items:center;gap:16px">
            <div id="big-letter" class="big-l">—</div>
            <div style="flex:1">
              <div class="c-track"><div id="conf-fill" class="c-fill"></div></div>
              <div id="conf-text" style="font-size:12px;color:rgba(255,255,255,0.3);margin-top:5px">—</div>
            </div>
          </div>
        </div>
        <div class="d-block">
          <div class="d-label">Word builder</div>
          <div id="word-display" class="word-d">—</div>
          <div class="w-btns">
            <button class="w-btn" onclick="addLetter()">Add</button>
            <button class="w-btn" onclick="clearWord()">Clear</button>
            <button class="w-btn green" onclick="speakWord()">🔊 Speak</button>
          </div>
        </div>
        <div class="d-block">
          <div class="d-label">ASL reference</div>
          <div class="a-grid" id="alpha-grid"></div>
        </div>
      </div>
    </div>
    <div id="voice-panel" style="display:none;margin-top:24px">
      <div class="d-block" style="max-width:540px">
        <div class="d-label">Voice to text — blind user mode</div>
        <div id="voice-output" style="font-size:18px;min-height:46px;color:#fff;padding:8px 0">Speak into your microphone...</div>
        <button class="btn-lime" id="voice-btn" onclick="toggleVoice()" style="margin-top:14px">🎙 Start listening</button>
      </div>
    </div>
  </div>
</section>

<!-- TEAM -->
<section id="team">
  <div class="section-inner">
    <div class="s-header">
      <div><div class="s-num">04</div></div>
      <div>
        <h2>The<br><em>builders</em></h2>
        <p class="s-sub">B.Tech students making communication accessible for everyone.</p>
      </div>
    </div>
    <div class="team-g" id="team-grid"></div>
  </div>
</section>

<!-- FOOTER -->
<footer>
  <div class="foot-inner">
    <div class="foot-logo">SignBridge</div>
    <div class="foot-mid">
      <p>Enhancing Accessibility using Sign Language Recognition with ML &amp; DL</p>
      <p class="foot-sub">B.Tech · Academic Project</p>
    </div>
    <div class="foot-tech">
      <span>Python</span><span>OpenCV</span><span>MediaPipe</span>
      <span>TensorFlow</span><span>Flask</span><span>pyttsx3</span>
    </div>
  </div>
</footer>

<script src="script.js"></script>
<script>
const team = [
  { name:"Member 1", role:"ML Engineer",       contrib:"CNN model & training",  color:"#e63329", bg:"rgba(230,51,41,0.08)"  },
  { name:"Member 2", role:"Computer Vision",   contrib:"MediaPipe integration", color:"#1a3cff", bg:"rgba(26,60,255,0.08)"  },
  { name:"Member 3", role:"Backend Dev",       contrib:"Flask API & Python",    color:"#b8f55a", bg:"rgba(184,245,90,0.15)" },
  { name:"Member 4", role:"Frontend Dev",      contrib:"UI & website",          color:"#e63329", bg:"rgba(230,51,41,0.08)"  },
  { name:"Member 5", role:"Data Engineer",     contrib:"Dataset & collection",  color:"#1a3cff", bg:"rgba(26,60,255,0.08)"  },
];
const grid = document.getElementById("team-grid");
team.forEach(m => {
  const initials = m.name.split(" ").map(w=>w[0]).join("");
  grid.innerHTML += `
    <div class="t-card">
      <div class="t-avatar" style="background:${m.bg};color:${m.color}">${initials}</div>
      <h3>${m.name}</h3>
      <div class="t-role">${m.role}</div>
      <div class="t-contrib" style="color:${m.color}">${m.contrib}</div>
    </div>`;
});
</script>
</body>
</html>

#CSS
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=DM+Sans:ital,wght@0,300;0,400;0,500;1,300&family=DM+Serif+Display:ital@0;1&display=swap');

:root {
  --bg:      #f5f2eb;
  --white:   #fdfcf8;
  --ink:     #111110;
  --ink2:    #2a2a28;
  --muted:   #888880;
  --line:    #dedad2;
  --lime:    #b8f55a;
  --lime-d:  #8bc43a;
  --red:     #e63329;
  --blue:    #1a3cff;
}

*{margin:0;padding:0;box-sizing:border-box;}
html{scroll-behavior:smooth;}
body{
  background:var(--bg);
  color:var(--ink);
  font-family:'DM Sans',sans-serif;
  font-size:16px;line-height:1.7;
  overflow-x:hidden;
}

/* ── NAV ── */
nav{
  position:fixed;top:0;left:0;right:0;z-index:100;
  display:flex;align-items:center;justify-content:space-between;
  padding:0 48px;height:60px;
  background:var(--ink);
}
.nav-logo{
  font-family:'Bebas Neue',sans-serif;
  font-size:22px;letter-spacing:2px;
  color:var(--lime);
}
.nav-links{display:flex;gap:32px;align-items:center;}
.nav-links a{
  color:rgba(255,255,255,0.5);text-decoration:none;
  font-size:12px;font-weight:500;letter-spacing:1px;
  text-transform:uppercase;transition:color .2s;
}
.nav-links a:hover{color:#fff;}
.nav-cta{
  background:var(--lime);color:var(--ink);
  padding:8px 20px;border-radius:4px;
  font-size:12px;font-weight:700;letter-spacing:1px;
  text-transform:uppercase;text-decoration:none;
  transition:background .2s;
}
.nav-cta:hover{background:var(--lime-d);}

/* ── HERO ── */
#hero{
  min-height:100vh;
  background:var(--ink);
  display:grid;grid-template-columns:1fr 1fr;
  overflow:hidden;position:relative;
}

/* animated noise texture */
#hero::before{
  content:'';position:absolute;inset:0;
  background-image:url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)' opacity='0.04'/%3E%3C/svg%3E");
  pointer-events:none;opacity:0.4;
}

.hero-l{
  padding:120px 48px 80px;
  display:flex;flex-direction:column;justify-content:center;
  position:relative;z-index:1;
  border-right:1px solid rgba(255,255,255,0.06);
}
.hero-eyebrow{
  display:flex;align-items:center;gap:12px;
  margin-bottom:32px;
  animation:fadeUp .5s ease both;
}
.hero-eyebrow-line{width:32px;height:2px;background:var(--lime);}
.hero-eyebrow span{
  font-size:11px;font-weight:500;letter-spacing:3px;
  text-transform:uppercase;color:var(--lime);
}
.hero-h1{
  font-family:'Bebas Neue',sans-serif;
  font-size:clamp(72px,8vw,120px);
  line-height:0.92;letter-spacing:2px;
  color:#fff;margin-bottom:32px;
  animation:fadeUp .5s .1s ease both;
}
.hero-h1 .outline{
  -webkit-text-stroke:1px rgba(255,255,255,0.3);
  color:transparent;
}
.hero-h1 .lime{color:var(--lime);}

.hero-desc{
  color:rgba(255,255,255,0.45);
  font-size:15px;font-weight:300;
  max-width:400px;line-height:1.8;
  margin-bottom:48px;
  animation:fadeUp .5s .2s ease both;
}
.hero-btns{display:flex;gap:12px;animation:fadeUp .5s .3s ease both;}
.btn-lime{
  background:var(--lime);color:var(--ink);
  padding:14px 32px;border-radius:4px;
  font-size:13px;font-weight:700;letter-spacing:1px;text-transform:uppercase;
  text-decoration:none;border:none;cursor:pointer;
  font-family:'DM Sans',sans-serif;
  transition:background .2s,transform .2s;display:inline-block;
}
.btn-lime:hover{background:var(--lime-d);transform:translateY(-1px);}
.btn-outline-w{
  background:transparent;color:rgba(255,255,255,0.6);
  padding:14px 32px;border-radius:4px;
  font-size:13px;font-weight:500;letter-spacing:1px;text-transform:uppercase;
  text-decoration:none;border:1px solid rgba(255,255,255,0.15);
  cursor:pointer;font-family:'DM Sans',sans-serif;transition:.2s;display:inline-block;
}
.btn-outline-w:hover{border-color:rgba(255,255,255,.35);color:#fff;}

.hero-r{
  display:flex;flex-direction:column;justify-content:flex-end;
  padding:120px 48px 80px;
  position:relative;z-index:1;
}
.hero-big-num{
  font-family:'Bebas Neue',sans-serif;
  font-size:clamp(120px,14vw,200px);
  line-height:1;letter-spacing:-2px;
  color:rgba(255,255,255,0.04);
  position:absolute;bottom:60px;right:48px;
}
.hero-stats-grid{
  display:grid;grid-template-columns:1fr 1fr;
  gap:1px;background:rgba(255,255,255,0.06);
  border:1px solid rgba(255,255,255,0.06);
  border-radius:12px;overflow:hidden;
  animation:fadeUp .5s .3s ease both;
}
.hsg-item{
  padding:28px 24px;background:var(--ink);
  transition:background .2s;
}
.hsg-item:hover{background:#1a1a18;}
.hsg-n{
  font-family:'Bebas Neue',sans-serif;
  font-size:48px;line-height:1;letter-spacing:1px;
  color:var(--lime);display:block;margin-bottom:4px;
}
.hsg-l{font-size:12px;color:rgba(255,255,255,0.35);letter-spacing:1px;text-transform:uppercase;}

@keyframes fadeUp{from{opacity:0;transform:translateY(20px)}to{opacity:1;transform:translateY(0)}}

/* ── TICKER ── */
.ticker{
  background:var(--lime);overflow:hidden;
  height:44px;display:flex;align-items:center;
}
.ticker-track{
  display:flex;gap:48px;
  animation:ticker 20s linear infinite;white-space:nowrap;
}
.ticker-track span{
  font-family:'Bebas Neue',sans-serif;
  font-size:18px;letter-spacing:3px;color:var(--ink);
}
.ticker-dot{color:var(--ink);opacity:0.3;}
@keyframes ticker{from{transform:translateX(0)}to{transform:translateX(-50%)}}

/* ── ABOUT ── */
#about{padding:100px 48px;background:var(--white);}
.section-inner{max-width:1160px;margin:0 auto;}
.s-header{
  display:grid;grid-template-columns:1fr 1fr;
  gap:48px;align-items:end;margin-bottom:64px;
  padding-bottom:40px;border-bottom:1px solid var(--line);
}
.s-num{
  font-family:'Bebas Neue',sans-serif;
  font-size:80px;line-height:1;letter-spacing:2px;
  color:var(--line);
}
h2{
  font-family:'DM Serif Display',serif;
  font-size:clamp(32px,3.5vw,50px);
  font-weight:400;line-height:1.1;
  letter-spacing:-0.5px;
}
h2 em{font-style:italic;color:var(--red);}
.s-sub{color:var(--muted);font-size:15px;font-weight:300;line-height:1.8;max-width:420px;}

.about-row{display:grid;grid-template-columns:repeat(3,1fr);gap:0;border:1px solid var(--line);border-radius:12px;overflow:hidden;}
.a-card{
  padding:40px 32px;border-right:1px solid var(--line);
  transition:background .2s;
}
.a-card:last-child{border-right:none;}
.a-card:hover{background:var(--bg);}
.a-tag{
  display:inline-block;
  font-size:10px;font-weight:700;letter-spacing:2px;text-transform:uppercase;
  color:var(--red);border:1px solid rgba(230,51,41,0.2);
  padding:3px 10px;border-radius:4px;margin-bottom:20px;
}
.a-card h3{font-family:'DM Serif Display',serif;font-size:20px;font-weight:400;margin-bottom:12px;}
.a-card p{color:var(--muted);font-size:14px;line-height:1.75;}

/* ── HOW IT WORKS ── */
#how{padding:100px 48px;background:var(--bg);}
.how-row{
  display:grid;grid-template-columns:repeat(5,1fr);
  gap:0;margin-top:48px;
  border:1px solid var(--line);border-radius:12px;overflow:hidden;
  background:var(--white);
}
.how-card{
  padding:36px 24px;border-right:1px solid var(--line);
  transition:background .2s;position:relative;
}
.how-card:last-child{border-right:none;}
.how-card:hover{background:var(--ink);}
.how-card:hover .hc-num,.how-card:hover .hc-tech,
.how-card:hover h3,.how-card:hover p{color:#fff!important;border-color:rgba(255,255,255,0.15)!important;background:transparent!important;}
.hc-num{
  font-family:'Bebas Neue',sans-serif;
  font-size:48px;line-height:1;color:var(--line);
  display:block;margin-bottom:20px;
}
.hc-tech{
  display:inline-block;font-size:10px;font-weight:700;
  letter-spacing:1.5px;text-transform:uppercase;
  color:var(--blue);border:1px solid rgba(26,60,255,0.2);
  padding:3px 8px;border-radius:4px;margin-bottom:14px;
}
.how-card h3{font-size:14px;font-weight:700;margin-bottom:8px;letter-spacing:-0.2px;}
.how-card p{color:var(--muted);font-size:12px;line-height:1.7;}

/* ── DEMO ── */
#demo{padding:100px 48px;background:var(--ink);}
#demo .s-num{color:rgba(255,255,255,0.06);}
#demo h2{color:#fff;}
#demo h2 em{color:var(--lime);}
#demo .s-sub{color:rgba(255,255,255,0.35);}
#demo .s-header{border-bottom-color:rgba(255,255,255,0.06);}

.demo-wrap{display:grid;grid-template-columns:1fr 340px;gap:24px;align-items:start;}
.cam-box{
  background:#0d0d0b;border:1px solid rgba(255,255,255,0.08);
  border-radius:12px;overflow:hidden;aspect-ratio:4/3;position:relative;
}
.cam-ph{
  position:absolute;inset:0;
  display:flex;flex-direction:column;
  align-items:center;justify-content:center;gap:14px;
}
.cam-ph p{color:rgba(255,255,255,0.3);font-size:14px;}
.cam-foot{display:flex;align-items:center;justify-content:space-between;margin-top:10px;}
.s-row{display:flex;align-items:center;gap:7px;font-size:13px;color:rgba(255,255,255,0.3);}
.dot{width:7px;height:7px;border-radius:50%;background:#333;}
.dot.on{background:var(--lime);animation:pulse 1.5s infinite;}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.4}}
.stop-btn{
  font-size:12px;font-weight:700;letter-spacing:1px;text-transform:uppercase;
  color:#f87171;background:rgba(248,113,113,.08);
  border:1px solid rgba(248,113,113,.15);
  padding:7px 16px;border-radius:4px;cursor:pointer;
  font-family:'DM Sans',sans-serif;transition:.2s;
}

.d-panel{display:flex;flex-direction:column;gap:10px;}
.d-block{
  background:rgba(255,255,255,0.04);
  border:1px solid rgba(255,255,255,0.08);
  border-radius:10px;padding:18px 20px;
}
.d-label{
  font-size:10px;font-weight:700;text-transform:uppercase;
  letter-spacing:2px;color:rgba(255,255,255,0.25);margin-bottom:12px;
}
.mode-row{display:flex;gap:8px;}
.mode-btn{
  flex:1;padding:10px 8px;border-radius:4px;
  border:1px solid rgba(255,255,255,0.1);background:transparent;
  color:rgba(255,255,255,0.35);font-size:12px;font-weight:700;
  letter-spacing:0.5px;text-transform:uppercase;
  cursor:pointer;font-family:'DM Sans',sans-serif;transition:.2s;
}
.mode-btn:hover{border-color:rgba(255,255,255,.2);color:rgba(255,255,255,.7);}
.mode-btn.active{background:var(--lime);border-color:var(--lime);color:var(--ink);}
.big-l{
  font-family:'Bebas Neue',sans-serif;
  font-size:80px;line-height:1;letter-spacing:2px;color:var(--lime);
}
.c-track{height:3px;background:rgba(255,255,255,.06);border-radius:2px;overflow:hidden;}
.c-fill{height:100%;background:var(--lime);border-radius:2px;width:0%;transition:width .3s;}
.word-d{
  font-family:'Bebas Neue',sans-serif;
  font-size:32px;letter-spacing:2px;color:#fff;
  min-height:40px;word-break:break-all;margin-bottom:12px;
}
.w-btns{display:flex;gap:8px;}
.w-btn{
  flex:1;padding:10px 8px;
  border:1px solid rgba(255,255,255,0.1);border-radius:4px;
  background:transparent;color:rgba(255,255,255,0.4);
  font-size:11px;font-weight:700;letter-spacing:1px;text-transform:uppercase;
  cursor:pointer;font-family:'DM Sans',sans-serif;transition:.2s;
}
.w-btn:hover{border-color:rgba(255,255,255,.2);color:#fff;}
.w-btn.green{background:var(--lime);border-color:var(--lime);color:var(--ink);}
.w-btn.green:hover{background:var(--lime-d);}
.a-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(32px,1fr));gap:4px;}
.alpha-key{
  background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.08);
  border-radius:5px;padding:6px 4px;text-align:center;
  font-size:12px;font-weight:700;color:rgba(255,255,255,.25);transition:.15s;
}
.alpha-key.lit{background:var(--lime);border-color:var(--lime);color:var(--ink);transform:scale(1.1);}
.b-pill{
  display:inline-block;font-size:11px;font-weight:600;
  padding:3px 12px;border-radius:4px;
  background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.08);
  color:rgba(255,255,255,.3);margin-top:8px;
}
.b-pill.ok{background:rgba(184,245,90,.08);border-color:rgba(184,245,90,.2);color:var(--lime);}
.b-pill.err{background:rgba(248,113,113,.06);border-color:rgba(248,113,113,.15);color:#f87171;}

/* ── TEAM ── */
#team{padding:100px 48px;background:var(--white);}
.team-g{
  display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));
  gap:0;margin-top:48px;
  border:1px solid var(--line);border-radius:12px;overflow:hidden;
}
.t-card{
  padding:36px 28px;text-align:center;
  border-right:1px solid var(--line);transition:background .2s;
}
.t-card:last-child{border-right:none;}
.t-card:hover{background:var(--bg);}
.t-avatar{
  width:56px;height:56px;border-radius:12px;
  display:flex;align-items:center;justify-content:center;
  font-family:'Bebas Neue',sans-serif;
  font-size:22px;margin:0 auto 14px;
}
.t-card h3{font-size:15px;font-weight:700;margin-bottom:4px;letter-spacing:-0.3px;}
.t-role{font-size:12px;color:var(--muted);text-transform:uppercase;letter-spacing:1px;}
.t-contrib{font-size:12px;margin-top:8px;font-weight:600;}

/* ── FOOTER ── */
footer{
  background:var(--ink);padding:60px 48px;
  border-top:4px solid var(--lime);
}
.foot-inner{
  max-width:1160px;margin:0 auto;
  display:flex;align-items:center;justify-content:space-between;
  flex-wrap:wrap;gap:24px;
}
.foot-logo{
  font-family:'Bebas Neue',sans-serif;
  font-size:28px;letter-spacing:3px;color:var(--lime);
}
.foot-mid p{font-size:13px;color:rgba(255,255,255,.35);margin-bottom:4px;}
.foot-mid .foot-sub{font-size:12px;color:rgba(255,255,255,.15);}
.foot-tech{display:flex;flex-wrap:wrap;gap:8px;}
.foot-tech span{
  font-size:10px;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;
  background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.08);
  color:rgba(255,255,255,.25);padding:5px 12px;border-radius:4px;
}

/* ── RESPONSIVE ── */
@media(max-width:900px){
  nav{padding:0 24px;}
  .nav-links{display:none;}
  #hero{grid-template-columns:1fr;}
  .hero-r{display:none;}
  .hero-l{padding:100px 24px 60px;}
  #about,#how,#demo,#team{padding:60px 24px;}
  .s-header{grid-template-columns:1fr;}
  .about-row,.how-row{grid-template-columns:1fr;}
  .a-card,.how-card{border-right:none;border-bottom:1px solid var(--line);}
  .demo-wrap{grid-template-columns:1fr;}
  .team-g{grid-template-columns:1fr 1fr;}
  .t-card{border-right:none;border-bottom:1px solid var(--line);}
  .foot-inner{flex-direction:column;text-align:center;}
  footer{padding:48px 24px;}
}

# Orange ......

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>SignBridge — Sign Language Recognition</title>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,wght@0,700;0,800;0,900;1,700;1,800&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css">
</head>
<body>

<nav>
  <div class="nav-logo">
    <div class="nav-icon">✋</div>
    SignBridge
  </div>
  <div class="nav-links">
    <a href="#about">About</a>
    <a href="#how">How it works</a>
    <a href="#demo">Live demo</a>
    <a href="#team">Team</a>
  </div>
</nav>

<!-- HERO — split layout -->
<section id="hero">
  <!-- Left side -->
  <div class="hero-l">
    <div class="hero-tag"><span class="tag-dot"></span> B.Tech Project — ML &amp; DL</div>
    <h1>Breaking<br>the <em>barrier</em><br>of silence</h1>
    <p class="hero-desc">Real-time sign language recognition using computer vision and deep learning — bridging communication between deaf, mute, and blind individuals.</p>
    <div class="hero-btns">
      <a href="#demo" class="btn-primary">Try live demo</a>
      <a href="#how"  class="btn-secondary">How it works ↓</a>
    </div>
    <div class="hero-chips">
      <span>OpenCV</span><span>MediaPipe</span><span>TensorFlow</span><span>Flask</span><span>pyttsx3</span>
    </div>
  </div>

  <!-- Right side — sunset orange -->
  <div class="hero-r">
    <div class="sun-circle"></div>
    <div class="sun-circle"></div>
    <div class="sun-circle"></div>
    <div class="hero-r-content">
      <span class="hero-emoji">🤟</span>
      <div class="hero-stats-box">
        <div class="h-stats">
          <div>
            <span class="h-stat-n">26+</span>
            <span class="h-stat-l">Gestures</span>
          </div>
          <div class="h-stat-div"></div>
          <div>
            <span class="h-stat-n">96%</span>
            <span class="h-stat-l">Accuracy</span>
          </div>
          <div class="h-stat-div"></div>
          <div>
            <span class="h-stat-n">21</span>
            <span class="h-stat-l">Landmarks</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ABOUT -->
<section id="about" class="section" style="background:var(--white);">
  <div class="section-inner">
    <div class="s-label">About</div>
    <h2>Who does this <em>help?</em></h2>
    <div class="cards-3">
      <div class="g-card">
        <div class="g-num">01</div>
        <div class="g-icon">🤟</div>
        <h3>Deaf &amp; mute users</h3>
        <p>Show a hand gesture to the camera. MediaPipe detects your landmarks, the CNN model recognizes the sign, and pyttsx3 speaks it out instantly.</p>
      </div>
      <div class="g-card">
        <div class="g-num">02</div>
        <div class="g-icon">🎙️</div>
        <h3>Blind users</h3>
        <p>Speak naturally into the microphone. SpeechRecognition converts your voice to text on screen in real-time for others to read clearly.</p>
      </div>
      <div class="g-card">
        <div class="g-num">03</div>
        <div class="g-icon">🔁</div>
        <h3>Two-way communication</h3>
        <p>Switch between sign-to-voice and voice-to-text with one tap — enabling complete two-way conversations for everyone.</p>
      </div>
    </div>
  </div>
</section>

<!-- HOW IT WORKS -->
<section id="how" class="section bg-soft">
  <div class="section-inner">
    <div class="s-label">Technology</div>
    <h2>How it <em>works</em></h2>
    <p class="s-sub">Five modules working together — gesture to speech in under 100ms.</p>
    <div class="steps-row">
      <div class="step-item">
        <div class="step-dot">01</div>
        <div class="step-tech">OpenCV</div>
        <h3>Camera capture</h3>
        <p>Opens webcam at 30fps and passes each frame to MediaPipe for analysis.</p>
      </div>
      <div class="step-item">
        <div class="step-dot">02</div>
        <div class="step-tech">MediaPipe</div>
        <h3>Hand detection</h3>
        <p>Maps 21 landmark points per hand as x, y, z coordinates.</p>
      </div>
      <div class="step-item">
        <div class="step-dot">03</div>
        <div class="step-tech">TensorFlow</div>
        <h3>Recognition</h3>
        <p>CNN identifies the gesture from 63 coordinates with confidence score.</p>
      </div>
      <div class="step-item">
        <div class="step-dot">04</div>
        <div class="step-tech">pyttsx3</div>
        <h3>Speech output</h3>
        <p>Converts predicted text to natural voice output instantly.</p>
      </div>
      <div class="step-item">
        <div class="step-dot">05</div>
        <div class="step-tech">SpeechRecog</div>
        <h3>Voice to text</h3>
        <p>Mic input transcribed in real-time for blind users.</p>
      </div>
    </div>
  </div>
</section>

<!-- LIVE DEMO -->
<section id="demo" class="section" style="background:var(--white);">
  <div class="section-inner">
    <div class="s-label">Interactive demo</div>
    <h2>Try it <em>live</em></h2>
    <p class="s-sub">
      Start the camera, show your hand — predictions happen in real-time.<br>
      <span id="backend-status" class="b-pill">Checking backend...</span>
    </p>
    <div class="demo-layout">
      <div>
        <div class="cam-box">
          <img id="cam-feed" style="width:100%;height:100%;object-fit:cover;display:none;border-radius:18px;" alt="feed">
          <div id="cam-placeholder" class="cam-ph">
            <div style="font-size:52px">📷</div>
            <p>Camera not started</p>
            <button class="btn-primary" id="start-btn" onclick="startCamera()">Start camera</button>
          </div>
        </div>
        <div class="cam-foot">
          <div class="s-row"><div class="dot" id="status-dot"></div><span id="status-text">No hand detected</span></div>
          <button class="stop-btn" id="stop-btn" onclick="stopCamera()" style="display:none">Stop</button>
        </div>
      </div>
      <div class="d-panel">
        <div class="d-block">
          <div class="d-label">Mode</div>
          <div class="mode-row">
            <button class="mode-btn active" id="mode-sign"  onclick="setMode('sign')">✋ Sign → Voice</button>
            <button class="mode-btn"        id="mode-voice" onclick="setMode('voice')">🎙 Voice → Text</button>
          </div>
        </div>
        <div class="d-block">
          <div class="d-label">Detected gesture</div>
          <div style="display:flex;align-items:center;gap:16px">
            <div id="big-letter" class="big-l">—</div>
            <div style="flex:1">
              <div class="c-track"><div id="conf-fill" class="c-fill"></div></div>
              <div id="conf-text" style="font-size:12px;color:var(--muted);margin-top:5px">—</div>
            </div>
          </div>
        </div>
        <div class="d-block">
          <div class="d-label">Word builder</div>
          <div id="word-display" class="word-d">—</div>
          <div class="w-btns">
            <button class="w-btn" onclick="addLetter()">Add</button>
            <button class="w-btn" onclick="clearWord()">Clear</button>
            <button class="w-btn green" onclick="speakWord()">🔊 Speak</button>
          </div>
        </div>
        <div class="d-block">
          <div class="d-label">ASL reference</div>
          <div class="a-grid" id="alpha-grid"></div>
        </div>
      </div>
    </div>
    <div id="voice-panel" style="display:none;margin-top:24px">
      <div class="d-block" style="max-width:540px">
        <div class="d-label">Voice to text — blind user mode</div>
        <div id="voice-output" style="font-size:18px;min-height:46px;color:var(--text);padding:8px 0">Speak into your microphone...</div>
        <button class="btn-primary" id="voice-btn" onclick="toggleVoice()" style="margin-top:14px">🎙 Start listening</button>
      </div>
    </div>
  </div>
</section>

<!-- TEAM -->
<section id="team" class="section bg-soft">
  <div class="section-inner">
    <div class="s-label">Our team</div>
    <h2>The <em>builders</em></h2>
    <p class="s-sub">B.Tech students making communication accessible for everyone.</p>
    <div class="team-g" id="team-grid"></div>
  </div>
</section>

<footer>
  <div class="foot-inner">
    <div class="foot-logo">✋ SignBridge</div>
    <p>Enhancing Accessibility using Sign Language Recognition with ML &amp; DL</p>
    <p class="foot-sub">B.Tech · Academic Project</p>
    <div class="foot-tech">
      <span>Python</span><span>OpenCV</span><span>MediaPipe</span><span>TensorFlow</span><span>Flask</span><span>pyttsx3</span>
    </div>
  </div>
</footer>

<script src="script.js"></script>
<script>
const team = [
  {name:"Member 1",role:"ML Engineer",       contrib:"CNN model & training",  color:"#ff6b35",bg:"#fff0ea"},
  {name:"Member 2",role:"Computer Vision",   contrib:"MediaPipe integration", color:"#e05c00",bg:"#fff3e6"},
  {name:"Member 3",role:"Backend Developer", contrib:"Flask API & Python",    color:"#ff8c00",bg:"#fff8e6"},
  {name:"Member 4",role:"Frontend Developer",contrib:"UI & website",          color:"#cc4400",bg:"#fff0e8"},
  {name:"Member 5",role:"Data Engineer",     contrib:"Dataset & collection",  color:"#ff6b35",bg:"#fff0ea"},
];
const grid = document.getElementById("team-grid");
team.forEach(m => {
  const initials = m.name.split(" ").map(w=>w[0]).join("");
  grid.innerHTML += `
    <div class="t-card">
      <div class="t-avatar" style="background:${m.bg};color:${m.color}">${initials}</div>
      <h3>${m.name}</h3>
      <div class="t-role">${m.role}</div>
      <div class="t-contrib" style="color:${m.color}">${m.contrib}</div>
    </div>`;
});
</script>
</body>
</html>

#CSS

@import url('https://fonts.googleapis.com/css2?family=Fraunces:ital,wght@0,700;0,800;0,900;1,700;1,900&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');

:root {
  --bg:      #fff8f0;
  --bg2:     #fff3e8;
  --bg3:     #ffeedd;
  --white:   #ffffff;
  --ink:     #1a1205;
  --ink2:    #3d2e1a;
  --muted:   #9a8060;
  --border:  #f0dcc8;
  --border2: #e0c8a8;
  --orange:  #ff6b35;
  --orange2: #ff8c5a;
  --amber:   #ffb347;
  --deep:    #c94a1a;
  --light:   #fff0e4;
}

*{margin:0;padding:0;box-sizing:border-box;}
html{scroll-behavior:smooth;}

body{
  background:var(--bg);
  color:var(--ink);
  font-family:'Plus Jakarta Sans',sans-serif;
  font-size:16px;line-height:1.7;
  overflow-x:hidden;
}

/* subtle warm texture */
body::before{
  content:'';
  position:fixed;inset:0;z-index:0;pointer-events:none;
  background:
    radial-gradient(ellipse 70% 50% at 100% 0%,   rgba(255,107,53,0.06) 0%,transparent 60%),
    radial-gradient(ellipse 50% 40% at 0%   100%, rgba(255,179,71,0.05) 0%,transparent 60%);
}

nav,section,footer{position:relative;z-index:1;}

/* ── NAV ── */
nav{
  position:fixed;top:0;left:0;right:0;z-index:100;
  display:flex;align-items:center;justify-content:space-between;
  padding:0 64px;height:68px;
  background:rgba(255,248,240,0.92);
  backdrop-filter:blur(20px);
  border-bottom:1px solid var(--border);
}
.nav-logo{
  font-family:'Plus Jakarta Sans',sans-serif;
  font-size:18px;font-weight:800;color:var(--ink);
  letter-spacing:-0.5px;display:flex;align-items:center;gap:8px;
}
.nav-icon{
  width:32px;height:32px;border-radius:10px;
  background:var(--orange);
  display:flex;align-items:center;justify-content:center;
  font-size:16px;
}
.nav-links{display:flex;gap:36px;}
.nav-links a{
  color:var(--muted);text-decoration:none;
  font-size:14px;font-weight:500;transition:color .2s;
}
.nav-links a:hover{color:var(--orange);}

/* ── HERO ── */
#hero{
  min-height:100vh;
  display:grid;grid-template-columns:1fr 1fr;
  overflow:hidden;
}

.hero-l{
  display:flex;flex-direction:column;justify-content:center;
  padding:120px 64px 80px;
  border-right:1px solid var(--border);
}
.hero-r{
  display:flex;align-items:center;justify-content:center;
  padding:120px 60px 80px;
  background:var(--orange);
  position:relative;overflow:hidden;
}

/* sun rays on right */
.hero-r::before{
  content:'';position:absolute;
  width:600px;height:600px;border-radius:50%;
  background:rgba(255,255,255,0.08);
  top:50%;left:50%;transform:translate(-50%,-50%);
}
.hero-r::after{
  content:'';position:absolute;
  width:400px;height:400px;border-radius:50%;
  background:rgba(255,255,255,0.08);
  top:50%;left:50%;transform:translate(-50%,-50%);
}

.hero-tag{
  display:inline-flex;align-items:center;gap:8px;
  font-size:11px;font-weight:700;letter-spacing:1.5px;
  text-transform:uppercase;color:var(--orange);
  margin-bottom:28px;
  animation:fadeUp .5s ease both;
}
.tag-line{width:24px;height:2px;background:var(--orange);border-radius:2px;}

h1{
  font-family:'Fraunces',serif;
  font-size:clamp(44px,5vw,72px);
  font-weight:900;line-height:1.0;
  letter-spacing:-2px;margin-bottom:24px;
  animation:fadeUp .5s .1s ease both;
  color:var(--ink);
}
h1 em{
  font-style:italic;
  color:var(--orange);
}

.hero-desc{
  color:var(--muted);font-size:17px;font-weight:300;
  max-width:440px;margin-bottom:40px;line-height:1.8;
  animation:fadeUp .5s .2s ease both;
}
.hero-btns{
  display:flex;gap:12px;margin-bottom:48px;
  animation:fadeUp .5s .3s ease both;
}

/* buttons */
.btn-primary{
  background:var(--ink);color:#fff;
  padding:14px 32px;border-radius:100px;
  font-size:14px;font-weight:700;
  text-decoration:none;border:none;cursor:pointer;
  font-family:'Plus Jakarta Sans',sans-serif;
  transition:background .2s,transform .2s;display:inline-block;
}
.btn-primary:hover{background:var(--orange);transform:translateY(-2px);}

.btn-secondary{
  background:transparent;color:var(--ink);
  padding:14px 32px;border-radius:100px;
  font-size:14px;font-weight:500;
  text-decoration:none;border:1.5px solid var(--border2);
  cursor:pointer;font-family:'Plus Jakarta Sans',sans-serif;
  transition:.2s;display:inline-block;
}
.btn-secondary:hover{border-color:var(--orange);color:var(--orange);}

.hero-chips{display:flex;gap:8px;flex-wrap:wrap;animation:fadeUp .5s .4s ease both;}
.hero-chip{
  font-size:12px;font-weight:600;
  background:var(--white);border:1.5px solid var(--border);
  color:var(--muted);padding:5px 14px;border-radius:100px;
  transition:.2s;
}
.hero-chip:hover{border-color:var(--orange);color:var(--orange);}

/* right side content */
.hero-r-content{position:relative;z-index:1;text-align:center;}
.hero-hand{font-size:72px;display:block;margin-bottom:32px;animation:float 3s ease-in-out infinite;}
@keyframes float{0%,100%{transform:translateY(0)}50%{transform:translateY(-12px)}}

.hero-stats-v{display:flex;flex-direction:column;gap:0;width:220px;margin:0 auto;}
.hstat-h{
  padding:18px 24px;
  border:1px solid rgba(255,255,255,0.25);
  border-bottom:none;background:rgba(255,255,255,0.12);
  transition:background .2s;
}
.hstat-h:first-child{border-radius:16px 16px 0 0;}
.hstat-h:last-child{border-bottom:1px solid rgba(255,255,255,0.25);border-radius:0 0 16px 16px;}
.hstat-h:hover{background:rgba(255,255,255,0.2);}
.hstat-h-num{
  font-family:'Fraunces',serif;
  font-size:28px;font-weight:900;color:#fff;
  display:block;line-height:1;
}
.hstat-h-label{font-size:11px;color:rgba(255,255,255,0.6);margin-top:4px;display:block;letter-spacing:0.5px;}

@keyframes fadeUp{from{opacity:0;transform:translateY(20px)}to{opacity:1;transform:translateY(0)}}

/* ── SECTIONS ── */
.section{padding:100px 64px;}
.section-inner{max-width:1160px;margin:0 auto;}
.bg-soft{background:var(--bg2);}

.s-label{
  font-size:11px;font-weight:700;letter-spacing:2.5px;
  text-transform:uppercase;color:var(--orange);margin-bottom:14px;
}
h2{
  font-family:'Fraunces',serif;
  font-size:clamp(28px,3.5vw,48px);
  font-weight:900;letter-spacing:-1.5px;
  line-height:1.05;margin-bottom:16px;color:var(--ink);
}
h2 em{font-style:italic;color:var(--orange);}
.s-sub{color:var(--muted);font-size:16px;font-weight:300;max-width:480px;margin-bottom:52px;}

/* ── ABOUT ── */
.cards-3{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin-top:48px;}
.g-card{
  background:var(--white);border:1.5px solid var(--border);
  border-radius:20px;padding:36px 28px;
  transition:border-color .2s,transform .2s,box-shadow .2s;
}
.g-card:hover{
  border-color:var(--orange);transform:translateY(-4px);
  box-shadow:0 12px 40px rgba(255,107,53,0.1);
}
.g-icon{font-size:32px;margin-bottom:18px;}
.g-card h3{font-size:17px;font-weight:700;margin-bottom:10px;color:var(--ink);}
.g-card p{color:var(--muted);font-size:14px;line-height:1.75;}

/* ── HOW IT WORKS ── */
.steps-row{
  display:grid;grid-template-columns:repeat(5,1fr);
  gap:0;margin-top:48px;
  border:1.5px solid var(--border);border-radius:20px;overflow:hidden;
}
.step-item{
  background:var(--white);padding:32px 24px;
  border-right:1.5px solid var(--border);
  transition:background .2s;
}
.step-item:last-child{border-right:none;}
.step-item:hover{background:var(--light);}
.step-num{
  font-family:'Fraunces',serif;
  font-size:28px;font-weight:900;color:var(--border2);
  margin-bottom:12px;line-height:1;
}
.step-tech{
  display:inline-block;font-size:10px;font-weight:700;
  background:rgba(255,107,53,.08);color:var(--orange);
  border:1px solid rgba(255,107,53,.2);
  padding:2px 10px;border-radius:6px;margin-bottom:12px;
}
.step-item h3{font-size:14px;font-weight:700;margin-bottom:8px;color:var(--ink);}
.step-item p{color:var(--muted);font-size:12px;line-height:1.7;}

/* ── DEMO ── */
.demo-layout{display:grid;grid-template-columns:1fr 340px;gap:24px;align-items:start;}
.cam-box{
  background:var(--bg3);border:1.5px solid var(--border);
  border-radius:20px;overflow:hidden;aspect-ratio:4/3;position:relative;
}
.cam-ph{
  position:absolute;inset:0;
  display:flex;flex-direction:column;
  align-items:center;justify-content:center;gap:14px;
}
.cam-ph p{color:var(--muted);font-size:14px;}
.cam-foot{display:flex;align-items:center;justify-content:space-between;margin-top:10px;}
.s-row{display:flex;align-items:center;gap:7px;font-size:13px;color:var(--muted);}
.dot{width:7px;height:7px;border-radius:50%;background:#ddd;}
.dot.on{background:var(--orange);animation:pulse 1.5s infinite;}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.4}}
.stop-btn{
  font-size:12px;font-weight:700;color:var(--deep);
  background:rgba(201,74,26,.06);border:1.5px solid rgba(201,74,26,.15);
  padding:7px 16px;border-radius:100px;cursor:pointer;
  font-family:'Plus Jakarta Sans',sans-serif;transition:.2s;
}
.stop-btn:hover{background:rgba(201,74,26,.1);}

.d-panel{display:flex;flex-direction:column;gap:12px;}
.d-block{
  background:var(--white);border:1.5px solid var(--border);
  border-radius:16px;padding:20px 22px;
}
.d-label{
  font-size:10px;font-weight:700;text-transform:uppercase;
  letter-spacing:2px;color:var(--muted);margin-bottom:12px;
}
.mode-row{display:flex;gap:8px;}
.mode-btn{
  flex:1;padding:10px 8px;border-radius:100px;
  border:1.5px solid var(--border);background:transparent;
  color:var(--muted);font-size:12px;font-weight:600;
  cursor:pointer;font-family:'Plus Jakarta Sans',sans-serif;transition:.2s;
}
.mode-btn:hover{border-color:var(--orange);color:var(--orange);}
.mode-btn.active{background:var(--orange);border-color:var(--orange);color:#fff;}

.big-l{
  font-family:'Fraunces',serif;
  font-size:76px;font-weight:900;color:var(--orange);
  line-height:1;letter-spacing:-3px;
}
.c-track{height:4px;background:var(--bg3);border-radius:2px;overflow:hidden;}
.c-fill{height:100%;background:var(--orange);border-radius:2px;width:0%;transition:width .3s;}
.word-d{
  font-family:'Fraunces',serif;
  font-size:26px;font-weight:900;color:var(--ink);
  min-height:36px;word-break:break-all;margin-bottom:14px;
  letter-spacing:-1px;
}
.w-btns{display:flex;gap:8px;}
.w-btn{
  flex:1;padding:10px 8px;border:1.5px solid var(--border);
  border-radius:100px;background:transparent;color:var(--muted);
  font-size:12px;font-weight:600;cursor:pointer;
  font-family:'Plus Jakarta Sans',sans-serif;transition:.2s;
}
.w-btn:hover{border-color:var(--orange);color:var(--orange);}
.w-btn.green{background:var(--orange);border-color:var(--orange);color:#fff;}
.w-btn.green:hover{background:var(--deep);border-color:var(--deep);}

.a-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(34px,1fr));gap:5px;}
.alpha-key{
  background:var(--bg);border:1.5px solid var(--border);
  border-radius:8px;padding:6px 4px;text-align:center;
  font-size:12px;font-weight:700;color:var(--muted);transition:.15s;
}
.alpha-key.lit{background:var(--orange);border-color:var(--orange);color:#fff;transform:scale(1.08);}

.b-pill{
  display:inline-block;font-size:11px;font-weight:600;
  padding:3px 12px;border-radius:100px;
  background:var(--bg2);border:1.5px solid var(--border);
  color:var(--muted);margin-top:8px;
}
.b-pill.ok{background:rgba(255,107,53,.08);border-color:rgba(255,107,53,.25);color:var(--orange);}
.b-pill.err{background:rgba(201,74,26,.06);border-color:rgba(201,74,26,.2);color:var(--deep);}

/* ── TEAM ── */
.team-g{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:18px;margin-top:48px;}
.t-card{
  background:var(--white);border:1.5px solid var(--border);
  border-radius:20px;padding:28px 22px;text-align:center;
  transition:border-color .2s,transform .2s,box-shadow .2s;
}
.t-card:hover{
  border-color:var(--orange);transform:translateY(-4px);
  box-shadow:0 12px 32px rgba(255,107,53,0.1);
}
.t-avatar{
  width:60px;height:60px;border-radius:16px;
  display:flex;align-items:center;justify-content:center;
  font-family:'Fraunces',serif;
  font-size:22px;font-weight:900;margin:0 auto 14px;
}
.t-card h3{font-size:15px;font-weight:700;margin-bottom:4px;color:var(--ink);}
.t-role{font-size:13px;color:var(--muted);}
.t-contrib{font-size:12px;margin-top:8px;font-weight:700;}

/* ── FOOTER ── */
footer{
  background:var(--ink);
  padding:60px 64px;text-align:center;
}
.foot-inner{max-width:600px;margin:0 auto;}
.foot-logo{
  font-family:'Fraunces',serif;
  font-size:24px;font-weight:900;color:var(--orange);
  margin-bottom:14px;letter-spacing:-0.5px;
}
footer p{font-size:14px;color:rgba(255,255,255,.4);margin-bottom:6px;}
.foot-sub{font-size:12px;color:rgba(255,255,255,.2)!important;}
.foot-tech{display:flex;flex-wrap:wrap;gap:8px;justify-content:center;margin-top:24px;}
.foot-tech span{
  font-size:11px;font-weight:600;
  background:rgba(255,107,53,.1);
  border:1px solid rgba(255,107,53,.2);
  color:var(--orange2);padding:4px 12px;border-radius:100px;
}

@media(max-width:900px){
  nav{padding:0 24px;}
  .nav-links{display:none;}
  .section,.bg-soft{padding:60px 24px;}
  #hero{grid-template-columns:1fr;}
  .hero-r{display:none;}
  .hero-l{padding:100px 24px 60px;}
  .cards-3{grid-template-columns:1fr;}
  .steps-row{grid-template-columns:1fr;}
  .step-item{border-right:none;border-bottom:1.5px solid var(--border);}
  .demo-layout{grid-template-columns:1fr;}
  footer{padding:48px 24px;}
}

# orange peach cream

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>SignBridge — Sign Language Recognition</title>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;1,400;1,600&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css">
</head>
<body>

<canvas id="particles"></canvas>

<nav>
  <div class="nav-logo">✋ SignBridge</div>
  <div class="nav-links">
    <a href="#about">About</a>
    <a href="#how">How it works</a>
    <a href="#demo">Live demo</a>
    <a href="#team">Team</a>
  </div>
</nav>

<section id="hero">
  <div class="hero-ring"></div>
  <div class="hero-ring"></div>
  <div class="hero-ring"></div>
  <div class="hero-tag"><span class="tag-dot"></span> B.Tech Project — ML &amp; DL</div>
  <h1>Sign language meets<br><span class="h1-g">intelligence</span></h1>
  <p class="hero-sub">Real-time gesture recognition using computer vision and deep learning — bridging communication between deaf, mute, and blind individuals.</p>
  <div class="hero-btns">
    <a href="#demo" class="btn-primary">Try live demo</a>
    <a href="#how"  class="btn-secondary">How it works ↓</a>
  </div>
  <div class="hero-stats">
    <div class="stat-card"><span class="stat-n">26+</span><span class="stat-l">Gestures</span></div>
    <div class="stat-card"><span class="stat-n">96%</span><span class="stat-l">Accuracy</span></div>
    <div class="stat-card"><span class="stat-n">21</span><span class="stat-l">Landmarks</span></div>
    <div class="stat-card"><span class="stat-n">&lt;100ms</span><span class="stat-l">Response</span></div>
  </div>
</section>

<section id="about" class="section glass-section">
  <div class="section-inner">
    <div class="s-label">About</div>
    <h2>Who does this <em>help?</em></h2>
    <div class="cards-3">
      <div class="g-card">
        <div class="g-icon">🤟</div>
        <h3>Deaf &amp; mute users</h3>
        <p>Show a hand gesture to the camera. MediaPipe detects your landmarks, the CNN model recognizes the sign, and pyttsx3 speaks it out loud instantly.</p>
      </div>
      <div class="g-card">
        <div class="g-icon">🎙️</div>
        <h3>Blind users</h3>
        <p>Speak naturally into the microphone. SpeechRecognition converts your voice to text in real-time, displayed clearly on screen for others to read.</p>
      </div>
      <div class="g-card">
        <div class="g-icon">🔁</div>
        <h3>Two-way communication</h3>
        <p>Switch between sign-to-voice and voice-to-text with one tap — enabling complete two-way conversations for everyone.</p>
      </div>
    </div>
  </div>
</section>

<section id="how" class="section">
  <div class="section-inner">
    <div class="s-label">Technology</div>
    <h2>How it <em>works</em></h2>
    <p class="s-sub">Five modules working together — from gesture to spoken word in under 100ms.</p>
    <div class="steps-row">
      <div class="step-item">
        <div class="step-num">01</div>
        <div class="step-tech">OpenCV</div>
        <h3>Camera capture</h3>
        <p>Opens webcam at 30fps and passes each frame to MediaPipe for hand detection.</p>
      </div>
      <div class="step-item">
        <div class="step-num">02</div>
        <div class="step-tech">MediaPipe</div>
        <h3>Hand detection</h3>
        <p>Maps 21 landmark points per hand as precise x, y, z coordinates.</p>
      </div>
      <div class="step-item">
        <div class="step-num">03</div>
        <div class="step-tech">TensorFlow</div>
        <h3>Recognition</h3>
        <p>CNN model identifies the gesture from 63 coordinates with confidence score.</p>
      </div>
      <div class="step-item">
        <div class="step-num">04</div>
        <div class="step-tech">pyttsx3</div>
        <h3>Speech output</h3>
        <p>Converts predicted text to natural voice output instantly.</p>
      </div>
      <div class="step-item">
        <div class="step-num">05</div>
        <div class="step-tech">SpeechRecog</div>
        <h3>Voice to text</h3>
        <p>Mic input transcribed in real-time and shown on screen for blind users.</p>
      </div>
    </div>
  </div>
</section>

<section id="demo" class="section glass-section">
  <div class="section-inner">
    <div class="s-label">Interactive demo</div>
    <h2>Try it <em>live</em></h2>
    <p class="s-sub">
      Start the camera, show your hand — predictions in real-time.<br>
      <span id="backend-status" class="b-pill">Checking backend...</span>
    </p>
    <div class="demo-layout">
      <div>
        <div class="cam-box">
          <img id="cam-feed" style="width:100%;height:100%;object-fit:cover;display:none;border-radius:18px;" alt="feed">
          <div id="cam-placeholder" class="cam-ph">
            <div style="font-size:52px">📷</div>
            <p>Camera not started</p>
            <button class="btn-primary" id="start-btn" onclick="startCamera()">Start camera</button>
          </div>
        </div>
        <div class="cam-foot">
          <div class="s-row"><div class="dot" id="status-dot"></div><span id="status-text">No hand detected</span></div>
          <button class="stop-btn" id="stop-btn" onclick="stopCamera()" style="display:none">Stop</button>
        </div>
      </div>
      <div class="d-panel">
        <div class="d-block">
          <div class="d-label">Mode</div>
          <div class="mode-row">
            <button class="mode-btn active" id="mode-sign"  onclick="setMode('sign')">✋ Sign → Voice</button>
            <button class="mode-btn"        id="mode-voice" onclick="setMode('voice')">🎙 Voice → Text</button>
          </div>
        </div>
        <div class="d-block">
          <div class="d-label">Detected gesture</div>
          <div style="display:flex;align-items:center;gap:16px">
            <div id="big-letter" class="big-l">—</div>
            <div style="flex:1">
              <div class="c-track"><div id="conf-fill" class="c-fill"></div></div>
              <div id="conf-text" style="font-size:12px;color:var(--muted);margin-top:5px">—</div>
            </div>
          </div>
        </div>
        <div class="d-block">
          <div class="d-label">Word builder</div>
          <div id="word-display" class="word-d">—</div>
          <div class="w-btns">
            <button class="w-btn" onclick="addLetter()">Add</button>
            <button class="w-btn" onclick="clearWord()">Clear</button>
            <button class="w-btn green" onclick="speakWord()">🔊 Speak</button>
          </div>
        </div>
        <div class="d-block">
          <div class="d-label">ASL reference</div>
          <div class="a-grid" id="alpha-grid"></div>
        </div>
      </div>
    </div>
    <div id="voice-panel" style="display:none;margin-top:24px">
      <div class="d-block" style="max-width:540px">
        <div class="d-label">Voice to text — blind user mode</div>
        <div id="voice-output" style="font-size:18px;min-height:46px;color:var(--text);padding:8px 0">Speak into your microphone...</div>
        <button class="btn-primary" id="voice-btn" onclick="toggleVoice()" style="margin-top:14px">🎙 Start listening</button>
      </div>
    </div>
  </div>
</section>

<section id="team" class="section">
  <div class="section-inner">
    <div class="s-label">Our team</div>
    <h2>The <em>builders</em></h2>
    <p class="s-sub">B.Tech students making communication accessible for everyone.</p>
    <div class="team-g" id="team-grid"></div>
  </div>
</section>

<footer>
  <div class="foot-inner">
    <div class="foot-logo">✋ SignBridge</div>
    <p>Enhancing Accessibility using Sign Language Recognition with ML &amp; DL</p>
    <p class="foot-sub">B.Tech · Academic Project</p>
    <div class="foot-tech">
      <span>Python</span><span>OpenCV</span><span>MediaPipe</span><span>TensorFlow</span><span>Flask</span><span>pyttsx3</span>
    </div>
  </div>
</footer>

<script src="script.js"></script>
<script>
const canvas = document.getElementById('particles');
const ctx = canvas.getContext('2d');
let W, H, pts = [];
function resize(){ W = canvas.width = window.innerWidth; H = canvas.height = window.innerHeight; }
resize(); window.addEventListener('resize', resize);
class Dot {
  constructor(){ this.reset(); }
  reset(){
    this.x = Math.random()*W; this.y = Math.random()*H;
    this.r = Math.random()*1.5+0.3;
    this.vx = (Math.random()-.5)*.2; this.vy = (Math.random()-.5)*.2;
    this.a = Math.random()*.15+0.04;
    this.c = Math.random()>.5 ? '245,158,11' : '239,68,68';
  }
  update(){ this.x+=this.vx; this.y+=this.vy; if(this.x<0||this.x>W||this.y<0||this.y>H) this.reset(); }
  draw(){ ctx.beginPath(); ctx.arc(this.x,this.y,this.r,0,Math.PI*2); ctx.fillStyle=`rgba(${this.c},${this.a})`; ctx.fill(); }
}
for(let i=0;i<80;i++) pts.push(new Dot());
function loop(){
  ctx.clearRect(0,0,W,H);
  for(let i=0;i<pts.length;i++){
    pts[i].update(); pts[i].draw();
    for(let j=i+1;j<pts.length;j++){
      const dx=pts[i].x-pts[j].x, dy=pts[i].y-pts[j].y;
      const d=Math.sqrt(dx*dx+dy*dy);
      if(d<100){
        ctx.beginPath(); ctx.moveTo(pts[i].x,pts[i].y); ctx.lineTo(pts[j].x,pts[j].y);
        ctx.strokeStyle=`rgba(245,158,11,${0.04*(1-d/100)})`; ctx.lineWidth=0.5; ctx.stroke();
      }
    }
  }
  requestAnimationFrame(loop);
}
loop();

const team = [
  {name:"Member 1",role:"ML Engineer",       contrib:"CNN model & training",  color:"#f59e0b",bg:"rgba(245,158,11,0.08)"},
  {name:"Member 2",role:"Computer Vision",   contrib:"MediaPipe integration", color:"#ef4444",bg:"rgba(239,68,68,0.08)"},
  {name:"Member 3",role:"Backend Developer", contrib:"Flask API & Python",    color:"#f97316",bg:"rgba(249,115,22,0.08)"},
  {name:"Member 4",role:"Frontend Developer",contrib:"UI & website",          color:"#d97706",bg:"rgba(217,119,6,0.08)"},
  {name:"Member 5",role:"Data Engineer",     contrib:"Dataset & collection",  color:"#b45309",bg:"rgba(180,83,9,0.08)"},
];
const grid = document.getElementById("team-grid");
team.forEach(m => {
  const initials = m.name.split(" ").map(w=>w[0]).join("");
  grid.innerHTML += `
    <div class="t-card">
      <div class="t-avatar" style="background:${m.bg};color:${m.color}">${initials}</div>
      <h3>${m.name}</h3>
      <div class="t-role">${m.role}</div>
      <div class="t-contrib" style="color:${m.color}">${m.contrib}</div>
    </div>`;
});
</script>
</body>
</html>

# CSS

@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;1,400;1,600&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');

:root {
  --bg:      #fffbf0;
  --bg2:     #fff5e6;
  --bg3:     #fff0f5;
  --white:   #ffffff;
  --border:  #fde8d8;
  --border2: #fcd9c0;
  --text:    #1c1412;
  --muted:   #a08070;
  --amber:   #f59e0b;
  --red:     #ef4444;
  --orange:  #f97316;
  --light:   #fffdf8;
}

*{margin:0;padding:0;box-sizing:border-box;}
html{scroll-behavior:smooth;}

body{
  background:var(--bg);
  color:var(--text);
  font-family:'Plus Jakarta Sans',sans-serif;
  font-size:16px;line-height:1.7;
  overflow-x:hidden;
}

body::before{
  content:'';
  position:fixed;inset:0;z-index:0;pointer-events:none;
  background:
    radial-gradient(ellipse 70% 50% at 100% 0%,   rgba(245,158,11,0.09) 0%,transparent 60%),
    radial-gradient(ellipse 50% 50% at 0%   100%, rgba(239,68,68,0.06)  0%,transparent 60%),
    radial-gradient(ellipse 40% 40% at 50%  50%,  rgba(249,115,22,0.04) 0%,transparent 70%);
}

#particles{position:fixed;top:0;left:0;width:100%;height:100%;z-index:0;pointer-events:none;}
nav,section,footer{position:relative;z-index:1;}

/* ── NAV ── */
nav{
  position:fixed;top:0;left:0;right:0;z-index:100;
  display:flex;align-items:center;justify-content:space-between;
  padding:0 64px;height:68px;
  background:rgba(255,251,240,0.92);
  backdrop-filter:blur(20px);
  border-bottom:1px solid var(--border);
}
.nav-logo{
  font-size:18px;font-weight:700;
  background:linear-gradient(135deg,#f59e0b,#ef4444);
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;
  background-clip:text;letter-spacing:-0.3px;
}
.nav-links{display:flex;gap:36px;}
.nav-links a{
  color:var(--muted);text-decoration:none;
  font-size:14px;font-weight:400;transition:color .2s;
}
.nav-links a:hover{color:var(--orange);}

/* ── HERO ── */
#hero{
  min-height:100vh;
  display:flex;flex-direction:column;
  align-items:center;justify-content:center;
  padding:100px 64px 80px;
  text-align:center;position:relative;
}
.hero-ring{
  position:absolute;border-radius:50%;pointer-events:none;
  animation:ringPulse 4s ease-in-out infinite;
}
.hero-ring:nth-child(1){width:400px;height:400px;top:50%;left:50%;transform:translate(-50%,-50%);border:1px solid rgba(245,158,11,0.1);}
.hero-ring:nth-child(2){width:620px;height:620px;top:50%;left:50%;transform:translate(-50%,-50%);border:1px solid rgba(239,68,68,0.07);animation-delay:1.5s;}
.hero-ring:nth-child(3){width:840px;height:840px;top:50%;left:50%;transform:translate(-50%,-50%);border:1px solid rgba(249,115,22,0.05);animation-delay:3s;}
@keyframes ringPulse{0%,100%{opacity:.6}50%{opacity:.15}}

.hero-tag{
  display:inline-flex;align-items:center;gap:8px;
  font-size:11px;font-weight:600;letter-spacing:1.5px;
  text-transform:uppercase;color:var(--amber);
  background:rgba(245,158,11,0.08);
  border:1px solid rgba(245,158,11,0.25);
  padding:7px 20px;border-radius:100px;
  margin-bottom:36px;
  animation:fadeUp .6s ease both;
}
.tag-dot{width:5px;height:5px;border-radius:50%;background:var(--amber);animation:tagPulse 2s infinite;}
@keyframes tagPulse{0%,100%{opacity:1;transform:scale(1)}50%{opacity:.4;transform:scale(.8)}}

h1{
  font-family:'Cormorant Garamond',serif;
  font-size:clamp(52px,7vw,96px);
  font-weight:600;line-height:1.0;
  letter-spacing:-2px;margin-bottom:28px;
  color:var(--text);
  animation:fadeUp .6s .1s ease both;
}
h1 .h1-g{
  font-style:italic;
  background:linear-gradient(135deg,#f59e0b,#ef4444);
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;
  background-clip:text;
}

.hero-sub{
  max-width:540px;color:var(--muted);font-size:17px;
  font-weight:300;margin:0 auto 48px;line-height:1.8;
  animation:fadeUp .6s .2s ease both;
}
.hero-btns{
  display:flex;gap:14px;justify-content:center;
  margin-bottom:64px;
  animation:fadeUp .6s .3s ease both;
}
.btn-primary{
  background:linear-gradient(135deg,#f59e0b,#ef4444);
  color:#fff;padding:14px 36px;border-radius:100px;
  font-size:14px;font-weight:700;letter-spacing:0.3px;
  text-decoration:none;border:none;cursor:pointer;
  font-family:'Plus Jakarta Sans',sans-serif;
  transition:transform .2s,box-shadow .2s;display:inline-block;
  box-shadow:0 4px 20px rgba(245,158,11,0.3);
}
.btn-primary:hover{transform:translateY(-2px);box-shadow:0 12px 40px rgba(245,158,11,0.4);}
.btn-secondary{
  background:var(--white);color:var(--orange);
  padding:14px 36px;border-radius:100px;
  font-size:14px;font-weight:500;
  text-decoration:none;border:1.5px solid var(--border2);
  cursor:pointer;font-family:'Plus Jakarta Sans',sans-serif;
  transition:.2s;display:inline-block;
  box-shadow:0 2px 10px rgba(245,158,11,0.1);
}
.btn-secondary:hover{border-color:var(--amber);box-shadow:0 4px 20px rgba(245,158,11,0.15);}

.hero-stats{
  display:flex;gap:0;
  border:1.5px solid var(--border2);
  border-radius:20px;overflow:hidden;
  animation:fadeUp .6s .4s ease both;
  background:var(--white);
  box-shadow:0 4px 24px rgba(245,158,11,0.1);
}
.stat-card{
  padding:24px 40px;text-align:center;
  border-right:1px solid var(--border);
  transition:background .2s;
}
.stat-card:last-child{border-right:none;}
.stat-card:hover{background:rgba(245,158,11,0.03);}
.stat-n{
  font-family:'Cormorant Garamond',serif;
  font-size:36px;font-weight:600;
  background:linear-gradient(135deg,#f59e0b,#ef4444);
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;
  background-clip:text;display:block;line-height:1;
}
.stat-l{font-size:11px;color:var(--muted);margin-top:6px;display:block;letter-spacing:1px;text-transform:uppercase;}

@keyframes fadeUp{from{opacity:0;transform:translateY(24px)}to{opacity:1;transform:translateY(0)}}

/* ── SECTIONS ── */
.section{padding:100px 64px;}
.section-inner{max-width:1160px;margin:0 auto;}
.glass-section{
  background:rgba(255,255,255,0.7);
  border-top:1px solid var(--border);
  border-bottom:1px solid var(--border);
  backdrop-filter:blur(10px);
}
.s-label{font-size:11px;font-weight:600;letter-spacing:2.5px;text-transform:uppercase;color:var(--amber);margin-bottom:14px;}
h2{
  font-family:'Cormorant Garamond',serif;
  font-size:clamp(32px,4vw,56px);font-weight:600;
  letter-spacing:-1px;line-height:1.05;margin-bottom:16px;color:var(--text);
}
h2 em{font-style:italic;color:var(--amber);}
.s-sub{color:var(--muted);font-size:16px;font-weight:300;max-width:480px;margin-bottom:52px;line-height:1.8;}

/* ── ABOUT ── */
.cards-3{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin-top:48px;}
.g-card{
  background:var(--white);border:1.5px solid var(--border);
  border-radius:20px;padding:36px 28px;
  box-shadow:0 2px 20px rgba(245,158,11,0.07);
  transition:border-color .3s,transform .2s,box-shadow .3s;
  position:relative;overflow:hidden;
}
.g-card::before{
  content:'';position:absolute;top:0;left:0;right:0;height:2px;
  background:linear-gradient(90deg,#f59e0b,#ef4444);
  opacity:0;transition:opacity .3s;
}
.g-card:hover{border-color:rgba(245,158,11,0.3);transform:translateY(-4px);box-shadow:0 12px 40px rgba(245,158,11,0.12);}
.g-card:hover::before{opacity:1;}
.g-icon{font-size:32px;margin-bottom:18px;}
.g-card h3{font-size:17px;font-weight:600;margin-bottom:10px;color:var(--text);}
.g-card p{color:var(--muted);font-size:14px;line-height:1.75;}

/* ── HOW IT WORKS ── */
.steps-row{
  display:grid;grid-template-columns:repeat(5,1fr);
  gap:0;margin-top:48px;
  border:1.5px solid var(--border);border-radius:20px;overflow:hidden;
  box-shadow:0 2px 20px rgba(245,158,11,0.07);
}
.step-item{
  padding:32px 24px;border-right:1px solid var(--border);
  background:var(--white);transition:background .2s;
}
.step-item:last-child{border-right:none;}
.step-item:hover{background:rgba(245,158,11,0.03);}
.step-num{
  font-size:11px;font-weight:700;letter-spacing:2px;
  background:linear-gradient(135deg,#f59e0b,#ef4444);
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;
  background-clip:text;margin-bottom:14px;
}
.step-tech{
  display:inline-block;font-size:10px;font-weight:600;
  background:rgba(245,158,11,0.08);color:var(--amber);
  border:1px solid rgba(245,158,11,0.2);
  padding:2px 10px;border-radius:6px;margin-bottom:12px;
}
.step-item h3{font-size:14px;font-weight:600;margin-bottom:8px;color:var(--text);}
.step-item p{color:var(--muted);font-size:12px;line-height:1.7;}

/* ── DEMO ── */
.demo-layout{display:grid;grid-template-columns:1fr 340px;gap:24px;align-items:start;}
.cam-box{
  background:var(--bg2);border:1.5px solid var(--border);
  border-radius:20px;overflow:hidden;aspect-ratio:4/3;position:relative;
  box-shadow:0 2px 20px rgba(245,158,11,0.08);
}
.cam-ph{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:14px;}
.cam-ph p{color:var(--muted);font-size:14px;}
.cam-foot{display:flex;align-items:center;justify-content:space-between;margin-top:10px;}
.s-row{display:flex;align-items:center;gap:7px;font-size:13px;color:var(--muted);}
.dot{width:7px;height:7px;border-radius:50%;background:#e2c4b0;}
.dot.on{background:var(--amber);box-shadow:0 0 8px rgba(245,158,11,0.4);animation:glow 1.5s infinite;}
@keyframes glow{0%,100%{opacity:1}50%{opacity:.5}}
.stop-btn{
  font-size:12px;font-weight:600;color:#ef4444;
  background:rgba(239,68,68,.06);border:1px solid rgba(239,68,68,.2);
  padding:7px 16px;border-radius:100px;cursor:pointer;
  font-family:'Plus Jakarta Sans',sans-serif;transition:.2s;
}
.stop-btn:hover{background:rgba(239,68,68,.1);}

.d-panel{display:flex;flex-direction:column;gap:12px;}
.d-block{
  background:var(--white);border:1.5px solid var(--border);
  border-radius:16px;padding:20px 22px;
  box-shadow:0 2px 12px rgba(245,158,11,0.06);
}
.d-label{font-size:10px;font-weight:600;text-transform:uppercase;letter-spacing:2px;color:var(--muted);margin-bottom:12px;}
.mode-row{display:flex;gap:8px;}
.mode-btn{
  flex:1;padding:10px 8px;border-radius:100px;
  border:1.5px solid var(--border);background:transparent;
  color:var(--muted);font-size:12px;font-weight:500;
  cursor:pointer;font-family:'Plus Jakarta Sans',sans-serif;transition:.2s;
}
.mode-btn:hover{border-color:var(--amber);color:var(--amber);}
.mode-btn.active{
  background:linear-gradient(135deg,rgba(245,158,11,0.1),rgba(239,68,68,0.1));
  border-color:rgba(245,158,11,0.4);color:var(--amber);
}
.big-l{
  font-family:'Cormorant Garamond',serif;
  font-size:76px;font-weight:600;line-height:1;
  background:linear-gradient(135deg,#f59e0b,#ef4444);
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;
  background-clip:text;
}
.c-track{height:3px;background:var(--border);border-radius:2px;overflow:hidden;}
.c-fill{height:100%;background:linear-gradient(90deg,#f59e0b,#ef4444);border-radius:2px;width:0%;transition:width .3s;}
.word-d{
  font-family:'Cormorant Garamond',serif;
  font-size:26px;font-weight:600;color:var(--text);
  min-height:36px;word-break:break-all;margin-bottom:14px;
}
.w-btns{display:flex;gap:8px;}
.w-btn{
  flex:1;padding:10px 8px;border:1.5px solid var(--border);
  border-radius:100px;background:transparent;color:var(--muted);
  font-size:12px;font-weight:500;cursor:pointer;
  font-family:'Plus Jakarta Sans',sans-serif;transition:.2s;
}
.w-btn:hover{border-color:var(--amber);color:var(--amber);}
.w-btn.green{
  background:linear-gradient(135deg,rgba(245,158,11,0.1),rgba(239,68,68,0.1));
  border-color:rgba(245,158,11,0.3);color:var(--amber);
}
.w-btn.green:hover{background:linear-gradient(135deg,rgba(245,158,11,0.15),rgba(239,68,68,0.15));}
.a-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(34px,1fr));gap:4px;}
.alpha-key{
  background:var(--light);border:1px solid var(--border);
  border-radius:7px;padding:6px 4px;text-align:center;
  font-size:12px;font-weight:600;color:var(--muted);transition:.15s;
}
.alpha-key.lit{
  background:rgba(245,158,11,.1);border-color:rgba(245,158,11,.4);
  color:var(--amber);transform:scale(1.1);
}
.b-pill{
  display:inline-block;font-size:11px;font-weight:500;
  padding:3px 12px;border-radius:100px;
  background:var(--white);border:1px solid var(--border);
  color:var(--muted);margin-top:8px;
}
.b-pill.ok{background:rgba(245,158,11,.08);border-color:rgba(245,158,11,.2);color:var(--amber);}
.b-pill.err{background:rgba(239,68,68,.06);border-color:rgba(239,68,68,.15);color:#ef4444;}

/* ── TEAM ── */
.team-g{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:18px;margin-top:48px;}
.t-card{
  background:var(--white);border:1.5px solid var(--border);
  border-radius:18px;padding:28px 22px;text-align:center;
  box-shadow:0 2px 16px rgba(245,158,11,0.07);
  transition:border-color .2s,transform .2s,box-shadow .2s;
}
.t-card:hover{border-color:rgba(245,158,11,.3);transform:translateY(-4px);box-shadow:0 12px 36px rgba(245,158,11,0.12);}
.t-avatar{
  width:60px;height:60px;border-radius:16px;
  display:flex;align-items:center;justify-content:center;
  font-family:'Cormorant Garamond',serif;
  font-size:22px;font-weight:600;margin:0 auto 14px;
}
.t-card h3{font-size:15px;font-weight:600;margin-bottom:4px;color:var(--text);}
.t-role{font-size:13px;color:var(--muted);}
.t-contrib{font-size:12px;margin-top:8px;font-weight:600;}

/* ── FOOTER ── */
footer{
  border-top:1px solid var(--border);
  padding:60px 64px;text-align:center;
  background:var(--white);
}
.foot-inner{max-width:600px;margin:0 auto;}
.foot-logo{
  font-size:22px;font-weight:600;margin-bottom:14px;
  font-family:'Cormorant Garamond',serif;
  background:linear-gradient(135deg,#f59e0b,#ef4444);
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;
  background-clip:text;
}
footer p{font-size:14px;color:var(--muted);margin-bottom:6px;}
.foot-sub{font-size:12px;color:#e2c4b0!important;}
.foot-tech{display:flex;flex-wrap:wrap;gap:8px;justify-content:center;margin-top:24px;}
.foot-tech span{
  font-size:11px;font-weight:500;
  background:rgba(245,158,11,.06);
  border:1px solid rgba(245,158,11,.15);
  color:var(--amber);padding:4px 12px;border-radius:100px;
}

@media(max-width:900px){
  nav{padding:0 24px;}
  .nav-links{display:none;}
  .section{padding:60px 24px;}
  #hero{padding:100px 24px 60px;}
  .cards-3{grid-template-columns:1fr;}
  .steps-row{grid-template-columns:1fr;}
  .step-item{border-right:none;border-bottom:1px solid var(--border);}
  .demo-layout{grid-template-columns:1fr;}
  footer{padding:48px 24px;}
  .hero-stats{flex-wrap:wrap;}
}

# HTML(Purple) -----------------------------------------------

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>SignBridge — Sign Language Recognition</title>
<link href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;500;600;700;800;900&family=Cormorant+Garamond:ital,wght@1,600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css">
</head>
<body>

<!-- BUBBLES -->
<div class="bubbles-wrap" id="bubbles"></div>

<nav>
  <div class="nav-logo">✋ SignBridge</div>
  <div class="nav-links">
    <a href="#about">About</a>
    <a href="#how">How it works</a>
    <a href="#demo">Live demo</a>
    <a href="#team">Team</a>
  </div>
</nav>

<section id="hero">
  <div class="orb orb1"></div>
  <div class="orb orb2"></div>
  <div class="orb orb3"></div>
  <div class="hero-tag"><span class="tag-dot"></span> B.Tech Project — ML &amp; DL</div>
  <h1>Sign language meets<br><span class="h1-g">intelligence</span></h1>
  <p class="hero-sub">Real-time gesture recognition using computer vision and deep learning — bridging communication between deaf, mute, and blind individuals.</p>
  <div class="hero-btns">
    <a href="#demo" class="btn-primary">🫧 Try live demo</a>
    <a href="#how"  class="btn-secondary">How it works ↓</a>
  </div>
  <div class="hero-stats">
    <div class="stat-card"><span class="stat-n">26+</span><span class="stat-l">Gestures</span></div>
    <div class="stat-card"><span class="stat-n">96%</span><span class="stat-l">Accuracy</span></div>
    <div class="stat-card"><span class="stat-n">21</span><span class="stat-l">Landmarks</span></div>
    <div class="stat-card"><span class="stat-n">&lt;100ms</span><span class="stat-l">Response</span></div>
  </div>
</section>

<section id="about" class="section bg-soft">
  <div class="section-inner">
    <div class="s-label">About the project</div>
    <h2>Who does this <em>help?</em></h2>
    <div class="cards-3">
      <div class="g-card"><div class="g-icon">🤟</div><h3>Deaf &amp; mute users</h3><p>Show a hand gesture to the camera. MediaPipe detects your landmarks, the CNN model recognizes the sign, and pyttsx3 speaks it out loud instantly.</p></div>
      <div class="g-card"><div class="g-icon">🎙️</div><h3>Blind users</h3><p>Speak naturally into the microphone. SpeechRecognition converts your voice to text in real-time, displayed clearly on screen for others to read.</p></div>
      <div class="g-card"><div class="g-icon">🔁</div><h3>Two-way communication</h3><p>Switch between sign-to-voice and voice-to-text with one tap — enabling complete conversations for everyone.</p></div>
    </div>
  </div>
</section>

<section id="how" class="section">
  <div class="section-inner">
    <div class="s-label">Technology</div>
    <h2>How it <em>works</em></h2>
    <p class="s-sub">Five modules working together — gesture to speech in under 100ms.</p>
    <div class="steps-row">
      <div class="step-item"><div class="step-num-circle">01</div><div class="step-tech">OpenCV</div><h3>Camera capture</h3><p>Opens webcam at 30fps, passes each frame to MediaPipe.</p></div>
      <div class="step-item"><div class="step-num-circle">02</div><div class="step-tech">MediaPipe</div><h3>Hand detection</h3><p>Maps 21 landmark points as x, y, z coordinates.</p></div>
      <div class="step-item"><div class="step-num-circle">03</div><div class="step-tech">TensorFlow</div><h3>Recognition</h3><p>CNN model identifies gesture with confidence score.</p></div>
      <div class="step-item"><div class="step-num-circle">04</div><div class="step-tech">pyttsx3</div><h3>Speech output</h3><p>Converts predicted text to natural voice instantly.</p></div>
      <div class="step-item"><div class="step-num-circle">05</div><div class="step-tech">SpeechRecog</div><h3>Voice to text</h3><p>Mic input transcribed in real-time on screen.</p></div>
    </div>
  </div>
</section>

<section id="demo" class="section bg-soft">
  <div class="section-inner">
    <div class="s-label">Interactive demo</div>
    <h2>Try it <em>live</em></h2>
    <p class="s-sub">Start the camera, show your hand — predictions in real-time.<br>
    <span id="backend-status" class="b-pill">Checking backend...</span></p>
    <div class="demo-layout">
      <div>
        <div class="cam-box">
          <img id="cam-feed" style="width:100%;height:100%;object-fit:cover;display:none;border-radius:22px;" alt="feed">
          <div id="cam-placeholder" class="cam-ph">
            <div style="font-size:52px">🫧</div>
            <p>Camera not started</p>
            <button class="btn-primary" id="start-btn" onclick="startCamera()">Start camera</button>
          </div>
        </div>
        <div class="cam-foot">
          <div class="s-row"><div class="dot" id="status-dot"></div><span id="status-text">No hand detected</span></div>
          <button class="stop-btn" id="stop-btn" onclick="stopCamera()" style="display:none">Stop</button>
        </div>
      </div>
      <div class="d-panel">
        <div class="d-block">
          <div class="d-label">Mode</div>
          <div class="mode-row">
            <button class="mode-btn active" id="mode-sign"  onclick="setMode('sign')">✋ Sign → Voice</button>
            <button class="mode-btn"        id="mode-voice" onclick="setMode('voice')">🎙 Voice → Text</button>
          </div>
        </div>
        <div class="d-block">
          <div class="d-label">Detected gesture</div>
          <div style="display:flex;align-items:center;gap:16px">
            <div id="big-letter" class="big-l">—</div>
            <div style="flex:1">
              <div class="c-track"><div id="conf-fill" class="c-fill"></div></div>
              <div id="conf-text" style="font-size:12px;color:var(--muted);margin-top:5px;font-weight:600">—</div>
            </div>
          </div>
        </div>
        <div class="d-block">
          <div class="d-label">Word builder</div>
          <div id="word-display" class="word-d">—</div>
          <div class="w-btns">
            <button class="w-btn" onclick="addLetter()">Add</button>
            <button class="w-btn" onclick="clearWord()">Clear</button>
            <button class="w-btn green" onclick="speakWord()">🔊 Speak</button>
          </div>
        </div>
        <div class="d-block">
          <div class="d-label">ASL reference</div>
          <div class="a-grid" id="alpha-grid"></div>
        </div>
      </div>
    </div>
    <div id="voice-panel" style="display:none;margin-top:24px">
      <div class="d-block" style="max-width:540px">
        <div class="d-label">Voice to text — blind user mode</div>
        <div id="voice-output" style="font-size:18px;min-height:46px;color:var(--text);padding:8px 0;font-weight:600">Speak into your microphone...</div>
        <button class="btn-primary" id="voice-btn" onclick="toggleVoice()" style="margin-top:14px">🎙 Start listening</button>
      </div>
    </div>
  </div>
</section>

<section id="team" class="section">
  <div class="section-inner">
    <div class="s-label">Our team</div>
    <h2>The <em>builders</em></h2>
    <p class="s-sub">B.Tech students making communication accessible for everyone.</p>
    <div class="team-g" id="team-grid"></div>
  </div>
</section>

<footer>
  <div class="foot-inner">
    <div class="foot-logo">✋ SignBridge</div>
    <p>Enhancing Accessibility using Sign Language Recognition with ML &amp; DL</p>
    <p class="foot-sub">B.Tech · Academic Project</p>
    <div class="foot-tech">
      <span>Python</span><span>OpenCV</span><span>MediaPipe</span><span>TensorFlow</span><span>Flask</span><span>pyttsx3</span>
    </div>
  </div>
</footer>

<script src="script.js"></script>
<script>
// ── BUBBLES ──
const wrap = document.getElementById('bubbles');
const bubbleCount = 18;
for(let i = 0; i < bubbleCount; i++){
  const b = document.createElement('div');
  b.className = 'bubble';
  const size = Math.random() * 60 + 20;
  const left = Math.random() * 100;
  const dur  = Math.random() * 12 + 8;
  const delay = Math.random() * 10;
  b.style.cssText = `
    width:${size}px;height:${size}px;
    left:${left}%;
    animation-duration:${dur}s;
    animation-delay:-${delay}s;
    opacity:${Math.random()*.5+.2};
  `;
  wrap.appendChild(b);
}

// ── Team ──
const team = [
  {name:"Member 1",role:"ML Engineer",       contrib:"CNN model & training",  color:"#7c3aed",bg:"rgba(124,58,237,0.1)"},
  {name:"Member 2",role:"Computer Vision",   contrib:"MediaPipe integration", color:"#9b73e8",bg:"rgba(155,115,232,0.1)"},
  {name:"Member 3",role:"Backend Developer", contrib:"Flask API & Python",    color:"#e879f9",bg:"rgba(232,121,249,0.1)"},
  {name:"Member 4",role:"Frontend Developer",contrib:"UI & website",          color:"#c4b5fd",bg:"rgba(196,181,253,0.15)"},
  {name:"Member 5",role:"Data Engineer",     contrib:"Dataset & collection",  color:"#7c3aed",bg:"rgba(124,58,237,0.1)"},
];
const grid = document.getElementById("team-grid");
team.forEach(m => {
  const initials = m.name.split(" ").map(w=>w[0]).join("");
  grid.innerHTML += `
    <div class="t-card">
      <div class="t-avatar" style="background:${m.bg};color:${m.color}">${initials}</div>
      <h3>${m.name}</h3>
      <div class="t-role">${m.role}</div>
      @import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;500;600;700;800;900&family=Cormorant+Garamond:ital,wght@1,600&display=swap');

:root {
  --bg:     #efe9ff;
  --bg2:    #e4dcff;
  --bg3:    #f5f0ff;
  --white:  #f8f5ff;
  --border: #d0c4f5;
  --border2:#baaef0;
  --text:   #1a0840;
  --muted:  #7a6aaa;
  --lav:    #9b73e8;
  --lav2:   #6d28d9;
  --lav3:   #c4b5fd;
  --pink:   #e879f9;
  --soft:   #eae4ff;
}

*{margin:0;padding:0;box-sizing:border-box;}
html{scroll-behavior:smooth;}
body{background:var(--bg);color:var(--text);font-family:'Nunito',sans-serif;font-size:16px;line-height:1.7;overflow-x:hidden;}

/* ── BUBBLES ── */
.bubbles-wrap{position:fixed;inset:0;z-index:0;pointer-events:none;overflow:hidden;}
.bubble{
  position:absolute;border-radius:50%;
  background:linear-gradient(135deg,rgba(147,90,230,0.35),rgba(255,255,255,0.12));
  border:1px solid rgba(255,255,255,0.35);
  animation:bubbleFloat linear infinite;
}
@keyframes bubbleFloat{
  0%  {transform:translateY(110vh) scale(0.8);opacity:0;}
  10% {opacity:1;}
  90% {opacity:.6;}
  100%{transform:translateY(-10vh) scale(1.1);opacity:0;}
}

nav,section,footer{position:relative;z-index:1;}

/* ── NAV ── */
nav{
  position:fixed;top:0;left:0;right:0;z-index:100;
  display:flex;align-items:center;justify-content:space-between;
  padding:0 64px;height:68px;
  background:rgba(235,228,255,0.92);
  backdrop-filter:blur(20px);
  border-bottom:1px solid var(--border);
}
.nav-logo{
  font-size:20px;font-weight:900;letter-spacing:-0.5px;
  background:linear-gradient(135deg,#7c3aed,#e879f9);
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;
}
.nav-links{display:flex;gap:36px;}
.nav-links a{color:var(--muted);text-decoration:none;font-size:14px;font-weight:600;transition:color .2s;}
.nav-links a:hover{color:var(--lav2);}

/* ── HERO ── */
#hero{
  min-height:100vh;display:flex;flex-direction:column;
  align-items:center;justify-content:center;
  padding:100px 64px 80px;text-align:center;position:relative;
}

/* large soft orbs */
.orb{position:absolute;border-radius:50%;filter:blur(70px);pointer-events:none;animation:orbFloat 8s ease-in-out infinite;}
.orb1{width:500px;height:500px;background:rgba(140,100,220,0.1);top:-10%;left:-10%;animation-delay:0s;}
.orb2{width:400px;height:400px;background:rgba(180,60,220,0.15);top:20%;right:-8%;animation-delay:2s;}
.orb3{width:350px;height:350px;background:rgba(130,80,230,0.18);bottom:-5%;left:20%;animation-delay:4s;}
@keyframes orbFloat{0%,100%{transform:translate(0,0)}50%{transform:translate(20px,-20px)}}

.hero-tag{
  display:inline-flex;align-items:center;gap:8px;
  font-size:11px;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;
  color:var(--lav2);background:rgba(124,58,237,0.08);
  border:1px solid rgba(124,58,237,0.2);
  padding:7px 20px;border-radius:100px;margin-bottom:36px;
  animation:fadeUp .6s ease both;
}
.tag-dot{width:6px;height:6px;border-radius:50%;background:var(--lav2);animation:pulse 2s infinite;}
@keyframes pulse{0%,100%{opacity:1;transform:scale(1)}50%{opacity:.4;transform:scale(.7)}}

h1{
  font-family:'Nunito',sans-serif;font-size:clamp(44px,6.5vw,90px);
  font-weight:900;line-height:1.0;letter-spacing:-3px;margin-bottom:24px;
  animation:fadeUp .6s .1s ease both;color:var(--text);
}
.h1-g{
  font-family:'Cormorant Garamond',serif;font-style:italic;font-size:1.1em;
  background:linear-gradient(135deg,#7c3aed,#9b73e8,#e879f9,#c4b5fd);
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;
}

.hero-sub{max-width:540px;color:var(--muted);font-size:17px;font-weight:500;margin:0 auto 48px;line-height:1.8;animation:fadeUp .6s .2s ease both;}
.hero-btns{display:flex;gap:14px;justify-content:center;margin-bottom:60px;animation:fadeUp .6s .3s ease both;}

.btn-primary{
  background:linear-gradient(135deg,#7c3aed,#e879f9);
  color:#fff;padding:14px 36px;border-radius:100px;
  font-size:14px;font-weight:800;text-decoration:none;border:none;cursor:pointer;
  font-family:'Nunito',sans-serif;transition:transform .2s,box-shadow .2s;display:inline-block;
  box-shadow:0 4px 24px rgba(124,58,237,0.35);
}
.btn-primary:hover{transform:translateY(-2px);box-shadow:0 12px 40px rgba(124,58,237,0.45);}
.btn-secondary{
  background:var(--white);color:var(--lav2);
  padding:14px 36px;border-radius:100px;font-size:14px;font-weight:600;
  text-decoration:none;border:2px solid var(--border2);
  cursor:pointer;font-family:'Nunito',sans-serif;transition:.2s;display:inline-block;
  box-shadow:0 2px 12px rgba(124,58,237,0.1);
}
.btn-secondary:hover{border-color:var(--lav2);box-shadow:0 4px 20px rgba(124,58,237,0.2);}

.hero-stats{
  display:flex;gap:0;animation:fadeUp .6s .4s ease both;
  border:2px solid var(--border2);border-radius:24px;overflow:hidden;
  background:var(--white);box-shadow:0 4px 30px rgba(124,58,237,0.1);
}
.stat-card{padding:22px 40px;text-align:center;border-right:1px solid var(--border);transition:background .2s;}
.stat-card:last-child{border-right:none;}
.stat-card:hover{background:rgba(124,58,237,0.03);}
.stat-n{
  font-size:32px;font-weight:900;display:block;line-height:1;letter-spacing:-1px;
  background:linear-gradient(135deg,#7c3aed,#e879f9);
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;
}
.stat-l{font-size:11px;color:var(--muted);margin-top:5px;display:block;font-weight:600;text-transform:uppercase;letter-spacing:1px;}

@keyframes fadeUp{from{opacity:0;transform:translateY(24px)}to{opacity:1;transform:translateY(0)}}

/* ── SECTIONS ── */
.section{padding:100px 64px;}
.section-inner{max-width:1160px;margin:0 auto;}
.bg-soft{background:var(--bg2);}
.s-label{font-size:11px;font-weight:800;letter-spacing:2.5px;text-transform:uppercase;color:var(--lav2);margin-bottom:14px;}
h2{font-family:'Nunito',sans-serif;font-size:clamp(28px,3.5vw,48px);font-weight:900;letter-spacing:-1.5px;line-height:1.05;margin-bottom:16px;color:var(--text);}
h2 em{font-style:italic;font-family:'Cormorant Garamond',serif;font-size:1.05em;color:var(--lav2);}
.s-sub{color:var(--muted);font-size:16px;max-width:480px;margin-bottom:52px;line-height:1.8;font-weight:500;}

/* ── ABOUT ── */
.cards-3{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin-top:48px;}
.g-card{
  background:var(--white);border:2px solid var(--border);
  border-radius:24px;padding:36px 28px;
  transition:transform .2s,box-shadow .2s,border-color .2s;
  position:relative;overflow:hidden;
}
.g-card::before{content:'';position:absolute;top:0;left:0;right:0;height:3px;background:linear-gradient(90deg,#7c3aed,#e879f9,#c4b5fd);opacity:0;transition:opacity .3s;}
.g-card:hover{transform:translateY(-6px);box-shadow:0 20px 50px rgba(124,58,237,0.12);border-color:rgba(124,58,237,0.3);}
.g-card:hover::before{opacity:1;}
.g-icon{font-size:36px;margin-bottom:18px;}
.g-card h3{font-size:18px;font-weight:800;margin-bottom:10px;color:var(--text);}
.g-card p{color:var(--muted);font-size:14px;line-height:1.75;}

/* ── HOW ── */
.steps-row{display:grid;grid-template-columns:repeat(5,1fr);gap:16px;margin-top:48px;}
.step-item{
  background:var(--white);border:2px solid var(--border);
  border-radius:20px;padding:28px 20px;text-align:center;
  transition:transform .2s,box-shadow .2s;
}
.step-item:hover{transform:translateY(-4px);box-shadow:0 12px 30px rgba(124,58,237,0.1);border-color:var(--lav3);}
.step-num-circle{
  width:44px;height:44px;border-radius:50%;
  background:linear-gradient(135deg,rgba(124,58,237,0.15),rgba(232,121,249,0.15));
  border:2px solid rgba(124,58,237,0.2);
  display:flex;align-items:center;justify-content:center;
  font-size:14px;font-weight:800;color:var(--lav2);margin:0 auto 14px;
}
.step-tech{display:inline-block;font-size:10px;font-weight:700;background:rgba(124,58,237,0.08);color:var(--lav2);border:1px solid rgba(124,58,237,0.2);padding:3px 10px;border-radius:100px;margin-bottom:10px;}
.step-item h3{font-size:14px;font-weight:800;margin-bottom:6px;color:var(--text);}
.step-item p{color:var(--muted);font-size:12px;line-height:1.7;}

/* ── DEMO ── */
.demo-layout{display:grid;grid-template-columns:1fr 340px;gap:24px;align-items:start;}
.cam-box{background:var(--bg2);border:2px solid var(--border);border-radius:24px;overflow:hidden;aspect-ratio:4/3;position:relative;box-shadow:0 4px 20px rgba(124,58,237,0.08);}
.cam-ph{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:14px;}
.cam-ph p{color:var(--muted);font-size:14px;font-weight:600;}
.cam-foot{display:flex;align-items:center;justify-content:space-between;margin-top:10px;}
.s-row{display:flex;align-items:center;gap:7px;font-size:13px;color:var(--muted);font-weight:600;}
.dot{width:7px;height:7px;border-radius:50%;background:#d0c0e8;}
.dot.on{background:var(--lav2);box-shadow:0 0 10px rgba(124,58,237,0.5);animation:glow 1.5s infinite;}
@keyframes glow{0%,100%{opacity:1}50%{opacity:.4}}
.stop-btn{font-size:12px;font-weight:700;color:#f43f5e;background:rgba(244,63,94,.06);border:1px solid rgba(244,63,94,.2);padding:7px 16px;border-radius:100px;cursor:pointer;font-family:'Nunito',sans-serif;transition:.2s;}

.d-panel{display:flex;flex-direction:column;gap:12px;}
.d-block{background:var(--white);border:2px solid var(--border);border-radius:18px;padding:20px 22px;box-shadow:0 2px 12px rgba(124,58,237,0.05);}
.d-label{font-size:10px;font-weight:800;text-transform:uppercase;letter-spacing:2px;color:var(--muted);margin-bottom:12px;}
.mode-row{display:flex;gap:8px;}
.mode-btn{flex:1;padding:10px 8px;border-radius:100px;border:2px solid var(--border);background:transparent;color:var(--muted);font-size:12px;font-weight:700;cursor:pointer;font-family:'Nunito',sans-serif;transition:.2s;}
.mode-btn:hover{border-color:var(--lav2);color:var(--lav2);}
.mode-btn.active{background:linear-gradient(135deg,rgba(124,58,237,0.1),rgba(232,121,249,0.1));border-color:rgba(124,58,237,0.4);color:var(--lav2);}
.big-l{font-size:72px;font-weight:900;line-height:1;letter-spacing:-3px;background:linear-gradient(135deg,#7c3aed,#e879f9);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;}
.c-track{height:4px;background:var(--border);border-radius:2px;overflow:hidden;margin-top:8px;}
.c-fill{height:100%;background:linear-gradient(90deg,#7c3aed,#9b73e8,#e879f9);border-radius:2px;width:0%;transition:width .3s;}
.word-d{font-size:26px;font-weight:900;color:var(--text);min-height:36px;word-break:break-all;margin-bottom:14px;letter-spacing:-1px;}
.w-btns{display:flex;gap:8px;}
.w-btn{flex:1;padding:10px 8px;border:2px solid var(--border);border-radius:100px;background:transparent;color:var(--muted);font-size:12px;font-weight:700;cursor:pointer;font-family:'Nunito',sans-serif;transition:.2s;}
.w-btn:hover{border-color:var(--lav2);color:var(--lav2);}
.w-btn.green{background:linear-gradient(135deg,rgba(124,58,237,0.1),rgba(232,121,249,0.1));border-color:rgba(124,58,237,0.3);color:var(--lav2);}
.a-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(34px,1fr));gap:4px;}
.alpha-key{background:var(--soft);border:1px solid var(--border);border-radius:8px;padding:6px 4px;text-align:center;font-size:12px;font-weight:700;color:var(--muted);transition:.15s;}
.alpha-key.lit{background:rgba(124,58,237,0.12);border-color:rgba(124,58,237,0.4);color:var(--lav2);transform:scale(1.1);}
.b-pill{display:inline-block;font-size:11px;font-weight:700;padding:3px 12px;border-radius:100px;background:var(--white);border:1px solid var(--border);color:var(--muted);margin-top:8px;}
.b-pill.ok{background:rgba(124,58,237,.08);border-color:rgba(124,58,237,.25);color:var(--lav2);}
.b-pill.err{background:rgba(244,63,94,.06);border-color:rgba(244,63,94,.15);color:#f43f5e;}

/* ── TEAM ── */
.team-g{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:18px;margin-top:48px;}
.t-card{background:var(--white);border:2px solid var(--border);border-radius:22px;padding:28px 22px;text-align:center;transition:transform .2s,box-shadow .2s,border-color .2s;}
.t-card:hover{transform:translateY(-5px);box-shadow:0 16px 40px rgba(124,58,237,0.12);border-color:rgba(124,58,237,0.3);}
.t-avatar{width:60px;height:60px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:22px;font-weight:900;margin:0 auto 14px;border:2px solid var(--border2);}
.t-card h3{font-size:15px;font-weight:800;margin-bottom:4px;color:var(--text);}
.t-role{font-size:13px;color:var(--muted);font-weight:600;}
.t-contrib{font-size:12px;margin-top:8px;font-weight:700;color:var(--lav2);}

/* ── FOOTER ── */
footer{border-top:2px solid var(--border);padding:60px 64px;text-align:center;background:var(--white);}
.foot-inner{max-width:600px;margin:0 auto;}
.foot-logo{font-size:24px;font-weight:900;margin-bottom:14px;letter-spacing:-0.5px;background:linear-gradient(135deg,#7c3aed,#9b73e8,#e879f9,#c4b5fd);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;}
footer p{font-size:14px;color:var(--muted);margin-bottom:6px;font-weight:600;}
.foot-sub{font-size:12px;color:#c0b0e0!important;}
.foot-tech{display:flex;flex-wrap:wrap;gap:8px;justify-content:center;margin-top:24px;}
.foot-tech span{font-size:11px;font-weight:700;background:rgba(124,58,237,.08);border:1px solid rgba(124,58,237,.2);color:var(--lav2);padding:4px 14px;border-radius:100px;}

@media(max-width:900px){
  nav{padding:0 24px;} .nav-links{display:none;}
  .section{padding:60px 24px;} #hero{padding:100px 24px 60px;}
  .cards-3,.steps-row{grid-template-columns:1fr;}
  .demo-layout{grid-template-columns:1fr;}
  footer{padding:48px 24px;}
  .hero-stats{flex-wrap:wrap;}
}


<div class="t-contrib">${m.contrib}</div>
    </div>`;
});
</script>
</body>
</html>

# CSS (PURPlE) ----------------------------------------
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;500;600;700;800;900&family=Cormorant+Garamond:ital,wght@1,600&display=swap');

:root {
  --bg:     #efe9ff;
  --bg2:    #e4dcff;
  --bg3:    #f5f0ff;
  --white:  #f8f5ff;
  --border: #d0c4f5;
  --border2:#baaef0;
  --text:   #1a0840;
  --muted:  #7a6aaa;
  --lav:    #9b73e8;
  --lav2:   #6d28d9;
  --lav3:   #c4b5fd;
  --pink:   #e879f9;
  --soft:   #eae4ff;
}

*{margin:0;padding:0;box-sizing:border-box;}
html{scroll-behavior:smooth;}
body{background:var(--bg);color:var(--text);font-family:'Nunito',sans-serif;font-size:16px;line-height:1.7;overflow-x:hidden;}

/* ── BUBBLES ── */
.bubbles-wrap{position:fixed;inset:0;z-index:0;pointer-events:none;overflow:hidden;}
.bubble{
  position:absolute;border-radius:50%;
  background:linear-gradient(135deg,rgba(147,90,230,0.35),rgba(255,255,255,0.12));
  border:1px solid rgba(255,255,255,0.35);
  animation:bubbleFloat linear infinite;
}
@keyframes bubbleFloat{
  0%  {transform:translateY(110vh) scale(0.8);opacity:0;}
  10% {opacity:1;}
  90% {opacity:.6;}
  100%{transform:translateY(-10vh) scale(1.1);opacity:0;}
}

nav,section,footer{position:relative;z-index:1;}

/* ── NAV ── */
nav{
  position:fixed;top:0;left:0;right:0;z-index:100;
  display:flex;align-items:center;justify-content:space-between;
  padding:0 64px;height:68px;
  background:rgba(235,228,255,0.92);
  backdrop-filter:blur(20px);
  border-bottom:1px solid var(--border);
}
.nav-logo{
  font-size:20px;font-weight:900;letter-spacing:-0.5px;
  background:linear-gradient(135deg,#7c3aed,#e879f9);
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;
}
.nav-links{display:flex;gap:36px;}
.nav-links a{color:var(--muted);text-decoration:none;font-size:14px;font-weight:600;transition:color .2s;}
.nav-links a:hover{color:var(--lav2);}

/* ── HERO ── */
#hero{
  min-height:100vh;display:flex;flex-direction:column;
  align-items:center;justify-content:center;
  padding:100px 64px 80px;text-align:center;position:relative;
}

/* large soft orbs */
.orb{position:absolute;border-radius:50%;filter:blur(70px);pointer-events:none;animation:orbFloat 8s ease-in-out infinite;}
.orb1{width:500px;height:500px;background:rgba(140,100,220,0.1);top:-10%;left:-10%;animation-delay:0s;}
.orb2{width:400px;height:400px;background:rgba(180,60,220,0.15);top:20%;right:-8%;animation-delay:2s;}
.orb3{width:350px;height:350px;background:rgba(130,80,230,0.18);bottom:-5%;left:20%;animation-delay:4s;}
@keyframes orbFloat{0%,100%{transform:translate(0,0)}50%{transform:translate(20px,-20px)}}

.hero-tag{
  display:inline-flex;align-items:center;gap:8px;
  font-size:11px;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;
  color:var(--lav2);background:rgba(124,58,237,0.08);
  border:1px solid rgba(124,58,237,0.2);
  padding:7px 20px;border-radius:100px;margin-bottom:36px;
  animation:fadeUp .6s ease both;
}
.tag-dot{width:6px;height:6px;border-radius:50%;background:var(--lav2);animation:pulse 2s infinite;}
@keyframes pulse{0%,100%{opacity:1;transform:scale(1)}50%{opacity:.4;transform:scale(.7)}}

h1{
  font-family:'Nunito',sans-serif;font-size:clamp(44px,6.5vw,90px);
  font-weight:900;line-height:1.0;letter-spacing:-3px;margin-bottom:24px;
  animation:fadeUp .6s .1s ease both;color:var(--text);
}
.h1-g{
  font-family:'Cormorant Garamond',serif;font-style:italic;font-size:1.1em;
  background:linear-gradient(135deg,#7c3aed,#9b73e8,#e879f9,#c4b5fd);
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;
}

.hero-sub{max-width:540px;color:var(--muted);font-size:17px;font-weight:500;margin:0 auto 48px;line-height:1.8;animation:fadeUp .6s .2s ease both;}
.hero-btns{display:flex;gap:14px;justify-content:center;margin-bottom:60px;animation:fadeUp .6s .3s ease both;}

.btn-primary{
  background:linear-gradient(135deg,#7c3aed,#e879f9);
  color:#fff;padding:14px 36px;border-radius:100px;
  font-size:14px;font-weight:800;text-decoration:none;border:none;cursor:pointer;
  font-family:'Nunito',sans-serif;transition:transform .2s,box-shadow .2s;display:inline-block;
  box-shadow:0 4px 24px rgba(124,58,237,0.35);
}
.btn-primary:hover{transform:translateY(-2px);box-shadow:0 12px 40px rgba(124,58,237,0.45);}
.btn-secondary{
  background:var(--white);color:var(--lav2);
  padding:14px 36px;border-radius:100px;font-size:14px;font-weight:600;
  text-decoration:none;border:2px solid var(--border2);
  cursor:pointer;font-family:'Nunito',sans-serif;transition:.2s;display:inline-block;
  box-shadow:0 2px 12px rgba(124,58,237,0.1);
}
.btn-secondary:hover{border-color:var(--lav2);box-shadow:0 4px 20px rgba(124,58,237,0.2);}

.hero-stats{
  display:flex;gap:0;animation:fadeUp .6s .4s ease both;
  border:2px solid var(--border2);border-radius:24px;overflow:hidden;
  background:var(--white);box-shadow:0 4px 30px rgba(124,58,237,0.1);
}
.stat-card{padding:22px 40px;text-align:center;border-right:1px solid var(--border);transition:background .2s;}
.stat-card:last-child{border-right:none;}
.stat-card:hover{background:rgba(124,58,237,0.03);}
.stat-n{
  font-size:32px;font-weight:900;display:block;line-height:1;letter-spacing:-1px;
  background:linear-gradient(135deg,#7c3aed,#e879f9);
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;
}
.stat-l{font-size:11px;color:var(--muted);margin-top:5px;display:block;font-weight:600;text-transform:uppercase;letter-spacing:1px;}

@keyframes fadeUp{from{opacity:0;transform:translateY(24px)}to{opacity:1;transform:translateY(0)}}

/* ── SECTIONS ── */
.section{padding:100px 64px;}
.section-inner{max-width:1160px;margin:0 auto;}
.bg-soft{background:var(--bg2);}
.s-label{font-size:11px;font-weight:800;letter-spacing:2.5px;text-transform:uppercase;color:var(--lav2);margin-bottom:14px;}
h2{font-family:'Nunito',sans-serif;font-size:clamp(28px,3.5vw,48px);font-weight:900;letter-spacing:-1.5px;line-height:1.05;margin-bottom:16px;color:var(--text);}
h2 em{font-style:italic;font-family:'Cormorant Garamond',serif;font-size:1.05em;color:var(--lav2);}
.s-sub{color:var(--muted);font-size:16px;max-width:480px;margin-bottom:52px;line-height:1.8;font-weight:500;}

/* ── ABOUT ── */
.cards-3{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin-top:48px;}
.g-card{
  background:var(--white);border:2px solid var(--border);
  border-radius:24px;padding:36px 28px;
  transition:transform .2s,box-shadow .2s,border-color .2s;
  position:relative;overflow:hidden;
}
.g-card::before{content:'';position:absolute;top:0;left:0;right:0;height:3px;background:linear-gradient(90deg,#7c3aed,#e879f9,#c4b5fd);opacity:0;transition:opacity .3s;}
.g-card:hover{transform:translateY(-6px);box-shadow:0 20px 50px rgba(124,58,237,0.12);border-color:rgba(124,58,237,0.3);}
.g-card:hover::before{opacity:1;}
.g-icon{font-size:36px;margin-bottom:18px;}
.g-card h3{font-size:18px;font-weight:800;margin-bottom:10px;color:var(--text);}
.g-card p{color:var(--muted);font-size:14px;line-height:1.75;}

/* ── HOW ── */
.steps-row{display:grid;grid-template-columns:repeat(5,1fr);gap:16px;margin-top:48px;}
.step-item{
  background:var(--white);border:2px solid var(--border);
  border-radius:20px;padding:28px 20px;text-align:center;
  transition:transform .2s,box-shadow .2s;
}
.step-item:hover{transform:translateY(-4px);box-shadow:0 12px 30px rgba(124,58,237,0.1);border-color:var(--lav3);}
.step-num-circle{
  width:44px;height:44px;border-radius:50%;
  background:linear-gradient(135deg,rgba(124,58,237,0.15),rgba(232,121,249,0.15));
  border:2px solid rgba(124,58,237,0.2);
  display:flex;align-items:center;justify-content:center;
  font-size:14px;font-weight:800;color:var(--lav2);margin:0 auto 14px;
}
.step-tech{display:inline-block;font-size:10px;font-weight:700;background:rgba(124,58,237,0.08);color:var(--lav2);border:1px solid rgba(124,58,237,0.2);padding:3px 10px;border-radius:100px;margin-bottom:10px;}
.step-item h3{font-size:14px;font-weight:800;margin-bottom:6px;color:var(--text);}
.step-item p{color:var(--muted);font-size:12px;line-height:1.7;}

/* ── DEMO ── */
.demo-layout{display:grid;grid-template-columns:1fr 340px;gap:24px;align-items:start;}
.cam-box{background:var(--bg2);border:2px solid var(--border);border-radius:24px;overflow:hidden;aspect-ratio:4/3;position:relative;box-shadow:0 4px 20px rgba(124,58,237,0.08);}
.cam-ph{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:14px;}
.cam-ph p{color:var(--muted);font-size:14px;font-weight:600;}
.cam-foot{display:flex;align-items:center;justify-content:space-between;margin-top:10px;}
.s-row{display:flex;align-items:center;gap:7px;font-size:13px;color:var(--muted);font-weight:600;}
.dot{width:7px;height:7px;border-radius:50%;background:#d0c0e8;}
.dot.on{background:var(--lav2);box-shadow:0 0 10px rgba(124,58,237,0.5);animation:glow 1.5s infinite;}
@keyframes glow{0%,100%{opacity:1}50%{opacity:.4}}
.stop-btn{font-size:12px;font-weight:700;color:#f43f5e;background:rgba(244,63,94,.06);border:1px solid rgba(244,63,94,.2);padding:7px 16px;border-radius:100px;cursor:pointer;font-family:'Nunito',sans-serif;transition:.2s;}

.d-panel{display:flex;flex-direction:column;gap:12px;}
.d-block{background:var(--white);border:2px solid var(--border);border-radius:18px;padding:20px 22px;box-shadow:0 2px 12px rgba(124,58,237,0.05);}
.d-label{font-size:10px;font-weight:800;text-transform:uppercase;letter-spacing:2px;color:var(--muted);margin-bottom:12px;}
.mode-row{display:flex;gap:8px;}
.mode-btn{flex:1;padding:10px 8px;border-radius:100px;border:2px solid var(--border);background:transparent;color:var(--muted);font-size:12px;font-weight:700;cursor:pointer;font-family:'Nunito',sans-serif;transition:.2s;}
.mode-btn:hover{border-color:var(--lav2);color:var(--lav2);}
.mode-btn.active{background:linear-gradient(135deg,rgba(124,58,237,0.1),rgba(232,121,249,0.1));border-color:rgba(124,58,237,0.4);color:var(--lav2);}
.big-l{font-size:72px;font-weight:900;line-height:1;letter-spacing:-3px;background:linear-gradient(135deg,#7c3aed,#e879f9);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;}
.c-track{height:4px;background:var(--border);border-radius:2px;overflow:hidden;margin-top:8px;}
.c-fill{height:100%;background:linear-gradient(90deg,#7c3aed,#9b73e8,#e879f9);border-radius:2px;width:0%;transition:width .3s;}
.word-d{font-size:26px;font-weight:900;color:var(--text);min-height:36px;word-break:break-all;margin-bottom:14px;letter-spacing:-1px;}
.w-btns{display:flex;gap:8px;}
.w-btn{flex:1;padding:10px 8px;border:2px solid var(--border);border-radius:100px;background:transparent;color:var(--muted);font-size:12px;font-weight:700;cursor:pointer;font-family:'Nunito',sans-serif;transition:.2s;}
.w-btn:hover{border-color:var(--lav2);color:var(--lav2);}
.w-btn.green{background:linear-gradient(135deg,rgba(124,58,237,0.1),rgba(232,121,249,0.1));border-color:rgba(124,58,237,0.3);color:var(--lav2);}
.a-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(34px,1fr));gap:4px;}
.alpha-key{background:var(--soft);border:1px solid var(--border);border-radius:8px;padding:6px 4px;text-align:center;font-size:12px;font-weight:700;color:var(--muted);transition:.15s;}
.alpha-key.lit{background:rgba(124,58,237,0.12);border-color:rgba(124,58,237,0.4);color:var(--lav2);transform:scale(1.1);}
.b-pill{display:inline-block;font-size:11px;font-weight:700;padding:3px 12px;border-radius:100px;background:var(--white);border:1px solid var(--border);color:var(--muted);margin-top:8px;}
.b-pill.ok{background:rgba(124,58,237,.08);border-color:rgba(124,58,237,.25);color:var(--lav2);}
.b-pill.err{background:rgba(244,63,94,.06);border-color:rgba(244,63,94,.15);color:#f43f5e;}

/* ── TEAM ── */
.team-g{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:18px;margin-top:48px;}
.t-card{background:var(--white);border:2px solid var(--border);border-radius:22px;padding:28px 22px;text-align:center;transition:transform .2s,box-shadow .2s,border-color .2s;}
.t-card:hover{transform:translateY(-5px);box-shadow:0 16px 40px rgba(124,58,237,0.12);border-color:rgba(124,58,237,0.3);}
.t-avatar{width:60px;height:60px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:22px;font-weight:900;margin:0 auto 14px;border:2px solid var(--border2);}
.t-card h3{font-size:15px;font-weight:800;margin-bottom:4px;color:var(--text);}
.t-role{font-size:13px;color:var(--muted);font-weight:600;}
.t-contrib{font-size:12px;margin-top:8px;font-weight:700;color:var(--lav2);}

/* ── FOOTER ── */
footer{border-top:2px solid var(--border);padding:60px 64px;text-align:center;background:var(--white);}
.foot-inner{max-width:600px;margin:0 auto;}
.foot-logo{font-size:24px;font-weight:900;margin-bottom:14px;letter-spacing:-0.5px;background:linear-gradient(135deg,#7c3aed,#9b73e8,#e879f9,#c4b5fd);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;}
footer p{font-size:14px;color:var(--muted);margin-bottom:6px;font-weight:600;}
.foot-sub{font-size:12px;color:#c0b0e0!important;}
.foot-tech{display:flex;flex-wrap:wrap;gap:8px;justify-content:center;margin-top:24px;}
.foot-tech span{font-size:11px;font-weight:700;background:rgba(124,58,237,.08);border:1px solid rgba(124,58,237,.2);color:var(--lav2);padding:4px 14px;border-radius:100px;}

@media(max-width:900px){
  nav{padding:0 24px;} .nav-links{display:none;}
  .section{padding:60px 24px;} #hero{padding:100px 24px 60px;}
  .cards-3,.steps-row{grid-template-columns:1fr;}
  .demo-layout{grid-template-columns:1fr;}
  footer{padding:48px 24px;}
  .hero-stats{flex-wrap:wrap;}
}


