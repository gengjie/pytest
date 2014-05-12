__author__ = 'gengjie'
import base64

f = open("./pickle.bin", "rb")
buf = f.read()
txt = base64.encodestring(buf)
print base64.decodestring(txt)
f.close()
print buf

base64.encode(open("./pickle.bin", "rb"), open("./pickle.b64", "w"))
# base64.decode(open("pickle.b64", "r"), open("pickle.bin"))
