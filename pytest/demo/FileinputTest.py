__author__ = 'gengjie'

import fileinput
import sys

lines = fileinput.input('/home/gengjie/index.html')

for line in lines:
    sys.stdout.write('->')
    sys.stdout.write(line)