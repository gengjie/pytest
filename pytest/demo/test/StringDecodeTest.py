__author__ = 'gengjie'
str = '\xE4\xBD\xA0\xE6\x98\xAF'
print str.decode('utf-8')

str = '123'
import string
i = string.atoi(str)
print type(i)
print type(repr(string.atoi(str)))
chs = ['1','2','3','4']
print ':'.join(chs)
print len(chs)

str = u'\u5e94\u7528\u7a0b\u5e8f\u540d'
print str.encode('utf-8'), str