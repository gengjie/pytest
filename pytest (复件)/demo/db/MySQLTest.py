# /usr/bin/env python
# coding=utf-8
__author__ = 'gengjie'
import MySQLdb

# charset='utf-8'
conn = MySQLdb.connect(host='localhost', user='root', passwd='njjndsgj', db='test', port=3306)
# conn.set_character_set('utf-8')
cur = conn.cursor()
cur.execute('select * from test')
results = cur.fetchone()
print results
results = cur.fetchmany(20)
print results
cur.scroll(0, mode='absolute')
results = cur.fetchall()
for index, value in results:
    if index == 99:
        print index, str(value).decode('latin1').encode('utf-8')
    else:
        print index, str(value).decode('utf-8'), value
print results
sql = 'create table if not exists test (id int(32) primary key auto_increment, name varchar(40))'
cur.execute(sql)
values = []
for i in range(20):
    values.append((i, 'hi for u陈道明' + str(i)))
cur.executemany('insert into test (name) values(%s)', values[:][1])
cur.close()
conn.commit()
print repr(conn)
conn.close()