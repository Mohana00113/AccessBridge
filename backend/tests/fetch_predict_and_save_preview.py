import urllib.request, json, base64, os
print('Calling /predict...')
try:
    print(json.load(urllib.request.urlopen('http://127.0.0.1:5000/predict', timeout=5)))
except Exception as e:
    print('predict error:', e)
print('\nFetching /debug/calibrate and saving preview...')
try:
    data = json.load(urllib.request.urlopen('http://127.0.0.1:5000/debug/calibrate', timeout=10))
    img_b64 = data['data']['image']
    img_bytes = base64.b64decode(img_b64)
    out_dir = 'backend/tests'
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, 'calibrated_preview.jpg')
    with open(out_path, 'wb') as f:
        f.write(img_bytes)
    print('Saved preview to', out_path)
    print('Returned mean brightness:', data['data'].get('mean'))
except Exception as e:
    print('calibrate error:', e)
