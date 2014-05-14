__author__ = 'gengjie'

stack1 = []
stack2 = []


def pow(x, n):
    stack1.append(x)
    stack2.append(n)
    temp = stack2.pop()
    total = stack1[0]
    while temp != 1:
        total *= stack1[0]
        temp -= 1
        stack2.append(temp)
    return total


print pow(2, 100000)