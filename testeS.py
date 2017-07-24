import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 6666
s.bind(('10.50.20.189',port))
s.listen(5)
while True:
    c,addr = s.accept()
    print "Got connection from", addr
    #c.send("FreeFloat Ftp Server (Version 1.00)")
    c.send("Strudel")