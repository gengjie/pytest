# /usr/bin/env python
# coding=utf-8

__author__ = 'gengjie'
import struct

bytes = struct.pack('i', 12.24)
num = struct.unpack('i', bytes)
print num, type(num), num[0]

a = (0,)
print a, type(a)