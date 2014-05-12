__author__ = 'gengjie'
import array
import sys

a = array.array('B', range(16))

t = (1, 2, 3, 4, 5,)
print array.array('b', t).tolist()

print repr(a.tostring())

b = array.array("i", "helloworldhelloworld")
print b, type(b)
print b.tolist()

RULES = '''Type code	C Type	    Python Type	Minimum size in bytes
                'c'	    char	    character	1
                'b'	    signed char	int	1
                'B'	    unsigned  char	int	1
                'u'	    Py_UNICODE	Unicode character	2 (see note)
                'h'	    signed short	int	2
                'H'	    unsigned short	int	2
                'i'	    signed int	int	2
                'I'	    unsigned int	long	2
                'l'	    signed long	int	4
                'L'	    unsigned long	long	4
                'f'	    float	float	4
                'd'	    double	float	8'''

# file = open('./rules.txt', 'w+')
# print RULES
#
# rows = string.split(RULES, '\n')
# for row in rows:
#     columns = string.split(row, '\t')
#     for column in columns:
#         if len(column) < 21:
#             column += ' '*(21 - len(column))
#         print column, '\t',
#         file.write(column)
#     print
#     file.write('\n')
# file.flush()
# file.close()

print sys.byteorder

print type(range(10))