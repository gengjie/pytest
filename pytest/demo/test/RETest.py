__author__ = 'gengjie'
f = open('test.txt', 'r')
lines = f.readlines()
for line in lines:
    import re
    if re.match(r'^.*(?!(abc|def)).*$', line):
        print line