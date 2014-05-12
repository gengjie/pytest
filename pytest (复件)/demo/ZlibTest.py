__author__ = 'gengjie'
import zlib

MESSAGE = "Merry Christmas"

print repr(MESSAGE)

print repr(zlib.compress(MESSAGE))

print repr(zlib.decompress(zlib.compress(MESSAGE)))

file = open("./test.z", "w+")
file.write(zlib.compress(MESSAGE))
file.flush()
file.close()