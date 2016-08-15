import socket
import sys

HOST = socket.gethostname()   # = localhost
PORT = 12321                    # random port
BUFSIZ = 4096

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    clientsocket.connect((HOST,PORT))
    print ("You are connected")

    while True:
        data = open("image.jpg", "r+", encoding="UTF8", errors='ignore')
        while True:
            pic = data.read()
            clientsocket.send(pic.encode())
            print ("File being sent: ", data.name)
            #reply = clientsocket.recv(BUFSIZ)
            if not data:
                break
            data.close()
            exit()

finally:
    clientsocket.close()
    #print("\nSent:\n{}".format(data))
    #print("\nReceived:\n{}".format(received))
    #data = open("image.jpg", "r+", encoding ="utf-16")




