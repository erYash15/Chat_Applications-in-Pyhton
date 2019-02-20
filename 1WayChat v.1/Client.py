import socket
s = socket.socket()
host = socket.gethostname()
port = 8080
s.connect((host,port))
print("Connected to Server")

while(1):
    mess = s.recv(1024)
    print("Server : ", mess.decode())
