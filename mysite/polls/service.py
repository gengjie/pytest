__author__ = 'gengjie'
from django.db import connection

def my_custom_sql():
    from django.db import connection, transaction
    cursor = connection.cursor()
    cursor.execute("select count(*) from auth_user")
    fetchall = cursor.fetchall()
    print fetchall

my_custom_sql()