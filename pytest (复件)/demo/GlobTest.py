__author__ = 'gengjie'
import glob
import os

files = []
files = glob.glob("/home/gengjie/python/*.py")
print files

for file in files:
    print file, os.path.split(file)[1]

