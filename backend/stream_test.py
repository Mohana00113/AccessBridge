import socket
import time

s = socket.create_connection(('127.0.0.1', 5000), timeout=10)
request = b'GET /video_feed HTTP/1.1\r\nHost: 127.0.0.1:5000\r\nConnection: close\r\n\r\n'
s.sendall(request)

data = b''
count = 0
start = time.time()
while time.time() - start < 6:
    chunk = s.recv(8192)
    if not chunk:
        break
    data += chunk
    count += chunk.count(b'--frame')

print('bytes', len(data), 'frames', count)
print(data[:400].decode('latin1', errors='replace'))
s.close()
