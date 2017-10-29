import socket
import os
import ntpath
import shutil


def send(path, port):

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

    filepath = str(path)
    filename = ntpath.basename(filepath)

    if os.path.isdir(path)==True:
        f = open(shutil.make_archive(filename, "zip", str(path)), 'rb')
        filename += ".zip"
    else:
        f = open(filepath, 'rb')

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
