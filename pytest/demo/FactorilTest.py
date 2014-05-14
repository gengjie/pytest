__author__ = 'gengjie'

stack = []


def factoril(n):
    if n > 1:
        return n * factoril(n - 1)
    else:
        return 1


for i in range(0, 1000, 1):
    print factoril(i)


def factorils(n):
    stack.append(n)
    total = 1
    temp = stack.pop()
    while temp != 1:
        total *= temp
        temp -= 1
        stack.append(temp)
    return total


print factorils(4)