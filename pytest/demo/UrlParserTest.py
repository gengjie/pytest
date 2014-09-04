#! /usr/bin/env python
# coding=utf-8
__author__ = 'gengjie'
import urlparse
import string
import urllib
url = 'http://www.baidu.com/s?tn=baiduhome_pg&ie=utf-8&bs=python+StringIO&f=3&rsv_bp=1&rsv_spt=1&wd=python+subprocess&rsv_sug3=4&rsv_sug4=618&rsv_sug1=3&oq=python+sub&rsv_sug2=0&rsp=0&inputT=8592'
'''''
Usage for urlparse.urlparse(url):
    <scheme>://<netloc>/<path>;<params>?<query>#<fragment>
    Return a 6-tuple: (scheme, netloc, path, params, query, fragment).
'''''
elements = urlparse.urlparse(url)
for e in elements:
    print e

host = 'http://192.168.1.1:8080/'
print string.split(host, ':', 1)

u = urllib.pathname2url("http://localhost:8080?param=萨达发打法")
#params = (('uname', '11'), ('passw', '22'),)
params = {'uname':'11', "passw":'22'}
print urllib.urlencode(params)
print u