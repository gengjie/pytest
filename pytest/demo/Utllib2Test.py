#!/usr/bin/env python
# _*_coding=utf-8_*_
__author__ = 'gengjie'
import urllib2
import urllib
# proxy_handler = urllib2.ProxyHandler({'http': 'http://139.24.236.123:8080'})
# proxy_auth_handler = urllib2.ProxyBasicAuthHandler()
# proxy_auth_handler.add_password('realm', 'host', 'z0033cha', 'temp$WIN2000')
#
# opener = urllib2.build_opener(proxy_handler, proxy_auth_handler)
# # This time, rather than install the OpenerDirector, we use it directly:
# opener.open('http://www.example.com/login.html')

# Create an OpenerDirector with support for Basic HTTP Authentication...
# auth_handler = urllib2.HTTPBasicAuthHandler()
# auth_handler.add_password(realm='cn001',
#                           uri='http://139.24.236.123:8080',
#                           user='z0033cha',
#                           passwd='temp$WIN2000')
# opener = urllib2.build_opener(auth_handler)
# # ...and install it globally so it can be used with urlopen.
# urllib2.install_opener(opener)
# urllib2.urlopen('http://www.qq.com', timeout=5)

proxy_info = {'host': '139.24.236.123',
              'port': 8080,
              'user': 'z0033cha',
              'pass': 'temp$WIN2000'
}
proxy_support = urllib2.ProxyHandler({"http": "http://%(user)s:%(pass)s@%(host)s:%(port)d" % proxy_info})
opener = urllib2.build_opener(proxy_support)
urllib2.install_opener(opener)
response = urllib2.urlopen("http://start.linuxdeepin.com/zh_CN/img/start3_01.gif", timeout=2)
print response.info()
print response.info().getheaders('Content-Length')[0]
htmlpage = response.read(200000)
# htmlpage = htmlpage.decode('gb2312').encode('utf-8')
print htmlpage


'''
实现通过urllib2提交post请求
'''
# url = 'https://login.xiami.com/member/login'
# data = {'email': 'jgeng@foxmail.com', 'password': 'njjndsgj', 'autologin': '1', 'submit': '登 录', 'type': ''}
# # data = ('email', 'jgeng@foxmail.com'), ('password', 'njjndsgj')
# # request = urllib2.Request(url)
# data = urllib.urlencode(data)
# print data
# urllib2.build_opener(urllib2.HTTPCookieProcessor())
# response = urllib2.urlopen(url, data, timeout=3)
# print response.info()
# print response.read()