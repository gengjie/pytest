__author__ = 'gengjie'
import commands

stat, outputs = commands.getstatusoutput("ls -1R | grep test")
print stat
print outputs