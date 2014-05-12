__author__ = 'gengjie'
import socket
import sys
import time

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("localhost", 9999))
    s.sendall("some message from client...")
    index = 0

    data = s.recv(1024)
    print data
    time.sleep(3)
    s.close()
except socket.error, msg:
    print msg
    sys.exit()

