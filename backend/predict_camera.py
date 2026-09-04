# ============================================================
# predict_camera.py
# Standalone live prediction — run this to test your model
# without the full app. Good for quick testing.
# ============================================================

import cv2
import mediapipe as mp
import numpy as np
import pickle
import pyttsx3
import threading
from tensorflow.keras.models import load_model

# ---- Load model ----
model   = load_model("backend/model/sign_model.h5")
with open("backend/model/encoder.pkl", "rb") as f:
    encoder = pickle.load(f)

# ---- MediaPipe ----
mp_hands = mp.solutions.hands
mp_draw  = mp.solutions.drawing_utils
hands    = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)

# ---- TTS ----
tts = pyttsx3.init()
tts.setProperty('rate', 150)

def speak(text):
    threading.Thread(target=lambda: (tts.say(text), tts.runAndWait()), daemon=True).start()

# ---- Colors ----
GREEN = (0, 229, 160)
WHITE = (255, 255, 255)
DARK  = (15, 20, 35)

built_word = ""
cap = cv2.VideoCapture(0)

print("predict_camera.py running")
print("SPACE = add letter | ENTER = speak word | C = clear | Q = quit")

while True:
    ret, frame = cap.read()
    if not ret: break
    frame = cv2.flip(frame, 1)
    rgb   = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    predicted = ""
    confidence = 0.0

    if result.multi_hand_landmarks:
        for lm in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, lm, mp_hands.HAND_CONNECTIONS,
                mp_draw.DrawingSpec(color=GREEN, thickness=2, circle_radius=3),
                mp_draw.DrawingSpec(color=WHITE, thickness=1))

        lm_list = result.multi_hand_landmarks[0].landmark
        coords  = []
        for lm in lm_list:
            coords += [lm.x, lm.y, lm.z]

        coords = np.array(coords).reshape(1, -1)
        pred   = model.predict(coords, verbose=0)[0]
        idx    = np.argmax(pred)
        predicted  = encoder.classes_[idx]
        confidence = float(pred[idx])

    # UI
    cv2.rectangle(frame, (0,0), (frame.shape[1], 75), DARK, -1)
    cv2.putText(frame, f"Letter: {predicted}  ({int(confidence*100)}%)",
                (20, 35), cv2.FONT_HERSHEY_SIMPLEX, 1, GREEN, 2)
    cv2.putText(frame, f"Word: {built_word}",
                (20, 65), cv2.FONT_HERSHEY_SIMPLEX, 0.7, WHITE, 1)
    cv2.putText(frame, "SPACE=add  ENTER=speak  C=clear  Q=quit",
                (20, frame.shape[0]-15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (100,100,100), 1)

    cv2.imshow("SignBridge — Predict", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'): break
    elif key == ord(' ') and predicted and confidence > 0.6:
        built_word += predicted
        speak(predicted)
    elif key == 13 and built_word:
        speak(built_word)
    elif key == ord('c'):
        built_word = ""

cap.release()
cv2.destroyAllWindows()