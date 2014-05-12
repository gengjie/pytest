__author__ = 'gengjie'
import os
import platform

st = {'a': '1', 'b': '2', 'c': '3'}
a, b, c = st
print st['a']
print a

s = 1, 2, 3
print type(s)

import operator

print operator.isSequenceType(s)

str = 'asdfksjkdgjshhsddg'

print str[0:4:2]
print str[-2:]
print str[-1:-4:-2]

for f in os.listdir('/home/gengjie/python'):
    print f, os.path.split(f)
    print f, os.path.splitext(f)

chs = '*'

print chs * 10


def f(x, n):
    try:
        if n == 1:
            return x
        else:
            n -= 1
            try:
                return x * f(x, n)
            except TypeError:
                print 'TypeError'
    except RuntimeError:
        print '234234'


print f(2, 100)

print chs * 100

# for _tuple in os.walk('/home/gengjie/'):
#     for item in _tuple:
#         print item

f = open("/home/gengjie/index.html", "rb")
data = f.read()
data.decode("utf-8")
print data

print '*' * 50

print platform.machine(), platform.uname()

s = "/home/gengjie/PycharmProjects/pytest/demo/ZlibDecompressTest.py"
print s.split('/', 4)[4]