# coding='utf-8'
__author__ = 'gengjie'

import string
import random

text = 'Resume for GengJie'

print string.upper(text)
print string.lower(text)
strs = []
strs = string.split(text)
# print os.path.split(text)
print strs
for str in strs:
    print str
print string.join(strs, '%')
print string.replace(text, 'GengJie', 'Geng Jie')
print string.find(text, 'GengJie'), string.find(text, 'r')
print 'there\'re %d e in the text' % (string.count(text, 'e'))

print string.atoi('0x9E8A32', 16)
print string.atof('101.2324')

print text.decode('utf-8').encode('gbk')

s = 'GET / HTTP/1.1'

print string.split(s, None, 2)

i = random.randint(ord('a'), ord('z'))
print i, chr(i)