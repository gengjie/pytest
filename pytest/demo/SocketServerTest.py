'''
this demo shows how to use socket as a server in multi-thread mode
'''
__author__ = 'gengjie'
import socket
import sys
import threading

class MessageHanlder(threading.Thread):
    MESSAGE = "some plain text responses from server..."

    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.conn = conn

    def run(self):
        super(MessageHanlder, self).run()
        self.conn.send(MessageHanlder.MESSAGE)
        while True:
            data = self.conn.recv(1024)
            if not data:
                break
            print data
        print 'server received complete'
        self.conn.sendall("the server has received message already...")
        self.conn.close()


HOST = ''  # Symbolic name meaning all available interfaces
PORT = 9999  # Arbitrary non-privileged port

# socket.AF_INET : ipv4
# socket.SOCK_STREAM : TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind socket to a local specified interface and port
try:
    s.bind((HOST, PORT))
except socket.error, message:
    sys.exit()

# start to listen
s.listen(1)

while 1:
    conn, addr = s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
    MessageHanlder(conn).start()

s.close()