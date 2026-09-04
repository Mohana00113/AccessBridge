# ============================================================
# train_model.py
# RUN THIS SECOND — extracts landmarks from collected images
# and trains the CNN model, saves to backend/model/sign_model.h5
# ============================================================

import cv2
import mediapipe as mp
import numpy as np
import os
import pickle
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing   import LabelEncoder
from keras.models import Sequential
from keras.layers import Dense, Dropout, BatchNormalization
from keras.utils  import to_categorical
from keras.callbacks import EarlyStopping

# ---- MediaPipe ----
mp_hands = mp.solutions.hands
hands    = mp_hands.Hands(static_image_mode=True, max_num_hands=1)

TRAIN_DIR  = "backend/data/train"
MODEL_DIR  = "backend/model"
GESTURES   = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

os.makedirs(MODEL_DIR, exist_ok=True)

# ============================================================
# STEP 1 — Extract landmarks from images
# ============================================================
print("Extracting hand landmarks from images...")

X, y = [], []

for gesture in GESTURES:
    folder = os.path.join(TRAIN_DIR, gesture)
    if not os.path.exists(folder):
        print(f"  Skipping {gesture} — folder not found")
        continue

    count = 0
    for img_name in os.listdir(folder):
        img_path = os.path.join(folder, img_name)
        img      = cv2.imread(img_path)
        if img is None:
            continue

        rgb    = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        result = hands.process(rgb)

        if result.multi_hand_landmarks:
            lm_list = result.multi_hand_landmarks[0].landmark
            coords  = []
            for lm in lm_list:
                coords += [lm.x, lm.y, lm.z]
            X.append(coords)
            y.append(gesture)
            count += 1

    print(f"  {gesture}: {count} samples")

X = np.array(X)
y = np.array(y)
print(f"\nTotal samples: {len(X)}")

# ============================================================
# STEP 2 — Encode labels and split data
# ============================================================
encoder   = LabelEncoder()
y_encoded = encoder.fit_transform(y)
y_onehot  = to_categorical(y_encoded)

# Save encoder for use in app.py
with open(os.path.join(MODEL_DIR, "encoder.pkl"), "wb") as f:
    pickle.dump(encoder, f)

X_train, X_test, y_train, y_test = train_test_split(
    X, y_onehot, test_size=0.2, random_state=42
)
print(f"Train: {len(X_train)} | Test: {len(X_test)}")

# ============================================================
# STEP 3 — Build and train model
# ============================================================
num_classes = len(encoder.classes_)

model = Sequential([
    Dense(128, activation='relu', input_shape=(63,)),
    BatchNormalization(),
    Dropout(0.3),
    Dense(256, activation='relu'),
    BatchNormalization(),
    Dropout(0.3),
    Dense(128, activation='relu'),
    Dropout(0.2),
    Dense(num_classes, activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.summary()

early_stop = EarlyStopping(monitor='val_accuracy', patience=5, restore_best_weights=True)

print("\nTraining model...")
history = model.fit(
    X_train, y_train,
    epochs=50,
    batch_size=32,
    validation_data=(X_test, y_test),
    callbacks=[early_stop],
    verbose=1
)

# ============================================================
# STEP 4 — Save model and plot results
# ============================================================
model.save(os.path.join(MODEL_DIR, "sign_model.h5"))
print(f"\nModel saved to {MODEL_DIR}/sign_model.h5")

# Final accuracy
loss, acc = model.evaluate(X_test, y_test, verbose=0)
print(f"Test Accuracy: {acc*100:.2f}%")

# Plot
plt.figure(figsize=(12, 4))
plt.subplot(1,2,1)
plt.plot(history.history['accuracy'],     label='Train')
plt.plot(history.history['val_accuracy'], label='Validation')
plt.title('Accuracy'); plt.legend()

plt.subplot(1,2,2)
plt.plot(history.history['loss'],     label='Train')
plt.plot(history.history['val_loss'], label='Validation')
plt.title('Loss'); plt.legend()

plt.tight_layout()
plt.savefig(os.path.join(MODEL_DIR, "training_results.png"))
plt.show()
print("Training graph saved!")