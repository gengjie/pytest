__author__ = 'gengjie'
import zlib

file = open("./test.z", "r")
line = file.readline()
file.close()
print line, repr(line)
decompressStr = zlib.decompress(line)
print repr(decompressStr)