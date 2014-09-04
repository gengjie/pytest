# /usr/bin/env python
# coding=utf-8

__author__ = 'gengjie'
import struct, string

bytes = struct.pack('i', 12.24)
num = struct.unpack('i', bytes)
buffer = struct.pack('l', 1234567890)
print num, type(num), num[0]
print struct.unpack('l',buffer)

ip = struct.pack('15s', '192.168.0.1')
print repr(struct.unpack('15s', ip)[0])
print len(struct.unpack('15s', ip)[0])
a = (0,)
print a, type(a)

s = '192.168.0.1\x00\x00\x00\x00'
print len(string.rstrip(s, '\x00'))