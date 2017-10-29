import socket                   # Import socket module

s = socket.socket()             # Create a socket object
host = input("Enter ip of sender: ")
port = int(input("Enter port number: "))                   # Reserve a port for your service.

s.connect((host, port))
s.send(str.encode("Hello server!"))
filename = s.recv(1024).decode("utf-8")
s.send(str.encode("lel"))
with open("R_"+filename, 'wb') as f:
    print('receiving data...')
    while True:
        data = s.recv(1024)
        #print('data=%s', (data))
        if not data:
            break
        # write data to a file
        f.write(data)

f.close()
print('Successfully get the file')
s.close()
print('connection closed')