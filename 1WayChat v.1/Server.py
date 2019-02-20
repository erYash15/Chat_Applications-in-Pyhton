import socket
s = socket.socket()
host = socket.gethostname()
print(host)
port = 8080
s.bind((host,port))
s.listen()
print("Waiting for connection")
temp = s.accept()
con1soc = temp[0]
con1add = temp[1]
print("Successful!Connection is stablished with :-")
print("socket :- ", con1soc)
print("")
print("socket :- ", con1add)

while(1):
    mess = input()
    con1soc.send(mess.encode())
    print("Succesfully! Message sent")
