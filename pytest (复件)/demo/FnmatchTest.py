__author__ = 'gengjie'
import fnmatch
import os

for file in os.listdir("."):
    if fnmatch.fnmatch(file, "S*.py"):
        print file