# ============================================================
# app.py — Flask backend server
# Connects your Python ML model to the website frontend
# Run: python main.py
# API available at: http://localhost:5000
# ============================================================

from flask import Flask, Response, jsonify, request, stream_with_context
from flask_cors import CORS
import cv2
import numpy as np
import collections
from collections import deque, Counter
# Try to import MediaPipe safely; if it fails we continue without hand detection
try:
    import mediapipe as mp
except Exception:
    mp = None
import pickle
import pyttsx3
import threading
import base64
import os
import time
from backend.blind_helpers import ocr_image_to_text, dominant_color_name, capture_frame, get_ocr_reader
import math
import logging
import traceback

try:
    from ultralytics import YOLO
except Exception:
    YOLO = None
    
# Pre-initialize OCR reader to avoid per-request startup latency
try:
    get_ocr_reader(['en'])
except Exception:
    # non-fatal — OCR will be attempted lazily on request
    pass

# Global YOLO model cache
yolo_model = None

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
FRONTEND_DIR = os.path.join(PROJECT_ROOT, 'frontend')

app = Flask(
    __name__,
    static_folder=FRONTEND_DIR,
    static_url_path=''
)
CORS(app)   # allows frontend to talk to backend

# configure simple logging for diagnostics
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')
logger = logging.getLogger(__name__)

# ============================================================
# LOAD MODEL (only if it exists)
# ============================================================
MODEL_PATH   = "backend/model/sign_model.h5"
ENCODER_PATH = "backend/model/encoder.pkl"

model   = None
encoder = None

try:
    # Allow disabling TensorFlow/model loading in environments where
    # TensorFlow / NumPy binaries are incompatible. Set environment
    # variable `DISABLE_TF=1` to force demo mode and avoid importing TF.
    if os.environ.get('DISABLE_TF', '0') == '1':
        print("DISABLE_TF=1 detected — skipping TensorFlow import and running in demo mode")
        model = None
        encoder = None
    elif os.path.exists(MODEL_PATH) and os.path.exists(ENCODER_PATH):
        try:
            from tensorflow.keras.models import load_model
            model = load_model(MODEL_PATH)
            with open(ENCODER_PATH, "rb") as f:
                encoder = pickle.load(f)
            print("Model loaded successfully!")
        except Exception as e:
            print("Failed to load TensorFlow model (continuing in demo mode):", e)
            model = None
            encoder = None
    else:
        print("Model not found — run train_model.py first")
        print("Running in demo mode (simulated predictions)")
except Exception as e:
    print("Unexpected error while checking model files — running in demo mode:", e)
    model = None
    encoder = None

# ============================================================
# MEDIAPIPE SETUP (optional)
# ============================================================
mp_hands = None
mp_draw = None
hands = None
if mp is not None:
    try:
        mp_hands = mp.solutions.hands
        mp_draw  = mp.solutions.drawing_utils
        # Tuned parameters: slightly lower detection confidence for robustness
        hands    = mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            # Lower confidence thresholds to increase sensitivity in poor lighting
            min_detection_confidence=0.3,
            min_tracking_confidence=0.3
        )
    except Exception:
        mp = None
        mp_hands = None
        mp_draw = None
        hands = None

# ============================================================
# TEXT TO SPEECH
# ============================================================
tts_engine = pyttsx3.init()
tts_engine.setProperty('rate', 150)
tts_engine.setProperty('volume', 1.0)

def speak_async(text):
    def _speak():
        tts_engine.say(text)
        tts_engine.runAndWait()
    threading.Thread(target=_speak, daemon=True).start()

# ============================================================
# CAMERA STATE
# ============================================================
camera     = None
is_running = False
current_prediction = {"letter": "", "confidence": 0.0, "hand_detected": False}
# Keep a short history of recent predictions to smooth flicker
pred_history = deque(maxlen=8)

def release_camera():
    global camera
    if camera is not None:
        try:
            camera.release()
        except Exception:
            pass
        camera = None


