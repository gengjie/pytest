__author__ = 'gengjie'
import subprocess


def test():
    print '>' * 10


p = subprocess.Popen('ping info.siemens.com.cn', stdout=open('test.txt', 'w+'), shell=True)
p.communicate()
print '.' * 10