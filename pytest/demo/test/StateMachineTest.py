__author__ = 'gengjie'
import time
import Queue
import random
import threading
'''
    Traffic Light Mode
    RED -> GREEN -> BLUE
'''
LIGHT_STATE = ['RED', 'GREEN', 'YELLOW']

def set_color(color):
    print 'current color is set to', color
    time.sleep(1.0 / 2)

def work(state):
    if state == 'RED':
        set_color(state)
        next_state = 'GREEN'
        work(next_state)
    elif state == 'GREEN':
        set_color(state)
        next_state = 'YELLOW'
        work(next_state)
    elif state == 'YELLOW':
        set_color(state)
        next_state = 'RED'
        work(next_state)

# while 1:
r = random.randint(0, 2)
print r
# work(LIGHT_STATE[r])

class Worker(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.condition = threading.Condition()
        self.is_waiting = False
        self.counter = 0

    def suspend(self):
        if not self.is_waiting:
            self.is_waiting = True

    def resume(self):
        if self.is_waiting:
            self.condition.notifyAll()

    def run(self):
        self.condition.acquire()
        while True:
            if self.is_waiting:
                self.condition.wait()
            self.counter += 1
            print self.counter
            time.sleep(1.0/10.0)
        self.condition.release()

w = Worker()
w.start()
time.sleep(5)
w.suspend()
time.sleep(5)
w.resume()