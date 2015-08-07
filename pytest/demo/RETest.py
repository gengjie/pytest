#! /usr/env/python
# coding=utf-8
__author__ = 'gengjie'
import re


str = '123我爱Python.py'
print re.compile(str)
re.search('.*爱.*', str)
if re.match('.*爱.*', str):
    print 123
if re.search('.*爱.*', str):
    print 234
print str

filename = "/home/gengjie/index.html.2"
pattern = '<a\\s+href\\s*=\\s*\"?(.*?)[\"|>]'
_file = open(filename, 'rb')
lines = _file.readlines()
for line in lines:
    strs = re.findall(r'<a\s+href\s*=\s*["|\']?(.*?)[\["|\']|>]', line)
    # print repr(strs)
    for link in strs:
        if link is None:
            continue
        elif link.strip() == "":
            continue
        elif link.lower().find('javascript') > -1:
            continue
        print link

s = 'c:/dir1/dir2/name.txt'
print re.findall(r'^.+/(.+)$', s)

content = '123123<type>sdfsdf</type><type>sdfsdf</type><type>sdfsdf</type>123123'
print re.findall(r'^.+<type>(.+?)</type>.+$', content)

content = 'HelloWorld234'
print re.findall(r'(^[a-z|A-z]*)[^a-z|A-z]*$', content)

content = '''
    ADFSADGSAHAHSH
    DATA
    2352353252
    sdgsdgsadg
    DGASDGSADG
'''
print repr(content)
# content = '\n    ADFSADGSAHAHSH\n    DATA\n    2352353252\n    sdgsdgsadg\n    DGASDGSADG\n'
# print content
print re.findall(r'^(?:\n|.)*DATA((\n|.)*?)$', content)
import string, re
s = '234B325b234'
print re.findall(r'[b|B]', s)
print s.replace('[b|B]', 'b,')
print string.replace(s, 'b', 'Geng Jie')
