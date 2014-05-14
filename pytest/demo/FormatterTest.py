#! /usr/env/python
# coding=utf-8
'''
formatter 将html parser的解析过程转换成事件流->Event Stream
这个类有两种, formatter & writer
writer 将事件流输出
'''
__author__ = 'gengjie'
import formatter
import htmllib

# w = formatter.AbstractWriter()
# DumbWriter is used for plain text writer.
# w = formatter.DumbWriter()
w = formatter.NullWriter()
f = formatter.AbstractFormatter(w)
htm = open('/home/gengjie/index.html')
p = htmllib.HTMLParser(f)
p.feed(htm.read())
p.close()
htm.close()