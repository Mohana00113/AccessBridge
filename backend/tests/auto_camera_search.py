import cv2, time, os, json
os.makedirs('backend/tests/auto_search', exist_ok=True)

backends = [cv2.CAP_DSHOW, cv2.CAP_MSMF, cv2.CAP_ANY]
indices = list(range(0,4))
exposures = [-13, -9, -5, -3, -1, 0, 1, 3, 5]
brights = [0.0, 0.5, 1.0, 1.5, 2.0]

results = []
for b in backends:
    for idx in indices:
        try:
            cap = cv2.VideoCapture(idx, apiPreference=b)
        except TypeError:
            cap = cv2.VideoCapture(idx)
        if not cap.isOpened():
            print(f'backend={b} idx={idx} open failed')
            continue
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
        time.sleep(0.3)
        best = None
        # try exposures
        for exp in exposures:
            try:
                cap.set(cv2.CAP_PROP_EXPOSURE, float(exp))
            except Exception:
                pass
            time.sleep(0.25)
            ret, frame = cap.read()
            if not ret or frame is None:
                continue
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            mean = float(gray.mean())
            fname = f'backend/tests/auto_search/b{int(b)}_i{idx}_exp{exp}_m{int(mean)}.jpg'
            try:
                cv2.imwrite(fname, frame)
            except Exception:
                fname = None
            if best is None or (mean is not None and mean > best[0]):
                best = (mean, fname, {'backend': int(b), 'index': idx, 'exp': exp, 'bright': None})
        # try brightness settings too
        for br in brights:
            try:
                cap.set(cv2.CAP_PROP_BRIGHTNESS, float(br))
            except Exception:
                pass
            time.sleep(0.18)
            ret, frame = cap.read()
            if not ret or frame is None:
                continue
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            mean = float(gray.mean())
            fname = f'backend/tests/auto_search/b{int(b)}_i{idx}_bright{br}_m{int(mean)}.jpg'
            try:
                cv2.imwrite(fname, frame)
            except Exception:
                fname = None
            if best is None or (mean is not None and mean > best[0]):
                best = (mean, fname, {'backend': int(b), 'index': idx, 'exp': None, 'bright': br})
        cap.release()
        if best:
            print(f'Best for backend={b} idx={idx} -> mean={best[0]} file={best[1]} cfg={best[2]}')
            results.append({'backend': int(b), 'index': idx, 'mean': best[0], 'file': best[1], 'cfg': best[2]})

# sort by mean desc
results.sort(key=lambda x: x['mean'] if x['mean'] is not None else -1, reverse=True)
with open('backend/tests/auto_search/result_summary.json', 'w') as f:
    json.dump(results, f, indent=2)

print('\nAuto-search complete. Results written to backend/tests/auto_search/result_summary.json')
for r in results:
    print(r)
