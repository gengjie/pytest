# /usr/bin/env python
# coding=utf-8
# marshal 模块可以把不连续的数据组合起来 - 与字符串相互转化, 这样它们就
# 可以写入文件或是在网络中传输.
__author__ = 'gengjie'
import marshal

value = (
    "this is a string",
    [1, 2, 3, 4],
    ("more tuples", 1.2, 3.4, 5.6),
    "this is yet another string"
)
# text mode
# data = marshal.dumps(value)
# binary mode
data = marshal.dumps(value, 1)
file = open("./marshal.bin", "w+")
file.write(data)
file.flush()
file.close()
print repr(data), type(data), len(data)

file = open("./marshal.bin", "rb")
# bin = file.read()
# print bin
print marshal.load(file)
file.close()