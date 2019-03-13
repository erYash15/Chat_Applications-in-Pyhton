import socket
import threading
s = socket.socket()
host = socket.gethostname()
print(host)
port = 9898
s.bind((host,port))
s.listen(5)
print("Waiting for connection.")
conn,temp = s.accept()
print("Successful!Connection is stablished with :- ", temp)
    
def function_sending():
    while(1):
        message = input("\nYou:- ")
        if(message == "quit"):
            s.close()
            exit()
        conn.send(message.encode())

def function_receving():
    while(1):
        recv_message = conn.recv(1024)
        print("client:-",recv_message.decode())
    
t1 = threading.Thread(target=function_sending) 
t2 = threading.Thread(target=function_receving) 
    
t1.start() 
t2.start() 

t1.join() 
t2.join() 
print("Done!") 
