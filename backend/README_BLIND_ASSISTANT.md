# Blind Assistance Module

This module provides accessible helpers for visually impaired users: medicine reader,
color detector, currency recognition, smart text reader, and object detection.

Files added
- `backend/blind_helpers.py` — OCR, TTS, webcam capture, color utilities.
- `backend/blind_assistant.py` — CLI entrypoint that runs each feature.

Installation

1. Activate your project virtual environment (example for PowerShell):

```powershell
& .\venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

Notes: `torch` installation may vary by platform/GPU. If `pip install -r requirements.txt`
fails for `torch`, follow the instructions at https://pytorch.org/ to install a compatible
wheel for your system, then re-run `pip install -r requirements.txt`.

Basic usage

Run the CLI from the repository root. Each command captures a single frame from the
default camera (or the camera index you provide) and speaks results via `pyttsx3`.

Examples:

```powershell
python backend/blind_assistant.py medicine --camera 0
python backend/blind_assistant.py color --camera 0
python backend/blind_assistant.py currency --camera 0
python backend/blind_assistant.py read --camera 0
python backend/blind_assistant.py objects --camera 0
```

Features details

- Medicine Reader: captures an image, runs EasyOCR, and speaks detected text.
- Color Detector: captures an image, estimates the dominant color and announces it.
- Currency Recognition: captures an image, runs OCR and heuristically searches for
  denominations (e.g., 500, 200, 100, 50, 20, 10) or common words like "five hundred".
- Smart Text Reader: captures an image and reads long text blocks aloud.
- Object Detection Assistant: uses YOLOv8 (`ultralytics`) to detect objects and announce
  common items like person, chair, bottle, laptop, book, table, door, mobile phone.

YOLO model notes

- `ultralytics` will try to download a default model (e.g., `yolov8n.pt`) automatically when
  first used. You can place a specific model file in the project root and edit
  `backend/blind_assistant.py` if you want to point to a custom model path.
- For better accuracy, use larger YOLOv8 models (at the cost of performance).

Troubleshooting

- Camera errors: ensure no other application is using the webcam and that your OS
  permissions allow camera access. Try changing `--camera` index (0, 1, ...).
- EasyOCR slow or missing languages: EasyOCR downloads language data on first run.
- TTS silent: `pyttsx3` uses local speech drivers; verify system audio works. If TTS fails,
  the helpers will print detected text as a fallback.
- Performance: running YOLO on CPU can be slow. For realtime/object-heavy tasks,
  consider a machine with a supported GPU and install the appropriate `torch` build.

Integration notes

- The Blind Assistance Module is modular and does not modify existing Sign Language
  Recognition code. You can call `python backend/blind_assistant.py <mode>` independently
  or integrate its functions into other parts of the project.

Security & Privacy

- All processing is local (EasyOCR + pyttsx3 + YOLO); no external cloud services are used.

If you want, I can:
- Add a short entry to the repo `README.md` linking to this file.
- Add unit/smoke tests for helper functions.