def get_camera():
    global camera
    if camera is None or not camera.isOpened():
        # Preferred camera configurations (from auto-search results)
        prefs = [
            { 'api': cv2.CAP_DSHOW, 'index': 0, 'exposure': -1, 'brightness': None },
            { 'api': cv2.CAP_ANY,   'index': 0, 'exposure': -1, 'brightness': None },
            { 'api': None,          'index': 0, 'exposure': None, 'brightness': None }
        ]

        cam = None
        for p in prefs:
            try:
                if p['api'] is None:
                    cap = cv2.VideoCapture(p['index'])
                else:
                    cap = cv2.VideoCapture(p['index'], apiPreference=p['api'])
            except TypeError:
                cap = cv2.VideoCapture(p['index'])

            if not cap or not cap.isOpened():
                try:
                    cap.release()
                except Exception:
                    pass
                continue

            # set resolution and give camera a moment to settle
            cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
            cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
            time.sleep(0.25)

            # try to set exposure/brightness if suggested
            try:
                if p.get('exposure') is not None:
                    cap.set(cv2.CAP_PROP_EXPOSURE, float(p['exposure']))
                if p.get('brightness') is not None:
                    cap.set(cv2.CAP_PROP_BRIGHTNESS, float(p['brightness']))
            except Exception:
                pass

            # read one frame to verify
            ok, _ = cap.read()
            if ok:
                cam = cap
                break
            else:
                try:
                    cap.release()
                except Exception:
                    pass

        if cam is None:
            # final fallback
            camera = cv2.VideoCapture(0)
            camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
            camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        else:
            camera = cam

    return camera

def predict_gesture(landmarks):
    """Run model prediction or simulate if model not loaded"""
    if model is not None and encoder is not None:
        coords = []
        for lm in landmarks:
            coords += [lm.x, lm.y, lm.z]
        arr  = np.array(coords).reshape(1, -1)
        pred = model.predict(arr, verbose=0)[0]
        idx  = np.argmax(pred)
        return encoder.classes_[idx], float(pred[idx])
    else:
        # Demo mode — simple heuristic
        lm = landmarks
        thumb  = lm[4]; index = lm[8]; middle = lm[12]
        wrist  = lm[0]; imcp  = lm[5]; mmcp   = lm[9]
        thumbUp  = thumb.y  < wrist.y - 0.15
        indexUp  = index.y  < imcp.y  - 0.05
        middleUp = middle.y < mmcp.y  - 0.05
        allUp    = indexUp and middleUp and lm[16].y < lm[13].y and lm[20].y < lm[17].y
        dist     = lambda a,b: ((a.x-b.x)**2+(a.y-b.y)**2)**0.5
        tIClose  = dist(thumb, index) < 0.06

        if thumbUp and not indexUp:           return "A", 0.91
        if allUp and not thumbUp:             return "B", 0.88
        if indexUp and middleUp and not allUp:return "V", 0.86
        if tIClose and not indexUp:           return "F", 0.84
        if indexUp and not middleUp:          return "D", 0.87
        if thumbUp and indexUp:               return "L", 0.89
        letters = list("CEGHI JKMNOPQRSTUWXYZ")
        idx = int(abs(thumb.x * len(letters))) % len(letters)
        return letters[idx], 0.72

# ============================================================
# VIDEO STREAM
# ============================================================
# Pre-compute gamma LUT once (used for low-light enhancement)
_GAMMA_LUT = (np.array([((i / 255.0) ** 0.5) * 255 for i in range(256)])).astype('uint8')
# Pre-create CLAHE object once
_CLAHE = cv2.createCLAHE(clipLimit=4.0, tileGridSize=(8, 8))

# Target ~15 FPS to keep CPU usage reasonable
_TARGET_FPS = 15
_FRAME_INTERVAL = 1.0 / _TARGET_FPS

