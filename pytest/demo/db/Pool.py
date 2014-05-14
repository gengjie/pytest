#!/usr/bin/python
#coding=UTF-8
# Mysql 数据库连接池
# allan 2009-04-28
import thread
import time
import MySQLdb
import MySQLdb.cursors

lock = thread.allocate_lock()


class Pool:
    DEFAULT_EXPIRY = 600

    def help(self):
        print('''
    usage:
        import MysqlDatabasePool
        pool = MysqlDatabasePool.Pool('host', 'user', 'passwd', 'db')
        conn = pool.connection()     # get a connection
        #################            # execute some sql here
        pool.close(conn)             # close the connection
        print(pool.status())         # show some status
        ''')

    def connection(self):
        lock.acquire()
        try:
            for connection, status in self.____connections.items():
                lastUseTime = status['lastUseTime']
                isFree = status['isFree']
                if isFree:
                    self.____connections.update({connection: {"lastUseTime": 0.0, "isFree": False}})
                    return connection
            newConn = self.________getNewConnection()
            self.____connections[newConn] = {"lastUseTime": 0.0, "isFree": False}
            return newConn
        finally:
            lock.release()

    def close(self, conn):
        lock.acquire()
        try:
            status = self.____connections[conn]
            if status == None:
                conn.close()
            else:
                self.____connections.update({conn: {"lastUseTime": time.time(), "isFree": True}})
        finally:
            lock.release()

    def status(self):
        result = ""
        count = 0
        for connection, status in self.____connections.items():
            count = count + 1
            result = result + str(connection) + ": " + str(status) + "\n"
        result = result + str(count) + " connection(s)."
        return result;

    def __init__(self, host, user, password, databaseName):
        self.____host = host
        self.____user = user
        self.____password = password
        self.____databaseName = databaseName
        self.____connections = {}  # key:connection, value: {"lastUseTime":$timestamp$, "isFree":$bool$}
        self.close(self.connection())  # make a test
        thread.start_new_thread(self.________periodicallyClean, ())

    def ________getNewConnection(self):
        return MySQLdb.Connection(host=self.____host, user=self.____user, passwd=self.____password,
                                  db=self.____databaseName, cursorclass=MySQLdb.cursors.DictCursor)

    def ________periodicallyClean(self):
        scanInterval = self.DEFAULT_EXPIRY / 2.0
        while True:
            time.sleep(scanInterval)
            self.________clean()

    def ________clean(self):
        lock.acquire()
        try:
            expireTime = time.time() - self.DEFAULT_EXPIRY
            for connection, status in self.____connections.items():
                lastUseTime = status['lastUseTime']
                isFree = status['isFree']
                if isFree:
                    if lastUseTime < expireTime:
                        self.____connections.pop(connection)
                        connection.close()
        finally:
            lock.release()