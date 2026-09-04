import urllib.request, json
print('Status:')
print(urllib.request.urlopen('http://127.0.0.1:5000/status', timeout=5).read().decode())
print('\nCamera info:')
print(json.dumps(json.load(urllib.request.urlopen('http://127.0.0.1:5000/debug/camera_info', timeout=10)), indent=2))
