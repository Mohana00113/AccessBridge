import cv2
import numpy as np
import pyttsx3
import time
from typing import Tuple, List, Optional

# Initialize OCR reader and TTS engine as singletons for reuse
_ocr_reader = None
_tts_engine = None

def get_ocr_reader(languages: List[str] = ["en"]):
    global _ocr_reader
    if _ocr_reader is None:
        try:
            import easyocr
        except ImportError:
            raise RuntimeError("easyocr is not installed")
        _ocr_reader = easyocr.Reader(lang_list=languages, gpu=False)
    return _ocr_reader

def get_tts_engine():
    global _tts_engine
    if _tts_engine is None:
        _tts_engine = pyttsx3.init()
        _tts_engine.setProperty('rate', 160)
    return _tts_engine

def speak(text: str):
    """Speak the given text using pyttsx3 (blocking until spoken).

    Keeps calls simple and protects against TTS errors.
    """
    try:
        engine = get_tts_engine()
        engine.say(text)
        engine.runAndWait()
    except Exception:
        # Fallback: print to console if TTS fails
        print("TTS error — fallback print:\n", text)

def capture_frame(camera_index: int = 0, timeout: float = 5.0) -> Tuple[bool, np.ndarray]:
    """Capture a single frame from the webcam. Returns (ok, frame).

    timeout: seconds to wait for a valid frame
    """
    cap = cv2.VideoCapture(camera_index, cv2.CAP_DSHOW)
    if not cap.isOpened():
        return False, None
    start = time.time()
    ok = False
    frame = None
    try:
        while time.time() - start < timeout:
            try:
                ret, f = cap.read()
            except Exception:
                # Protect against OpenCV C++ exceptions
                break
            if ret and f is not None:
                ok = True
                frame = f
                break
    finally:
        try:
            cap.release()
        except Exception:
            pass
    return ok, frame

def ocr_image_to_text(image: np.ndarray, languages: List[str] = ["en"]) -> str:
    """Run OCR on an image and return concatenated text.

    Uses EasyOCR; returns an empty string on error.
    """
    try:
        reader = get_ocr_reader(languages)
        results = reader.readtext(image)
        texts = [res[1] for res in results if len(res) >= 2]
        return " ".join(texts)
    except Exception:
        return ""

def dominant_color_name(image: np.ndarray) -> Tuple[str, Tuple[int,int,int]]:
    """Estimate the dominant color name and return (name, bgr_color).

    Uses k-means on pixels and maps hue to a small set of basic colors.
    """
    try:
        small = cv2.resize(image, (100, 100), interpolation=cv2.INTER_AREA)
        data = small.reshape((-1,3))
        data = np.float32(data)
        # kmeans to find main cluster
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
        K = 3
        _, labels, centers = cv2.kmeans(data, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
        counts = np.bincount(labels.flatten())
        dominant = centers[np.argmax(counts)].astype(int)
        b,g,r = int(dominant[0]), int(dominant[1]), int(dominant[2])
        # Convert to HSV to map to color name
        hsv = cv2.cvtColor(np.uint8([[[b,g,r]]]), cv2.COLOR_BGR2HSV)[0][0]
        h, s, v = int(hsv[0]), int(hsv[1]), int(hsv[2])
        name = _hsv_to_color_name(h, s, v)
        return name, (b,g,r)
    except Exception:
        return "unknown", (0,0,0)

def _hsv_to_color_name(h: int, s: int, v: int) -> str:
    # Simple hue ranges for basic colors
    if v < 40:
        return "black"
    if s < 30 and v > 200:
        return "white"
    if s < 40:
        return "gray"
    if h < 10 or h >= 160:
        return "red"
    if 10 <= h < 25:
        return "orange"
    if 25 <= h < 35:
        return "yellow"
    if 35 <= h < 85:
        return "green"
    if 85 <= h < 125:
        return "blue"
    if 125 <= h < 160:
        return "purple"
    return "unknown"


def extract_prices(text: str) -> list:
    """Extract probable price mentions from OCR text.

    Matches patterns like '₹100', 'Rs. 50', 'INR 20', or bare numbers like '100.00'.
    Returns a list of normalized strings.
    """
    import re
    if not text:
        return []
    text = text.replace(',', '')
    patterns = [r'₹\s?\d+(?:\.\d+)?', r'Rs\.?\s?\d+(?:\.\d+)?', r'INR\s?\d+(?:\.\d+)?', r'\b\d+(?:\.\d{1,2})?\b']
    found = []
    for p in patterns:
        for m in re.findall(p, text, flags=re.IGNORECASE):
            found.append(m.strip())
    # Heuristic: prefer currency-tagged matches first
    cur = [f for f in found if any(sym in f.lower() for sym in ['₹','rs','inr'])]
    if cur:
        return cur
    # otherwise return numeric candidates (filter out long digits like years)
    nums = [f for f in found if len(f) <= 10 and re.search(r'\d', f)]
    return nums
