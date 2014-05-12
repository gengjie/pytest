# /usr/bin/env python
# coding=utf-8
'''
除了 dispatcher 外, 这个模块还包含一个 dispatcher_with_send 类. 你可
以使用这个类发送大量的数据而不会阻塞网络通讯缓冲区.
'''
__author__ = 'gengjie'
import asyncore
import urlparse
import string
import socket
import HTMLParser


class SimleAsyncHTTP(asyncore.dispatcher_with_send):
    def __init__(self, url, handler):
        asyncore.dispatcher_with_send.__init__(self)
        self.url = url
        self.handler = handler
        scheme, netloc, path, params, query, fragment = urlparse.urlparse(self.url)
        # print netloc
        # print string.split(netloc, ':', 1)
        host = ''
        port = 80  # default port
        try:
            print netloc
            netinfos = string.split(netloc, ':', 1)
            if len(netinfos) == 1:
                host = netinfos[0]
            else:
                host, port = string.split(netloc, ':', 1)
                port = int(port)
        except (TypeError, ValueError):
            port = 80
        if not path:  # path == None
            path = '/'
        if params:
            path += ';' + params
        if query:
            path += '?' + path

        self.request = 'GET %s HTTP/1.1\r\nHost: %s\r\n\r\n' % (path, host)
        self.host = host
        self.port = port
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect((host, port))

    def handle_connect(self):
        self.send(self.request)

    def handle_expt(self):  # connection failed
        self.close()
        if self.request.status is None:
            print 'connection failed...'
        else:
            print 'status:', self.request.status
            for key, value in self.request.status.items():
                print key, ':', value

    def handle_read(self):
        data = self.recv(2048)
        # print data,'\n','*'*100
        self.handler.collection_data(data)

    def handle_close(self):
        # self.handler.parse()
        pass


class DataHandler:
    def __init__(self):
        self.data = ''

    def collection_data(self, data):
        self.data += data

    def parse(self):
        try:
            HTMLParser.HTMLParser.feed(self.data)
        except AttributeError as e:
            print e.message


if __name__ == '__main__':
    SimleAsyncHTTP('http://www.siemens.com/entry/cc/en/', DataHandler())
    asyncore.loop()