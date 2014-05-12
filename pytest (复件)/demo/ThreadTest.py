__author__ = 'gengjie'
import threading
import time
import random
import Queue

queue = Queue.LifoQueue()
START = 0
SUSPEND = 1
CONTINUE = 2
EXIT = 4
# queue.put('start')
# queue.put('suspend')
# queue.put('exit')

class Counter(object):
    def __init__(self):
        self.lock = threading.Lock()
        self.value = 0

    def increment(self):
        self.lock.acquire()
        self.value += 1
        self.lock.release()
        return self.value


counter = Counter()

event = threading.Event()


class Worker(threading.Thread):
    def run(self):
        super(Worker, self).run()
        while 1:
            for i in range(1000):
                if event.isSet():
                    value = counter.increment()
                    time.sleep(random.randint(10, 100) / 1000)
                    print self.getName(), i, value
                elif queue.get() == SUSPEND:
                    while True:
                        if queue.get() == CONTINUE:
                            break
                        time.sleep(1.0 / 1000.0)
                elif queue.get() == EXIT:
                    break
                else:
                    pass


for i in range(10):
    Worker().start()