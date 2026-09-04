import urllib.request
import json

BASE = 'http://127.0.0.1:5000'
ENDPOINTS = ['medicine','color','currency','read','objects']

def call(ep):
    try:
        with urllib.request.urlopen(f"{BASE}/blind/{ep}", timeout=10) as r:
            body = r.read().decode('utf8')
            print(ep.upper(), '->', r.status)
            try:
                print(json.dumps(json.loads(body), indent=2))
            except Exception:
                print(body)
    except Exception as e:
        print(ep.upper(), 'ERROR ->', e)

if __name__ == '__main__':
    for e in ENDPOINTS:
        call(e)
        print('-' * 40)
