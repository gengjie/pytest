# /usr/bin/env python
# coding=utf-8
# pickle 模块同 marshal 模块相同, 将数据连续化, 便于保存传输. 它比
# marshal 要慢一些, 但它可以处理类实例, 共享的元素, 以及递归数据结构等.
__author__ = 'gengjie'
import pickle


class Something(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getinfo(self):
        print self.name, self.age

    pass


value = (
    "this is a string",
    [1, 2, 3, 4],
    ("more tuples", 1.2, 3.4, 5.6),
    "this is yet another string",
    Something('gengjie', 28)
)

data = pickle.dumps(value, 1)
print repr(data), len(data)

file = open("./pickle.bin", "w+")
file.write(data)
file.flush()
file.close()

file = open("./pickle.bin", "rb")
data = file.read()
print repr(data)
file.close()
file = open("./pickle.bin", "rb")
data = pickle.load(file)
file.close()
print data

s = data[4]
s.getinfo()

