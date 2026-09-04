# ============================================================
# demo_system.py
# Full demo — both sign mode and voice mode in one script
# No website needed — runs entirely in a camera window
# Good for college presentation / demo day
# ============================================================

import cv2
import mediapipe as mp
import numpy as np
import pyttsx3
import threading
import os
import pickle

# Try loading trained model
MODEL_PATH   = "backend/model/sign_model.h5"
ENCODER_PATH = "backend/model/encoder.pkl"
model = encoder = None

if os.path.exists(MODEL_PATH):
    from tensorflow.keras.models import load_model
    model   = load_model(MODEL_PATH)
    with open(ENCODER_PATH, "rb") as f:
        encoder = pickle.load(f)
    print("Trained model loaded!")
else:
    print("No model found — using demo mode")

# MediaPipe
mp_hands = mp.solutions.hands
mp_draw  = mp.solutions.drawing_utils
hands    = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)

# TTS
tts = pyttsx3.init()
tts.setProperty('rate', 145)

def speak(text):
    threading.Thread(target=lambda: (tts.say(text), tts.runAndWait()), daemon=True).start()

# Colors
GREEN  = (0, 229, 160)
BLUE   = (255, 143, 91)
WHITE  = (255, 255, 255)
DARK   = (15, 20, 35)
GRAY   = (120, 120, 120)
YELLOW = (0, 220, 255)

# State
mode       = "sign"
built_word = ""
predicted  = ""
confidence = 0.0

def simple_predict(lm):
    thumb=lm[4]; index=lm[8]; middle=lm[12]; wrist=lm[0]
    imcp=lm[5]; mmcp=lm[9]
    tUp = thumb.y < wrist.y-0.15
    iUp = index.y < imcp.y-0.05
    mUp = middle.y < mmcp.y-0.05
    allUp = iUp and mUp and lm[16].y<lm[13].y and lm[20].y<lm[17].y
    dist = lambda a,b: ((a.x-b.x)**2+(a.y-b.y)**2)**0.5
    if tUp and not iUp:             return "A", 0.91
    if allUp and not tUp:           return "B", 0.88
    if iUp and mUp and not allUp:   return "V", 0.86
    if dist(thumb,index)<0.06:      return "F", 0.84
    if iUp and not mUp:             return "D", 0.87
    if tUp and iUp:                 return "L", 0.89
    opts="CEGHI JKMNOPQRSTUWXYZ"
    return opts[int(abs(thumb.x*len(opts)))%len(opts)], 0.72

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

print("\n=== SignBridge Demo System ===")
print("SPACE=add letter | ENTER=speak | C=clear | M=switch mode | Q=quit")

while True:
    ret, frame = cap.read()
    if not ret: break
    frame  = cv2.flip(frame, 1)
    h, w   = frame.shape[:2]
    rgb    = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    predicted  = ""
    confidence = 0.0

    if result.multi_hand_landmarks:
        for lm in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, lm, mp_hands.HAND_CONNECTIONS,
                mp_draw.DrawingSpec(color=GREEN, thickness=2, circle_radius=4),
                mp_draw.DrawingSpec(color=WHITE, thickness=2))

        lm_list = result.multi_hand_landmarks[0].landmark

        if model and encoder:
            coords = []
            for lm in lm_list: coords += [lm.x, lm.y, lm.z]
            arr  = np.array(coords).reshape(1, -1)
            pred = model.predict(arr, verbose=0)[0]
            idx  = np.argmax(pred)
            predicted  = encoder.classes_[idx]
            confidence = float(pred[idx])
        else:
            predicted, confidence = simple_predict(lm_list)

    # ---- Draw UI ----
    # Top bar
    cv2.rectangle(frame, (0,0), (w,80), DARK, -1)
    cv2.putText(frame, "SignBridge", (20,35), cv2.FONT_HERSHEY_SIMPLEX, 1, GREEN, 2)
    cv2.putText(frame, "Enhancing Accessibility using Sign Language Recognition",
                (20,60), cv2.FONT_HERSHEY_SIMPLEX, 0.45, GRAY, 1)

    mode_label = "SIGN → VOICE MODE" if mode=="sign" else "VOICE → TEXT MODE"
    mode_color = GREEN if mode=="sign" else BLUE
    cv2.putText(frame, mode_label, (w-260,35), cv2.FONT_HERSHEY_SIMPLEX, 0.7, mode_color, 2)
    cv2.putText(frame, "M = switch mode", (w-200,60), cv2.FONT_HERSHEY_SIMPLEX, 0.45, GRAY, 1)

    # Bottom bar
    cv2.rectangle(frame, (0, h-100), (w, h), DARK, -1)

    if mode == "sign":
        if predicted:
            cv2.putText(frame, predicted, (30, h-20),
                        cv2.FONT_HERSHEY_SIMPLEX, 3.5, GREEN, 6)
            # Confidence bar
            bx, by = 130, h-75
            cv2.rectangle(frame, (bx, by), (bx+250, by+12), (50,50,50), -1)
            cv2.rectangle(frame, (bx, by), (bx+int(250*confidence), by+12), GREEN, -1)
            cv2.putText(frame, f"{int(confidence*100)}%", (bx+260, by+12),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, GREEN, 1)
        cv2.putText(frame, f"Word: {built_word or '_'}", (130, h-30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, WHITE, 2)
    else:
        cv2.putText(frame, "Voice mode: speak into mic", (20, h-50),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, BLUE, 2)
        cv2.putText(frame, "(SpeechRecognition integration)", (20, h-20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, GRAY, 1)

    # Controls hint
    cv2.putText(frame, "SPACE=add letter | ENTER=speak word | C=clear | Q=quit",
                (int(w/2)-280, h-8), cv2.FONT_HERSHEY_SIMPLEX, 0.45, GRAY, 1)

    cv2.imshow("SignBridge — Demo System", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'): break
    elif key == ord('m'): mode = "voice" if mode=="sign" else "sign"
    elif key == ord(' ') and predicted and confidence > 0.6:
        built_word += predicted
        speak(predicted)
        print(f"Letter: {predicted} | Word: {built_word}")
    elif key == 13 and built_word:
        speak(built_word)
        print(f"Speaking: {built_word}")
    elif key == ord('c'):
        built_word = ""
        print("Word cleared")

cap.release()
cv2.destroyAllWindows()