__author__ = 'gengjie'
import threading, time

conn = threading.Condition()
def calculate():
    global s
    global i
    global status
    conn.acquire()
    while 1:
        if status == 'SUSPEND':
            pass
        elif status == 'TERMINATED':
            print 'Final Result: %d' % s
            break
        else:
            if status == 'RESUME':
                conn.notifyAll()
            i += 1
            s += i
            print s
            time.sleep(1)
    threading.Condition().release()

if __name__ == '__main__':
    s = 0
    i = 0
    status = None
    threading.Thread(target=calculate).start()
    time.sleep(5)
    print '-'*20
    status = 'SUSPEND'
    conn.wait()
    time.sleep(5)
    print '-'*20
    status = 'RESCUME'
    conn.notifyAll()
    time.sleep(5)
    print '-'*20
    status = 'TERMINATED'