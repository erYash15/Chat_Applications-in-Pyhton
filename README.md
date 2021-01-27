# Chat_Applications-in-Pyhton
Bunch of Application for Broad Communication, One to One , Many to Many etc.(of clients of same and different machines)<br>

How to set up a simple Chat Room server and allow multiple clients to connect to it using a client-side script. The code uses the concept of sockets and threading.<br>

### Socket programming

Sockets can be thought of as endpoints in a communication channel that is bi-directional, and establishes communication between a server and one or more clients. Here, we set up a socket on each end and allow a client to interact with other clients via the server. The socket on the server side associates itself with some hardware port on the server side. Any client that has a socket associated with the same port can communicate with the server socket.

### Multi-Threading

A thread is sub process that runs a set of commands individually of any other thread. So, every time a user connects to the server, a separate thread is created for that user and communication from server to client takes place along individual threads based on socket objects created for the sake of identity of each client.
We will require two scripts to establish this chat room. One to keep the serving running, and another that every client should run in order to connect to the server.


### Server Side Script

The server side script will attempt to establish a socket and bind it to an IP address and port specified by the user (windows users might have to make an exception for the specified port number in their firewall settings, or can rather use a port that is already open). The script will then stay open and receive connection requests, and will append respective socket objects to a list to keep track of active connections. Every time a user connects,
a separate thread will be created for that user. In each thread, the server awaits a message, and sends that message to other users currently on the chat. If the server encounters an error while trying to receive a message from a particular thread, it will exit that thread.

## Usage

This server can be set up on a local area network by choosing any on computer to be a server node, and using that computer’s private IP address as the server IP address.
For example, if a local area network has a set of private IP addresses assigned ranging from 192.168.1.2 to 192.168.1.100, then any computer from these 99 nodes can act as a server, and the remaining nodes may connect to the server node by using the server’s private IP address. Care must be taken to choose a port that is currently not in usage. For example, port 22 is default for ssh, and port 80 is default for HTTP protocols. So these two ports preferably, shouldnt be used or reconfigured to make them free for usage.
However, if the server is meant to be accessible beyond a local network, the public IP address would be required for usage. This would require port forwarding in cases where a node from a local network (node that isnt the router) wishes to host the server. In this case, we would require any requests that come to the public IP addresses to be re routed towards our private IP address in our local network, and would hence require port forwarding.<br><br>
```bash
/* Both the server and client script can then be run
   from the Command prompt (in Windows) or from bash 
   Terminal (Linux users) by simply typing 
   "python chat_server.py  " or "python client.py  ". 
   For example, */
python chat_server.py 192.168.55.13 8081
python client.py 192.168.55.13 8081
```

## Output

In the picture given below, a server has been initialized on the left side of the terminal and a client script on the right side of the terminal. (Splitting of terminal done using tmux, ‘sudo apt-get install tmux’). For initialization purposes, you can see that whenever a message is sent by a user, the message along with IP address is shown on the server side.
<br>
![Chat1](https://user-images.githubusercontent.com/34357926/106038383-e6cb2f00-60fd-11eb-99f5-feef1b3e7bdf.png)

The below picture has a basic conversation between two people on the same server. Multiple clients can connect to the server in the same way!><br>

![Chat2](https://user-images.githubusercontent.com/34357926/106038386-e894f280-60fd-11eb-868f-94af8efd5f85.png)

## Thank You
