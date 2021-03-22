import socket

#c = socket.socket()
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clientsocket.connect (("www.google.com", 80))

reqest = "GET / HTTP/1.1\n\n"

clientsocket.sendall (bytes(reqest, "ascii"))

i=0
while True:

    data = clientsocket.recv(40960)
    if not data: 
        break

    i +=1
    print(i, data) 
    if b"</html>" in data:
        break

