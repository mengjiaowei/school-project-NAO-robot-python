import socket
import sys

HOST = ""
PORT = 12321
ADDR = (HOST, PORT)

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(ADDR)
serversocket.listen(5)
print ("Server is listening")

while True:
    print ("Waiting for connection...")
    conn, addr = serversocket.accept()
    print ("Got connection from: ", addr)
    
    while True:
        data = conn.recv(512).decode()
        #text = data.readlines()
        #for lines in data:
        print("File received: "+ data.name)
        print("\n"+format(data)+"\n")
   # serversocket.sendall("R")
    
    conn.close()

print ("Connection terminated")
serversocket.close()




