import socket
import sys
import base64

HOST = socket.gethostname()   # = localhost
PORT = 12321                    # random port
BUFSIZ = 4096

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    clientsocket.connect((HOST,PORT))
    print ("You are connected")

    while True:

        with open("tempimage.png", "rb") as imageFile:
            base64Image_data = base64.b64encode(imageFile.read())

        #image = open("tempimage.png", "r+", encoding="UTF8", errors='ignore')
        
        while True:

            #image_data = image.read()

            #base64Image_data = base64.b64encode(image_data)
            
            clientsocket.send(base64Image_data)
            print ("File being sent: ", imageFile.name)
            
            exit()

finally:
    clientsocket.close()
    #print("\nSent:\n{}".format(data))
    #print("\nReceived:\n{}".format(received))
    #data = open("image.jpg", "r+", encoding ="utf-16")




