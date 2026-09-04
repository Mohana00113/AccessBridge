import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from backend.blind_helpers import capture_frame
import cv2

ok, frame = capture_frame(0, timeout=5.0)
if not ok or frame is None:
    print('Failed to capture frame')
else:
    cv2.imwrite('backend/tests/last_frame.jpg', frame)
    print('Saved backend/tests/last_frame.jpg')
