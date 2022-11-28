import socket
host = socket.gethostname()
print(host)

host_get = socket.gethostbyname(host)
print(host_get)