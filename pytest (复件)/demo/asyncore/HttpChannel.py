# _*_coding=utf-8_*_
__author__ = 'gengjie'
import asynchat
import asyncore
import socket
import string

'''
asynchat 模块是对 asyncore 的一个扩展. 它提供对面向行( line-oriented )
的协议的额外支持. 它还提供了增强的缓冲区支持(通过 push 方法和
"producer" 机制.
'''
PORT = 8080


class HttpChannel(asynchat.async_chat):
    def __init__(self, sock, addr):
        asynchat.async_chat.__init__(self, sock)
        self.set_terminator('\r\n')
        self.request = None
        self.data = ''
        self.shutdown = 0

    def collect_incoming_data(self, data):
        print data
        self.data += data

    def found_terminator(self):
        print '>>>>>>>>>>>>>>>>>>>>>>', self.request
        if not self.request:
            print '*' * 100
            self.request = string.split(self.data, None, 2)
            if len(self.request) != 3:
                self.shutdown = 1
            else:
                self.push("HTTP/1.0 200 OK\r\n")
                self.push("Content-type: text/html\r\n")
                self.push("\r\n")
                self.data = self.data + "\r\n"
                self.set_terminator("\r\n\r\n")  # look for end of headers
            print '*' * 100
        else:
            print '-' * 100
            self.push('<html><body><pre>\r\n')
            self.push(self.data)
            self.push('</pre></body></html>\r\n')
            self.close_when_done()
            print '-' * 100


class HttpServer(asyncore.dispatcher):
    def __init__(self, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.bind(("", port))
        self.listen(5)

    def handle_accept(self):
        print 'some request reaching...'
        conn, addr = self.accept()
        HttpChannel(conn, addr)
        # pass


if __name__ == '__main__':
    HttpServer(PORT)
    asyncore.loop()