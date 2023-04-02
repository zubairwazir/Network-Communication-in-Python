import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('data.pr4e.org', 80))

url = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
sock.send(url)

while True:
    data = sock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
sock.close()