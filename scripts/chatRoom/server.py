import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()
port = 12348

print "Waiting for connection"
s.bind((host,port))
s.listen(9)

socket_list = []
socket_list.append('send')
client_thread,address = s.accept()
print("Connection established. Send a message")

while True:
    if socket_list[len(socket_list)-1] == 'send':
        print "Enter message"
        send_data = raw_input()
        client_thread.send(send_data)
        socket_list.remove('send')
        socket_list.append('recv')
    elif socket_list[len(socket_list)-1] == 'recv':
        recv_data = client_thread.recv(1024)
        if recv_data:
            print "Message fron the client:"
            print(recv_data)
            socket_list.remove('recv')
            socket_list.append('send')




# while True:
#     (client_thread,address) = s.accept()
#     print "Recieved from client" + address + ":"
#     recv_data = client_thread.recv(1024)
#     print(recv_data)
#     print "Enter Mesaage:"
#     s = raw_input()
#     client_thread.send(s)
