"""Blind Assistance Module

Features:
- Medicine Reader
- Color Detector
- Currency Recognition
- Smart Text Reader
- Object Detection Assistant

Uses OpenCV, EasyOCR, pyttsx3 and YOLOv8 (ultralytics). This module is modular
and intentionally does not modify the existing Sign Language code.
"""
import argparse
import time
import cv2
from typing import List

from backend.blind_helpers import (
    capture_frame,
    ocr_image_to_text,
    speak,
    dominant_color_name,
)

try:
    from ultralytics import YOLO
except Exception:
    YOLO = None


def medicine_reader(camera_index: int = 0):
    ok, frame = capture_frame(camera_index)
    if not ok:
        speak("Unable to access camera for medicine reader.")
        return
    text = ocr_image_to_text(frame)
    if not text:
        speak("No readable text detected on the medicine box. Please try again.")
        return
    speak("Detected the following text on the medicine:")
    speak(text)


def color_detector(camera_index: int = 0):
    ok, frame = capture_frame(camera_index)
    if not ok:
        speak("Unable to access camera for color detection.")
        return
    name, bgr = dominant_color_name(frame)
    speak(f"Detected color: {name}")


def currency_recognition(camera_index: int = 0, languages: List[str] = ["en"]):
    ok, frame = capture_frame(camera_index)
    if not ok:
        speak("Unable to access camera for currency recognition.")
        return
    text = ocr_image_to_text(frame, languages=languages)
    if not text:
        speak("No text detected on the note. Please try again.")
        return
    # Look for numeric denominations in OCR text
    detected = None
    for denom in ["2000","500","200","100","50","20","10"]:
        if denom in text.replace(' ', ''):
            detected = denom
            break
    # Many Indian notes print the denomination in words; also check for common tokens
    word_map = {"five hundred":"500", "two hundred":"200", "one hundred":"100", "fifty":"50", "twenty":"20", "ten":"10"}
    if detected is None:
        low = text.lower()
        for k,v in word_map.items():
            if k in low:
                detected = v
                break
    if detected:
        speak(f"Detected currency denomination: rupees {detected}")
    else:
        speak("Could not confidently detect denomination. Detected text is:")
        speak(text)


def smart_text_reader(camera_index: int = 0, languages: List[str] = ["en"]):
    speak("Capturing image for text reading. Please hold document in front of the camera.")
    ok, frame = capture_frame(camera_index, timeout=8.0)
    if not ok:
        speak("Unable to capture image for text reader.")
        return
    text = ocr_image_to_text(frame, languages=languages)
    if not text:
        speak("No readable text found. Please try again.")
        return
    speak("Reading detected text now.")
    speak(text)


def object_detection_assistant(camera_index: int = 0, model_name: str = "yolov8n.pt"):
    if YOLO is None:
        speak("Object detection is not available because the ultralytics package is not installed.")
        return
    speak("Starting object detection. Hold object in front of camera.")
    ok, frame = capture_frame(camera_index)
    if not ok:
        speak("Unable to access camera for object detection.")
        return
    try:
        model = YOLO(model_name)
        results = model(frame)[0]
        names = results.names if hasattr(results, 'names') else None
        detected = []
        for box in results.boxes:
            cls = int(box.cls[0]) if hasattr(box, 'cls') else None
            if cls is not None and names is not None and cls < len(names):
                detected.append(names[cls])
        # Filter for requested common objects
        common = ["person", "chair", "bottle", "laptop", "book", "table", "cell phone", "mobile", "door"]
        announced = set()
        for d in detected:
            dn = d.lower()
            for c in common:
                if c in dn or dn in c:
                    announced.add(c)
        if announced:
            for obj in announced:
                speak(f"Detected: {obj}")
        else:
            speak("No common objects detected. Detected classes: " + ", ".join(detected[:10]))
    except Exception as e:
        speak("Object detection failed: " + str(e))


def main():
    parser = argparse.ArgumentParser(description='Blind Assistance Module')
    parser.add_argument('mode', choices=['medicine','color','currency','read','objects'], help='Feature to run')
    parser.add_argument('--camera', type=int, default=0)
    args = parser.parse_args()

    if args.mode == 'medicine':
        medicine_reader(args.camera)
    elif args.mode == 'color':
        color_detector(args.camera)
    elif args.mode == 'currency':
        currency_recognition(args.camera)
    elif args.mode == 'read':
        smart_text_reader(args.camera)
    elif args.mode == 'objects':
        object_detection_assistant(args.camera)


if __name__ == '__main__':
    main()
