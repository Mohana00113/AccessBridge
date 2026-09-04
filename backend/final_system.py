import cv2
import numpy as np
from tensorflow.keras.models import load_model
import pyttsx3

# Load model
model = load_model("model/sign_model.keras")

# Classes
classes = ['A', 'B', 'C']

# Text-to-speech
engine = pyttsx3.init()

# Camera
cap = cv2.VideoCapture(0)

word = ""
last_letter = ""
count = 0

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    # ROI box
    cv2.rectangle(frame, (100,100), (300,300), (0,255,0), 2)
    roi = frame[100:300, 100:300]

    # Preprocess
    img = cv2.resize(roi, (64,64))
    img = img / 255.0
    img = np.reshape(img, (1,64,64,3))

    # Prediction
    prediction = model.predict(img, verbose=0)
    class_index = np.argmax(prediction)
    confidence = prediction[0][class_index]

    if confidence > 0.8:
        letter = classes[class_index]

        # Stability check (avoid flickering)
        if letter == last_letter:
            count += 1
        else:
            count = 0

        last_letter = letter

        # Add letter if stable for few frames
        if count == 15:
            word += letter
            count = 0

        label = f"{letter} {confidence:.2f}"
    else:
        label = "..."

    # Display
    cv2.putText(frame, label, (100,90),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

    cv2.putText(frame, "Text: " + word, (10,450),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)

    cv2.imshow("Sign System", frame)

    key = cv2.waitKey(1)

    # Speak text
    if key == ord('s'):
        engine.say(word)
        engine.runAndWait()

    # Clear text
    if key == ord('c'):
        word = ""

    # Quit
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()