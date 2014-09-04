__author__ = 'gengjie'
import copy

a = [[1], [2], [3]]
b = copy.copy(a)
''''shallow copy: just copy the parent object'''
'''deep copy: copy both parent and child object'''
c = copy.deepcopy(a)

print a, b, c

a[0][0] = 0

print a, b, c

a[1] = None

print a, b, c

