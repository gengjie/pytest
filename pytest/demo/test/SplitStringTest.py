# -*- coding=utf-8 -*-
__author__ = 'gengjie'
str = 'This is a demonstrate program for Hadoop!' \
      '123 1231 23'
substr = str.split()
print substr
for s in substr:
    print s,

import re
d = '''[  4] local 10.0.0.9 port 5001 connected with 10.0.0.1 port 59345
[ ID] Interval       Transfer     Bandwidth
[  4]  0.0- 2.0 sec   242 KBytes   990 Kbitsc
[  4]  2.0- 4.0 sec   238 KBytes   973 Kbitsc
[  4]  4.0- 6.0 sec   240 KBytes   985 Kbitsc
[  4]  6.0- 8.0 sec   238 KBytes   973 Kbitsc
[  4]  8.0-10.0 sec   238 KBytes   973 Kbitsc
[  4] 10.0-12.0 sec   240 KBytes   985 Kbitsc'''
a = re.findall("\d+.\d+", d)
print a

url = 'http://www.dmoz.org/Computers/Programming/Languages/Python/Books/'
print url.split('/')[-6:]