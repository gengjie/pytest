__author__ = 'gengjie'
import threading
import time
from multiprocessing import Process
import multiprocessing

num = multiprocessing.Value('d', 0)

def run(num):
    while True:
        num.value += 1
        time.sleep(5)
        # print num

def refresh(num):
    # global num
    while True:
        time.sleep(1)
        print num.value

# threading.Thread(target=run).start()
# # threading.Thread(target=refresh()).start()
# refresh()

p1 = Process(target=run, args=(num,))
p2 = Process(target=refresh, args=(num,))
p1.start()
p2.start()

# class T(threading.Thread):
#     def __init__(self):
#         threading.Thread.__init__(self)
#
#     def getValue(self):
#         return [1, 2, 3]
#
#     def run(self):
#         global thms
#         i = 0
#         while True:
#             # num.append(self.getValue())
#             # time.sleep(2)
#             thms = self.getValue()
#             time.sleep(60)
#             i += 1
#             # break
#             # print num
#
# if __name__ == '__main__':
#     thms = []
#     t = T()
#     t.start()
#     # while True:
#     time.sleep(2)
#     print thms