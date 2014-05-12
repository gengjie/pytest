# /usr/bin/env python
# coding=utf-8
'''
asyncore库是python的一个标准库，它是一个异步socket的包装。我们操作网络的时候可以直接使用socket等底层的库，但是asyncore使得我们可以更加方便的操作网络，避免直接使用socket，select，poll等工具时需要面对的复杂。
这个库很简单，包含了一个函数和一个类
* loop()函数
* dispatcher基类
需要注意的是，loop函数是全局的，不是dispatcher的方法
每一个从dispatcher继承的类的对象，都可以看作我们需要处理的一个socket,可以是TCP连接或者UDP，甚至是其它不常用的。使用容易，我们需要定义一个类，它继承dispatcher，然后我们重写（覆盖）一些方法就可以了。
我们需要重写的方法一般都以handle_打头。
'''
__author__ = 'gengjie'
import asyncore
import socket


class HttpClient(asyncore.dispatcher):
    def __init__(self, host, path):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect((host, 80))
        self.buffer = 'GET %s HTTP/1.1\r\nHost: %s\r\n\r\n' % (path, host)

    def handle_connect(self):
        asyncore.dispatcher.handle_connect(self)

    def handle_write(self):
        sent = self.send(self.buffer)
        self.buffer = self.buffer[sent:]

    def writable(self):
        return len(self.buffer) > 0


    def handle_read(self):
        print self.recv(8096)

    def close(self):
        return asyncore.dispatcher.close(self)


c = HttpClient('www.siemens.com', '/entry/cc/en/')
asyncore.loop()




