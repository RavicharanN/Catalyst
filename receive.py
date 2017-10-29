import socket

def receive(ip, portNo):
    s = socket.socket()
    port = int(portNo)
    s.connect((ip, port))
    s.send(str.encode("Connected"))
    filename = s.recv(1024).decode("utf-8")
    s.send(str.encode("lel"))
    with open("R_"+filename, 'wb') as f:
        print('receiving file...')
        while True:
            data = s.recv(1024)
            if not data:
                break
            f.write(data)

    f.close()
    print('Received Successfully')
    s.close()
    print('connection closed')