def generate_frames():
    global current_prediction
    cam = get_camera()
    frame_count = 0
    logger.info('Starting frame generator')
    last_frame_bytes = None
    last_proc_frame = None            # cache processed frame between prediction frames
    last_frame_time = 0.0             # for FPS throttling
    silhouette_cooldown = 0           # only run silhouette fallback every N frames

    try:
        retry_count = 0
        while True:
            # ── FPS throttle: sleep to maintain ~15 FPS ──
            now = time.time()
            elapsed = now - last_frame_time
            if elapsed < _FRAME_INTERVAL:
                time.sleep(_FRAME_INTERVAL - elapsed)
            last_frame_time = time.time()

            try:
                success, frame = cam.read()
            except Exception as e:
                logger.error('Camera read failed: %s', e)
                logger.debug(traceback.format_exc())
                success, frame = False, None
            if not success or frame is None:
                retry_count += 1
                logger.warning('Camera read failed (retry #%d)', retry_count)
                if retry_count > 5:
                    # avoid terminating generator — yield last known good frame (if available)
                    if last_frame_bytes is not None:
                        try:
                            yield (b'--frame\r\n'
                                   b'Content-Type: image/jpeg\r\n\r\n' + last_frame_bytes + b'\r\n')
                        except Exception:
                            logger.debug('Failed to yield last_frame_bytes during camera retry')
                    time.sleep(0.5)
                    cam = get_camera()
                    continue
                time.sleep(0.1)
                cam = get_camera()
                continue

            retry_count = 0
            frame_count += 1
            frame = cv2.flip(frame, 1)
            # Ensure frame is max 640x480 even if camera ignores our setting
            h_f, w_f = frame.shape[:2]
            if w_f > 640 or h_f > 480:
                frame = cv2.resize(frame, (640, 480))

            # ── Image preprocessing: only run on every 3rd frame to save CPU ──
            do_preprocess = (frame_count % 3 == 1) or last_proc_frame is None
            if do_preprocess:
                try:
                    img = cv2.convertScaleAbs(frame, alpha=1.2, beta=15)
                    yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
                    yuv[:, :, 0] = cv2.equalizeHist(yuv[:, :, 0])
                    proc_frame = cv2.cvtColor(yuv, cv2.COLOR_YUV2BGR)
                    # If frame still very dark, apply CLAHE + gamma correction
                    try:
                        gray = cv2.cvtColor(proc_frame, cv2.COLOR_BGR2GRAY)
                        mean_val = gray.mean()
                        if mean_val < 60:
                            yuv[:, :, 0] = _CLAHE.apply(yuv[:, :, 0])
                            proc_frame = cv2.cvtColor(yuv, cv2.COLOR_YUV2BGR)
                            proc_frame = cv2.LUT(proc_frame, _GAMMA_LUT)
                    except Exception:
                        pass
                    last_proc_frame = proc_frame
                except Exception:
                    proc_frame = frame
                    last_proc_frame = proc_frame
            else:
                proc_frame = last_proc_frame if last_proc_frame is not None else frame

            # If MediaPipe is available, attempt hand detection; otherwise show placeholder
            if hands is not None:
                try:
                    rgb = cv2.cvtColor(proc_frame, cv2.COLOR_BGR2RGB)
                    result = hands.process(rgb)
                    if result and getattr(result, 'multi_hand_landmarks', None):
                        for lm in result.multi_hand_landmarks:
                            mp_draw.draw_landmarks(
                                frame, lm, mp_hands.HAND_CONNECTIONS,
                                mp_draw.DrawingSpec(color=(0, 229, 160), thickness=2, circle_radius=4),
                                mp_draw.DrawingSpec(color=(255, 255, 255), thickness=2)
                            )
                        lm_list = result.multi_hand_landmarks[0].landmark
                        letter, conf = predict_gesture(lm_list)
                        # Add to prediction history and compute majority vote
                        pred_history.append(letter or "")
                        try:
                            most_common = Counter(pred_history).most_common(1)[0][0]
                        except Exception:
                            most_common = letter
                        avg_conf = float(conf)
                        current_prediction = {"letter": most_common, "confidence": round(avg_conf, 2), "hand_detected": True}
                        cv2.rectangle(frame, (0, 0), (frame.shape[1], 65), (15, 20, 35), -1)
                        cv2.putText(frame, f"{current_prediction['letter']}  {int(avg_conf * 100)}%",
                                    (20, 45), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 229, 160), 3)
                        silhouette_cooldown = 0  # reset cooldown when MP succeeds
                    else:
                        # No MediaPipe landmarks — try silhouette fallback only every 5th frame
                        silhouette_cooldown += 1
                        if silhouette_cooldown >= 5:
                            silhouette_cooldown = 0
                            hand_detected = False
                            try:
                                gray_s = cv2.cvtColor(proc_frame, cv2.COLOR_BGR2GRAY)
                                blur = cv2.GaussianBlur(gray_s, (7, 7), 0)
                                th = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                                           cv2.THRESH_BINARY_INV, 11, 2)
                                kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
                                th = cv2.morphologyEx(th, cv2.MORPH_OPEN, kernel, iterations=1)

                                contours, _ = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                                if contours:
                                    largest = max(contours, key=cv2.contourArea)
                                    area = cv2.contourArea(largest)
                                    h, w = gray_s.shape
                                    if area > (w * h) * 0.01:
                                        hull = cv2.convexHull(largest, returnPoints=False)
                                        finger_count = 0
                                        if hull is not None and len(hull) > 3:
                                            defects = cv2.convexityDefects(largest, hull)
                                            if defects is not None:
                                                cnt = 0
                                                for i in range(defects.shape[0]):
                                                    s, e, f, d = defects[i, 0]
                                                    start = tuple(largest[s][0])
                                                    end = tuple(largest[e][0])
                                                    far = tuple(largest[f][0])
                                                    a = np.linalg.norm(np.array(start) - np.array(end))
                                                    b = np.linalg.norm(np.array(start) - np.array(far))
                                                    c = np.linalg.norm(np.array(end) - np.array(far))
                                                    if b * c == 0:
                                                        continue
                                                    angle = np.arccos(max(-1.0, min(1.0, (b * b + c * c - a * a) / (2 * b * c))))
                                                    if d > 1000 and angle < (np.pi * 0.9 / 2):
                                                        cnt += 1
                                                finger_count = cnt

                                        fingers = 0
                                        if finger_count > 0:
                                            fingers = min(5, finger_count + 1)
                                        else:
                                            x, y, ww, hh = cv2.boundingRect(largest)
                                            ar = ww / float(hh) if hh > 0 else 0
                                            if area > (w * h) * 0.15 and ar > 0.6:
                                                fingers = 5

                                        x, y, ww, hh = cv2.boundingRect(largest)
                                        cv2.rectangle(frame, (x, y), (x + ww, y + hh), (0, 180, 220), 2)

                                        if fingers >= 4:
                                            letter, conf = "B", 0.75
                                        elif fingers == 3:
                                            letter, conf = "W", 0.6
                                        elif fingers == 2:
                                            letter, conf = "V", 0.7
                                        elif fingers == 1:
                                            letter, conf = "D", 0.6
                                        else:
                                            letter, conf = "S", 0.65

                                        cv2.putText(frame, f"{letter} {int(conf * 100)}%",
                                                    (x, max(20, y - 6)), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 180, 220), 2)
                                        hand_detected = True
                            except Exception:
                                hand_detected = False

                            if hand_detected:
                                letter = ""
                                conf = 0.5
                                try:
                                    pts = largest.reshape(-1, 2)
                                    cx = float(pts[:, 0].mean())
                                    cy = float(pts[:, 1].mean())
                                    dists = np.sqrt((pts[:, 0] - cx) ** 2 + (pts[:, 1] - cy) ** 2)
                                    if dists.size > 0:
                                        maxd = float(dists.max())
                                        peaks = []
                                        for i, (x, y) in enumerate(pts):
                                            if dists[i] > 0.6 * maxd and y < cy:
                                                angle = math.atan2(y - cy, x - cx)
                                                if not any(abs(((angle - a + math.pi) % (2 * math.pi) - math.pi)) < 0.4 for a in peaks):
                                                    peaks.append(angle)
                                        finger_count = len(peaks)
                                    else:
                                        finger_count = 0

                                    if finger_count >= 4:
                                        letter, conf = "B", 0.75
                                    elif finger_count == 3:
                                        letter, conf = "W", 0.6
                                    elif finger_count == 2:
                                        letter, conf = "V", 0.7
                                    elif finger_count == 1:
                                        letter, conf = "D", 0.6
                                    else:
                                        letter, conf = "S", 0.65
                                except Exception:
                                    letter = ""
                                    conf = 0.5

                                current_prediction = {"letter": letter, "confidence": round(conf, 2), "hand_detected": True}
                                cv2.rectangle(frame, (0, 0), (frame.shape[1], 65), (15, 20, 35), -1)
                                text = f"{letter} {int(conf * 100)}%" if letter else "Hand silhouette"
                                cv2.putText(frame, text,
                                            (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 180, 220), 2)
                            else:
                                current_prediction = {"letter": "", "confidence": 0.0, "hand_detected": False}
                                cv2.rectangle(frame, (0, 0), (frame.shape[1], 65), (15, 20, 35), -1)
                                cv2.putText(frame, "Show your hand...",
                                            (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (100, 100, 100), 2)
                        else:
                            # Between silhouette checks, just show "Show your hand..." overlay
                            current_prediction = {"letter": "", "confidence": 0.0, "hand_detected": False}
                            cv2.rectangle(frame, (0, 0), (frame.shape[1], 65), (15, 20, 35), -1)
                            cv2.putText(frame, "Show your hand...",
                                        (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (100, 100, 100), 2)
                except Exception:
                    current_prediction = {"letter": "", "confidence": 0.0, "hand_detected": False}
                    cv2.rectangle(frame, (0, 0), (frame.shape[1], 65), (15, 20, 35), -1)
                    cv2.putText(frame, "Hand detection unavailable.",
                                (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (200, 100, 100), 2)
            else:
                current_prediction = {"letter": "", "confidence": 0.0, "hand_detected": False}
                cv2.rectangle(frame, (0, 0), (frame.shape[1], 65), (15, 20, 35), -1)
                cv2.putText(frame, "Hand detection disabled (optional dependency missing).",
                            (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (180, 180, 180), 2)

            # ── Encode frame as JPEG and yield ──
            try:
                _, buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 75])
                frame_bytes = buffer.tobytes()
                last_frame_bytes = frame_bytes
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')
            except Exception as e:
                logger.error('Failed to encode or yield frame #%d: %s', frame_count, e)
                logger.debug(traceback.format_exc())
                if last_frame_bytes is not None:
                    try:
                        yield (b'--frame\r\n'
                               b'Content-Type: image/jpeg\r\n\r\n' + last_frame_bytes + b'\r\n')
                        logger.info('Yielded cached frame as fallback for frame #%d', frame_count)
                    except Exception:
                        logger.debug('Failed to yield cached fallback frame')
                continue

            # occasional heartbeat to diagnose silent stalls (every 150 frames)
            if frame_count % 150 == 0:
                logger.info('Yielded frame #%d', frame_count)
    finally:
        release_camera()

# ============================================================
# API ROUTES
# ============================================================

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/video_feed')
def video_feed():
    """Live camera stream with hand landmarks drawn on it"""
    return Response(stream_with_context(generate_frames()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/predict')
def predict():
    """Returns the current gesture prediction as JSON"""
    return jsonify(current_prediction)

@app.route('/release_camera', methods=['POST'])
def release_camera_route():
    """Release the camera resource when the frontend stops streaming."""
    release_camera()
    return jsonify({"status": "released"})

@app.route('/speak', methods=['POST'])
def speak():
    """Speaks the given text using TTS"""
    data = request.get_json()
    text = data.get('text', '')
    if text:
        speak_async(text)
        return jsonify({"status": "speaking", "text": text})
    return jsonify({"status": "error", "message": "No text provided"}), 400

@app.route('/status')
def status():
    """Returns server and model status"""
    return jsonify({
        "server": "running",
        "model_loaded": model is not None,
        "camera_open": camera is not None and camera.isOpened()
    })


def _capture_one_frame() -> (bool, object):
    # Use helper with a short timeout to avoid blocking if camera is unavailable
    ok, frame = capture_frame(camera_index=0, timeout=3.0)
    if not ok or frame is None:
        return False, None
    return True, frame


@app.route('/blind/medicine', methods=['GET'])
def blind_medicine():
    ok, frame = _capture_one_frame()
    if not ok:
        speak_async("Unable to access camera for medicine reader.")
        return jsonify({"ok": False, "message": "Camera unavailable", "data": None}), 500
    text = ocr_image_to_text(frame)
    if not text:
        speak_async("No readable text detected on the medicine box. Please try again.")
        return jsonify({"ok": False, "message": "No readable text detected", "data": {"text": ""}})
    speak_async("Detected the following text on the medicine.")
    speak_async(text)
    return jsonify({"ok": True, "message": "Text detected", "data": {"text": text}})


@app.route('/blind/color', methods=['GET'])
def blind_color():
    ok, frame = _capture_one_frame()
    if not ok:
        speak_async("Unable to access camera for color detection.")
        return jsonify({"ok": False, "message": "Camera unavailable", "data": None}), 500
    name, bgr = dominant_color_name(frame)
    speak_async(f"Detected color: {name}")
    return jsonify({"ok": True, "message": f"Detected color {name}", "data": {"color": name, "bgr": bgr}})


@app.route('/blind/currency', methods=['GET'])
def blind_currency():
    ok, frame = _capture_one_frame()
    if not ok:
        speak_async("Unable to access camera for currency recognition.")
        return jsonify({"ok": False, "message": "Camera unavailable", "data": None}), 500
    text = ocr_image_to_text(frame)
    if not text:
        speak_async("No text detected on the note. Please try again.")
        return jsonify({"ok": False, "message": "No text detected", "data": {"text": "", "denomination": None}})
    detected = None
    for denom in ["2000","500","200","100","50","20","10"]:
        if denom in text.replace(' ', ''):
            detected = denom
            break
    word_map = {"five hundred":"500", "two hundred":"200", "one hundred":"100", "fifty":"50", "twenty":"20", "ten":"10"}
    if detected is None:
        low = text.lower()
        for k,v in word_map.items():
            if k in low:
                detected = v
                break
    if detected:
        speak_async(f"Detected currency denomination: rupees {detected}")
        return jsonify({"ok": True, "message": f"Detected denomination {detected}", "data": {"text": text, "denomination": detected}})
    else:
        speak_async("Could not confidently detect denomination.")
        return jsonify({"ok": False, "message": "Could not detect denomination", "data": {"text": text, "denomination": None}})


@app.route('/blind/read', methods=['GET'])
def blind_read():
    ok, frame = _capture_one_frame()
    if not ok:
        speak_async("Unable to capture image for text reader.")
        return jsonify({"ok": False, "message": "Camera unavailable", "data": None}), 500
    text = ocr_image_to_text(frame)
    if not text:
        speak_async("No readable text found. Please try again.")
        return jsonify({"ok": False, "message": "No readable text found", "data": {"text": ""}})
    speak_async("Reading detected text now.")
    speak_async(text)
    return jsonify({"ok": True, "message": "Text read", "data": {"text": text}})


@app.route('/blind/objects', methods=['GET'])
def blind_objects():
    ok, frame = _capture_one_frame()
    if not ok:
        speak_async("Unable to access camera for object detection.")
        return jsonify({"ok": False, "message": "Camera unavailable", "data": None}), 500
    if YOLO is None:
        speak_async("Object detection not available; ultralytics not installed.")
        return jsonify({"ok": False, "message": "YOLO not available", "data": None}), 500
    try:
        global yolo_model
        if yolo_model is None:
            try:
                yolo_model = YOLO('yolov8n.pt')
            except Exception as e:
                speak_async("Failed to load YOLO model.")
                return jsonify({"ok": False, "message": "Failed to load YOLO model", "data": {"error": str(e)}}), 500
        results = yolo_model(frame)[0]
        names = results.names if hasattr(results, 'names') else None
        detected = []
        for box in results.boxes:
            cls = int(box.cls[0]) if hasattr(box, 'cls') else None
            if cls is not None and names is not None and cls < len(names):
                detected.append(names[cls])
        common = ["person", "chair", "bottle", "laptop", "book", "table", "door", "cell phone", "phone", "mobile"]
        announced = set()
        for d in detected:
            dn = d.lower()
            for c in common:
                if c in dn or dn in c:
                    announced.add(c)
        if announced:
            for obj in announced:
                speak_async(f"Detected: {obj}")
            return jsonify({"ok": True, "message": "Objects detected", "data": {"detected": list(announced)}})
        else:
            speak_async("No common objects detected.")
            return jsonify({"ok": False, "message": "No common objects detected", "data": {"detected": detected}})
    except Exception as e:
        speak_async("Object detection failed.")
        return jsonify({"ok": False, "message": "Object detection failed", "data": {"error": str(e)}}), 500


@app.route('/blind/shopping', methods=['GET'])
def blind_shopping():
    """Shopping Assistant: identify products and read labels/prices.

    Returns detected product classes (if YOLO available) and OCR-extracted text and prices.
    """
    ok, frame = _capture_one_frame()
    if not ok:
        speak_async("Unable to access camera for shopping assistant.")
        return jsonify({"ok": False, "message": "Camera unavailable", "data": None}), 500

    # Run OCR
    text = ocr_image_to_text(frame)
    prices = []
    try:
        from backend.blind_helpers import extract_prices
        prices = extract_prices(text)
    except Exception:
        prices = []

    detected_products = []
    if YOLO is not None:
        try:
            global yolo_model
            if yolo_model is None:
                yolo_model = YOLO('yolov8n.pt')
            results = yolo_model(frame)[0]
            names = results.names if hasattr(results, 'names') else None
            for box in results.boxes:
                cls = int(box.cls[0]) if hasattr(box, 'cls') else None
                if cls is not None and names is not None and cls < len(names):
                    detected_products.append(names[cls])
        except Exception as e:
            # fail gracefully — keep detected_products empty
            detected_products = []

    # Announce summary
    if detected_products:
        speak_async("Detected products: " + ", ".join(detected_products[:5]))
    if prices:
        speak_async("Detected prices: " + ", ".join(prices[:5]))
    elif text:
        # speak a short snippet of text if no prices
        speak_async("Detected label text: " + (text[:150] + '...' if len(text) > 150 else text))

    return jsonify({
        "ok": True,
        "message": "Shopping assistant results",
        "data": {
            "products": detected_products,
            "prices": prices,
            "text": text
        }
    })


@app.route('/debug/camera_info', methods=['GET'])
def debug_camera_info():
    """Attempt to open camera with multiple backends and indices, save samples, and report mean brightness.

    Useful when frames are unexpectedly dark or camera behaves oddly on Windows.
    """
    results = []
    backends = [cv2.CAP_DSHOW, cv2.CAP_MSMF, cv2.CAP_ANY]
    for b in backends:
        for idx in range(0, 3):
            try:
                cap = cv2.VideoCapture(idx, apiPreference=b)
            except TypeError:
                # Older OpenCV may not accept apiPreference kwarg
                cap = cv2.VideoCapture(idx)
            if not cap.isOpened():
                results.append({"backend": int(b), "index": idx, "ok": False, "mean": None, "file": None})
                try:
                    cap.release()
                except Exception:
                    pass
                continue
            # try to warm up
            cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
            cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
            time_sleep = 0.35
            try:
                import time
                time.sleep(time_sleep)
            except Exception:
                pass
            ok, frame = cap.read()
            if not ok or frame is None:
                results.append({"backend": int(b), "index": idx, "ok": False, "mean": None, "file": None})
                try:
                    cap.release()
                except Exception:
                    pass
                continue
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            mean = float(gray.mean())
            fname = f'backend/tests/debug_backend{int(b)}_idx{idx}_mean{int(mean)}.jpg'
            try:
                cv2.imwrite(fname, frame)
            except Exception:
                fname = None
            results.append({"backend": int(b), "index": idx, "ok": True, "mean": mean, "file": fname})
            try:
                cap.release()
            except Exception:
                pass

    return jsonify({"ok": True, "message": "camera debug results", "data": results})


@app.route('/debug/calibrate', methods=['GET'])
def debug_calibrate():
    """Capture one frame, apply aggressive enhancement (CLAHE + gamma),
    return a base64-encoded preview and mean brightness so frontend can show it.
    """
    ok, frame = _capture_one_frame()
    if not ok or frame is None:
        return jsonify({"ok": False, "message": "Camera unavailable", "data": None}), 500

    try:
        # Convert to YUV and apply CLAHE on Y channel
        yuv = cv2.cvtColor(frame, cv2.COLOR_BGR2YUV)
        clahe = cv2.createCLAHE(clipLimit=4.0, tileGridSize=(8,8))
        yuv[:,:,0] = clahe.apply(yuv[:,:,0])
        enhanced = cv2.cvtColor(yuv, cv2.COLOR_YUV2BGR)
        # Stronger gamma correction to brighten
        inv_gamma = 0.4
        table = (np.array([((i / 255.0) ** inv_gamma) * 255 for i in range(256)])).astype('uint8')
        enhanced = cv2.LUT(enhanced, table)

        gray = cv2.cvtColor(enhanced, cv2.COLOR_BGR2GRAY)
        mean = float(gray.mean())

        _, buf = cv2.imencode('.jpg', enhanced, [cv2.IMWRITE_JPEG_QUALITY, 85])
        img_b64 = base64.b64encode(buf.tobytes()).decode('ascii')

        return jsonify({"ok": True, "message": "Calibration image", "data": {"mean": mean, "image": img_b64}})
    except Exception as e:
        return jsonify({"ok": False, "message": f"Calibration failed: {e}", "data": None}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)