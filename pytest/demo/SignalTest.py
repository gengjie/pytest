__author__ = 'gengjie'
import signal
import time


def handle(signo, frame):
    print "start to handle something...", signo, frame


signal.signal(signal.SIGALRM, handle)
signal.alarm(2)
now = time.time()
time.sleep(4000)

print time.time() - now