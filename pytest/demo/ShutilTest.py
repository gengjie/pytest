__author__ = 'gengjie'
import os

BACKUP_DICTIONARY = '/home/gengjie/backup/'

for file in os.listdir('.'):
    print file
    suffix = os.path.splitext(file)[1]
    if '.py' == suffix:
        print os.path.join('/home/gengjie/backup/', file)
        # copy files from src to dst dictionary
        # shutil usage: shutil.copy(src, dst)
        # shutil.copy(file, os.path.join(BACKUP_DICTIONARY, file))

for file2 in os.listdir(BACKUP_DICTIONARY):
    print file2
