__author__ = 'gengjie'
import sys
import os

paths = []
paths = sys.path
print sys.path

for p in paths:
    print p

print len(paths)

print sys.modules.keys()

print os.name, sys.platform

try:
    sys.exit(1)
except SystemExit:
    pass
print 'still running...'
