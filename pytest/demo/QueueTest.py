__author__ = 'gengjie'
import threading
import time
import random
import Queue

WORKERS = 3

queue = Queue.Queue(2)
queue1 = Queue.LifoQueue(0)
queue2 = Queue.PriorityQueue(0)

# for j in range(10):
#     print queue.get()

class Worker(threading.Thread):
    def __init__(self, queue):
        self.__queue = queue
        threading.Thread.__init__(self)

    def run(self):
        while 1:
            value = self.__queue.get()
            if value is None:
                break
            else:
                print 'get %d' % value
                time.sleep(random.randint(100, 1000) / 100)


for i in range(WORKERS):
    Worker(queue).start()

for i in range(10):
    queue.put(i)
    print 'put %d' % i

for j in range(WORKERS):
    queue.put(None)