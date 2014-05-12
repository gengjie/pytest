__author__ = 'gengjie'
import getpass

user = getpass.getuser()
pwd = getpass.getpass("enter password for user %s:" % user)

print user, pwd
