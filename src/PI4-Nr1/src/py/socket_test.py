# Test Socket
# Projekt EduDev
# 2020-05-05

import socket

socketname = socket.gethostname()
print (socketname, socket.gethostbyname(socketname))
socketname = "fom.de"
print (socketname, socket.gethostbyname(socketname))

# ZeitServer / TODO
# c = socket.socket()
# url ="ptbtime1.ptb.de"
# port = 37 
# c.connect ((url, port))
# ret = c.recv(100)
# print (ret )

# http get per socket 

