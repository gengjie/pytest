__author__ = 'gengjie'
import hashlib

m = hashlib.md5()
m.update('GengJie')
print repr(m.digest())
print m.hexdigest()

m.update('gengjie')
print m.hexdigest()

print hashlib.sha384('gengjie').hexdigest()
print hashlib.sha512('gengjie').hexdigest()