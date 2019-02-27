import socket
s = socket.socket()
host = socket.gethostname()
print(host)
port = 8080
s.bind((host,port))
s.listen(5)
print("Waiting for connection.")
conn,temp = s.accept()
print("Successful!Connection is stablished with :- ", temp)

while(1):
    message = input("You:- ")
    if(message == "quit"):
        s.close()
        exit()
    conn.send(message.encode())
    recv_message = conn.recv(1024)
    print("client :- ",recv_message.decode())
