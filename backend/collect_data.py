# ============================================================
# collect_data.py
# RUN THIS FIRST — collects hand gesture images from webcam
# Saves images to backend/data/train/ and backend/data/test/
# ============================================================

import cv2
import os
import mediapipe as mp

# ---- MediaPipe setup ----
mp_hands = mp.solutions.hands
mp_draw  = mp.solutions.drawing_utils
hands    = mp_hands.Hands(static_image_mode=False, max_num_hands=1)

# ---- Settings ----
TRAIN_DIR    = "backend/data/train"
TEST_DIR     = "backend/data/test"
GESTURES     = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
TRAIN_COUNT  = 80   # 80 images per letter for training
TEST_COUNT   = 20   # 20 images per letter for testing

# Create folders
for g in GESTURES:
    os.makedirs(os.path.join(TRAIN_DIR, g), exist_ok=True)
    os.makedirs(os.path.join(TEST_DIR,  g), exist_ok=True)

cap = cv2.VideoCapture(0)

for gesture in GESTURES:
    print(f"\nGet ready for gesture: {gesture}")
    print("Press SPACE to start | Q to quit")

    # Wait for space
    while True:
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        cv2.rectangle(frame, (0,0), (frame.shape[1], 70), (15,20,35), -1)
        cv2.putText(frame, f"Ready: {gesture}  |  Press SPACE to collect",
                    (20, 45), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,229,160), 2)
        cv2.imshow("Collect Data", frame)
        key = cv2.waitKey(1)
        if key == ord(' '): break
        if key == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            exit()

    # Collect training images
    count = 0
    total = TRAIN_COUNT + TEST_COUNT
    while count < total:
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)

        rgb    = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(rgb)
        if result.multi_hand_landmarks:
            for lm in result.multi_hand_landmarks:
                mp_draw.draw_landmarks(frame, lm, mp_hands.HAND_CONNECTIONS)

        cv2.rectangle(frame, (0,0), (frame.shape[1], 70), (15,20,35), -1)
        cv2.putText(frame, f"{gesture}: {count}/{total}",
                    (20, 45), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,229,160), 2)
        cv2.imshow("Collect Data", frame)

        # Save to train or test folder
        if count < TRAIN_COUNT:
            path = os.path.join(TRAIN_DIR, gesture, f"{count}.jpg")
        else:
            path = os.path.join(TEST_DIR, gesture, f"{count - TRAIN_COUNT}.jpg")

        cv2.imwrite(path, frame)
        count += 1
        cv2.waitKey(40)

print("\nData collection complete!")
cap.release()
cv2.destroyAllWindows()