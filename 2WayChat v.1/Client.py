import socket
s = socket.socket()
host = ""#server host id in ""
port = 8080
s.connect((host,port))
print("Connected to Server")

while(1):
    recv_message = s.recv(1024)
    print("Server :", recv_message.decode())
    message = input("You:-")
    message = message.encode()
    s.send(message)
