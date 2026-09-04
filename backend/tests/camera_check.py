import cv2, time, os
os.makedirs('backend/tests/camera_samples', exist_ok=True)

def try_camera(idx):
    cap = cv2.VideoCapture(idx, cv2.CAP_DSHOW)
    if not cap.isOpened():
        return False, None
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    # Attempt to disable auto exposure if supported
    try:
        cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0.25)
    except Exception:
        pass
    time.sleep(0.5)
    ok, frame = cap.read()
    samples = []
    if ok and frame is not None:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        mean = gray.mean()
        fname = f'backend/tests/camera_samples/sample_idx{idx}_mean{int(mean)}.jpg'
        cv2.imwrite(fname, frame)
        samples.append((fname, mean))
    # Capture a few more to see exposure changes
    for i in range(2):
        time.sleep(0.3)
        ok, frame = cap.read()
        if ok and frame is not None:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            mean = gray.mean()
            fname = f'backend/tests/camera_samples/sample_idx{idx}_iter{i}_mean{int(mean)}.jpg'
            cv2.imwrite(fname, frame)
            samples.append((fname, mean))
    cap.release()
    return True, samples

results = []
for idx in range(4):
    ok, samples = try_camera(idx)
    if not ok:
        print(f'Camera index {idx}: not available')
    else:
        print(f'Camera index {idx}: saved {len(samples)} samples')
        for s,m in samples:
            print(' ', s, 'mean=', int(m))
        results.append((idx, samples))

print('\nDiagnostic complete. Check backend/tests/camera_samples for images.')
