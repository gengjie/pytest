__author__ = 'gengjie'
import random

print random.random()
print random.randint(1, 100)
print random.uniform(10, 20)
print random.randrange(1, 100, 10)

list = [1, 2, 3, 4, 5]

for i in range(5):
    dst = random.choice(list)
    list.remove(dst)
    print dst