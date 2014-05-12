__author__ = 'gengjie'
from datetime import *
import time
import dateutil.parser

print repr(dateutil.parser.parse('2008-09-26T01:51:42.456Z'))

now = time.time()
print date.today(), now
print time.localtime(now)

print time.strftime('%04Y-%02m-%02d %02H:%02M:%02S,%SSS %Z')

t = time.strptime("2004-01-01 20:08:00 CST", "%Y-%m-%d %H:%M:%S %Z")
print t, repr(t), t.tm_wday, t.tm_mday


def procedure():
    time.sleep(3.0)


t0 = time.clock()
print t0
procedure()
duration = time.clock() - t0

print duration

print datetime.now() - timedelta(days=1)