import cv2
import numpy
import socket
import os
import sys
import time

ip = raw_input()
s = socket.socket()
port = 9999
s.connect((ip, port))
s.send(str.encode("Connected"))


cv2.namedWindow("preview")
while True:
    try:
        raw_input()
        img_str = s.recv(90456)
        print(sys.getsizeof(img_str))
        nparr = numpy.fromstring(img_str, numpy.uint8)
        frame = cv2.imdecode(nparr, cv2.CV_LOAD_IMAGE_COLOR)
        cv2.imshow("preview", frame)
        key = cv2.waitKey(20)
        if key == 27: # exit on ESC
            break
        s.send(str.encode("1"))
    except:
        print("error")
        s.send(str.encode("0"))

cv2.destroyWindow("preview")
s.close()
print('connection closed')