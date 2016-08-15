import socket
import sys
import io

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
    #f = open("tempimage.png", "wb")

    while True:
        data = conn.recv(BUFSIZ)
        if len(data) < 1:
            break
        count = count + len(data)
        print (len(data), count)
        picture = (picture + data.decode())
        print ("Received file: \n")
        #f.write(data)
        
        pos = picture.find("\r\n\r\n");
        print("Header length", pos)
        print(picture[:pos])
        picture = picture[pos+4:]
        img = open("image.jpg", "w", encoding="UTF8", errors='ignore')

        image = Image.open(io.BytesIO(bytes))
        image.save(savepath)
        
        img.write(picture);
        img.close()
    conn.close()

print ("Connection terminated")
serversocket.close()




