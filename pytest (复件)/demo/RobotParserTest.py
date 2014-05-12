__author__ = 'gengjie'
import robotparser
import urllib2

proxy_info = {'host': '139.24.236.123',
              'port': 8080,
              'user': 'z0033cha',
              'pass': 'temp$WIN2000'
}
proxy_support = urllib2.ProxyHandler({"https": "http://%(user)s:%(pass)s@%(host)s:%(port)d" % proxy_info})
opener = urllib2.build_opener(proxy_support)
urllib2.install_opener(opener)
fp = urllib2.urlopen('https://www.google.com.hk/robots.txt', timeout=3)
lines = fp.readlines()
print lines
rp = robotparser.RobotFileParser()
rp.parse(lines)
print rp.can_fetch('*', '/search')
fp.close()