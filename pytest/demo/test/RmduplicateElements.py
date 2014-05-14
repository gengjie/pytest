# -*-coding=utf-8-*-
__author__ = 'gengjie'
import random

list = []
for i in range(1000):
    list.append(chr(random.randint(ord('0'), ord('z'))))
print repr(list)


def partion(base):
    for j in range(0, len(list)):
        if list[j] <= base:
            pass


print 1.0 / 1000.0
print '\a'