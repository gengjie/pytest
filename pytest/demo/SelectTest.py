# /usr/bin/env python
# _*_coding=utf-8_*_
'''
在python中，select函数是一个对底层操作系统的直接访问的接口。
它用来监控sockets、files和pipes，等待IO完成（Waiting for I/O completion）。
当有可读、可写或是异常事件产生时，select可以很容易的监控到.
select.select（rlist, wlist, xlist[, timeout]） 传递三个参数，
一个为输入而观察的文件对象列表，
一个为输出而观察的文件对象列表和一个观察错误异常的文件列表。
第四个是一个可选参数，表示超时秒数。其返回3个tuple，每个tuple都是一个准备好的对象列表，它和前边的参数是一样的顺序。
'''
__author__ = 'gengjie'
