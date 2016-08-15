import socket
import sys
import io
import base64

HOST = ""
PORT = 12321
ADDR = (HOST, PORT)
BUFSIZ = 4096

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(ADDR)
serversocket.listen(5)
print ("Server is listening")

count = 0
picture = "";

while True:
    print ("Waiting for connection...")
    conn, addr = serversocket.accept()
    print ("Got connection from: ", addr)

    while True:
        
        base64Image = conn.recv(BUFSIZ)

        if len(base64Image) < 1:
            break

        print("Recieved data: " + str(base64Image))

        decodedImage = base64.b64decode(base64Image)

        print("Decoded image: " + str(decodedImage))

        file = open("imageToSave.png", "wb")
        file.write(decodedImage)
        file.close()

        print ("Received file: \n")

        #image = Image.open(io.BytesIO(picture))
        #image.save(savepath)
        
        #img.write(picture);
        #img.close()
    conn.close()

print ("Connection terminated")
serversocket.close()




