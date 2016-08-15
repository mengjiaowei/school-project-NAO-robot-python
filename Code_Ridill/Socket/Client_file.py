import socket
import sys

HOST = socket.gethostname()   # = localhost
PORT = 12321                    # random port

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    clientsocket.connect((HOST,PORT))
    print ("You are connected")
    with open("ny.txt", "r+") as file:
        data = file.read(512)
    clientsocket.send(data.encode())
    print ("File being sent: ", file.name)
    file.close()
    #received = clientsocket.recv(512)

finally:
    clientsocket.close()
    print("\nSent:\n{}".format(data))
    #print("\nReceived:\n{}".format(received))








