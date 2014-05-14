import time
import threading

__author__ = 'gengjie'


class InsertEvent(object):
    def __init__(self, data):
        self.data = data

    def handleInsertEvent(self):
        print '-' * 10, '>', self.data


class DataModifiedListener(object):
    def fireDataEvent(self, event):
        if isinstance(event, InsertEvent):
            event.handleInsertEvent()


class DataManager(DataModifiedListener):
    dm = None

    def __init__(self):
        self.lock = threading.Lock()

    def getinstance(self):
        try:
            self.lock.acquire()
            if DataManager.dm is None:
                DataManager.dm = DataManager()
                return DataManager.dm
            else:
                return DataManager.dm
        finally:
            self.lock.release()
            print DataManager.dm


def insert(data):
    time.sleep(10.0 / 20.0)
    e = InsertEvent(data)
    dm = DataManager().getinstance()
    print id(dm)
    dm.fireDataEvent(e)


for i in range(110):
    threading.Thread(target=insert(i)).start()
    # time.sleep(1)