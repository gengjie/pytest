__author__ = 'gengjie'
import copy

a = [[1], [2], [3]]
b = copy.copy(a)
c = copy.deepcopy(a)

a[0][0] = 0
a[1] = None

print a, b, c