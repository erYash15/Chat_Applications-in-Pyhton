import socket
import threading
s = socket.socket()
host = socket.gethostname()
port = 9898
s.connect((host,port))
print("Connected to Server")
    
def function_receving():
    while(1):
        recv_message = s.recv(1024)
        print("\nServer :", recv_message.decode())
    
def function_sending():
    while(1):
        message = input("\nYou:-")
        if(message == "quit"):
            s.close()
            exit()
        s.send(message.encode()) 
    
t1 = threading.Thread(target=function_sending) 
t2 = threading.Thread(target=function_receving) 
    
t1.start() 
t2.start() 

t1.join() 
t2.join() 
print("Done!") 
