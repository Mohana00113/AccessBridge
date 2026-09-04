import time
import urllib.request
import json

URL = 'http://127.0.0.1:5000/predict'
print('Starting /predict poller. Make gestures in front of the camera now.')
start = time.time()
try:
    for i in range(60):
        try:
            r = urllib.request.urlopen(URL, timeout=2)
            data = r.read().decode()
            j = json.loads(data)
            ts = time.time() - start
            print(f"{i:02d} {ts:5.2f}s -> letter={j.get('letter')!r} hand={j.get('hand_detected')} conf={j.get('confidence')}")
        except Exception as e:
            print(f"{i:02d} ERROR: {e}")
        time.sleep(0.5)
except KeyboardInterrupt:
    print('Interrupted by user')
print('Poller finished.')
