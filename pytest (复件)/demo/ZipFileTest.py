__author__ = 'gengjie'
import zipfile
import os
import glob

'''
    this part is the demo for reading from zip files
'''
# file = zipfile.ZipFile("./kwplayer-master.zip", "r")
# for name in file.namelist():
#     print name
#     content = file.read(name)
#     print repr(content)
#
# for info in file.infolist():
#     print os.path.split(info.filename)[-1], info.file_size

'''
    this part shows how to write files into zip file
'''
z = open("/home/gengjie/output.zip", "w+")
zf = zipfile.ZipFile("/home/gengjie/output.zip", "w")
currentPath = os.path.abspath("../")
files = glob.glob(currentPath + "/*/*")
for f in files:
    print f
    # zf.write(f, "/python/" + os.path.basename(f), zipfile.ZIP_STORED)
    zf.write(f, "/python/" + os.path.abspath(f).split('/', 4)[4], zipfile.ZIP_STORED)
zf.close()

'''
    this part shows how to exact zip file into a specified dictionary
'''
zf = zipfile.ZipFile("/home/gengjie/output.zip")
zf.printdir()
zf.extractall("/home/gengjie/output/")
