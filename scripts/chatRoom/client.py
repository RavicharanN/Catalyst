import socket
import time

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()
port = 12348

socket_list = []
socket_list.append('recv')
s.connect((host,port))

while True:
    if socket_list[len(socket_list)-1] == 'recv':
        recv_data = s.recv(1024)
        if recv_data:
            print "Message from server:"
            print(recv_data)
            socket_list.remove('recv')
            socket_list.append('send')
    elif socket_list[len(socket_list)-1] == 'send':
        print "Enter message:"
        send_data = raw_input()
        s.send(send_data)
        socket_list.remove('send')
        socket_list.append('recv')
