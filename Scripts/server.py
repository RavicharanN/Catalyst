import socket
import os


port = int(input("Enter port: "))

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
host = s.getsockname()[0]
s.close()
s = socket.socket()
s.bind((host, port))
s.listen(5)

print('Server listening....')
print(host, port)

conn, addr = s.accept()
print ('Got connection from' + str(addr))
data = conn.recv(1024)

filename=input()
f = open(filename,'rb')
l = f.read(1024)
print ("Sending file " + filename)

conn.send(str.encode(filename))
conn.recv(1024)
while (l):
   conn.send(l)
   l = f.read(1024)
f.close()

print('Done sending')
conn.close()