__author__ = 'gengjie'
import MySQLdb
import time

MAX_CONNECTION_NUM = 40
TIMEOUT = 5


class DBUtils:
    def __init__(self, host, port, user, passwd, db):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.db = db
        self.connections = {}
        if len(self.connections) == 0:
            self.__createpool__()

    def __createpool__(self):
        for id in range(MAX_CONNECTION_NUM):
            connection = MySQLdb.Connection(host=self.host, user=self.user, passwd=self.passwd, db=self.db,
                                            port=self.port)
            self.connections[connection] = (id + 1, True)

    def getconnection(self):
        for conn, (_id, _status) in self.connections.items():
            if _status:
                self.connections[conn] = (_id, False)
                return conn
        time.sleep(TIMEOUT)
        return None
        self.getconnection()

    def close(self, conn):
        self.connections[conn] = (self.connections[conn][0], True)


pool = DBUtils(host='localhost', user='root', passwd='njjndsgj', db='test', port=3306)
for i in range(80):
    print i, pool.getconnection()