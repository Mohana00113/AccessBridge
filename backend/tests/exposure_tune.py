import cv2, time, os
os.makedirs('backend/tests/exposure_runs', exist_ok=True)

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
if not cap.isOpened():
    print('Camera open failed')
    exit(1)

# Try to set manual exposure (platform dependent)
print('Initial CAP_PROP_AUTO_EXPOSURE:', cap.get(cv2.CAP_PROP_AUTO_EXPOSURE))
try:
    cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0.25)
    print('Set CAP_PROP_AUTO_EXPOSURE -> 0.25')
except Exception as e:
    print('Auto exposure set failed', e)

# Try ranges of exposure and brightness
results = []
for exp in [-13, -11, -9, -7, -5, -3, -1, 0, 1, 3, 5]:
    try:
        cap.set(cv2.CAP_PROP_EXPOSURE, float(exp))
    except Exception:
        pass
    time.sleep(0.3)
    ret, frame = cap.read()
    if not ret or frame is None:
        mean = None
        fname = None
    else:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        mean = gray.mean()
        fname = f'backend/tests/exposure_runs/exp_{exp}_mean{int(mean)}.jpg'
        cv2.imwrite(fname, frame)
    print('exp=', exp, 'mean=', mean)
    results.append((exp, mean, fname))

# Try brightness adjustments
for b in [0.0, 0.2, 0.5, 1.0, 1.5, 2.0]:
    try:
        cap.set(cv2.CAP_PROP_BRIGHTNESS, float(b))
    except Exception:
        pass
    time.sleep(0.2)
    ret, frame = cap.read()
    if not ret or frame is None:
        mean = None
        fname = None
    else:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        mean = gray.mean()
        fname = f'backend/tests/exposure_runs/bright_{b}_mean{int(mean)}.jpg'
        cv2.imwrite(fname, frame)
    print('bright=', b, 'mean=', mean)
    results.append((f'bright_{b}', mean, fname))

cap.release()
print('\nDone. Files in backend/tests/exposure_runs')
for r in results:
    print(r)
