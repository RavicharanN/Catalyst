import cv2
import numpy
import socket
import os
import ntpath
import sys
import time
import threading

port = 9999
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
host = s.getsockname()[0]
s.close()
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, int(port)))
s.listen(5)

print('Server listening....')
print(host, int(port))

conn, addr = s.accept()
print ('Got connection from' + str(addr))
data = conn.recv(1024)

vc = cv2.VideoCapture(0)
frame = b''

def startWebcam():
    global vc
    global frame
    rval = True
    while rval:
        rval, frame = vc.read()
        key = cv2.waitKey(20)
        if key == 27: # exit on ESC
            break

t = threading.Thread(target=startWebcam)
t.start()

time.sleep(1)

while True:
    img_str = cv2.imencode('.jpg', frame)[1].tostring()
    #print(sys.getsizeof(img_str))
    conn.send(img_str)
    stat = conn.recv(1024).decode("utf-8")
    print(stat+"|")

print("Error")
conn.close()
cv2.destroyWindow("preview")