__author__ = 'gengjie'
import os
import time

files = []
files = os.listdir('/home/gengjie')
textfiles = []
hiddenfiles = []
for file in files:
    if file.endswith('.txt'):
        textfiles.append(file)
    elif file.startswith('.'):
        hiddenfiles.append(file)
    else:
        pass
        # print('-----------------> %s' %(file))
        # print(file)


def listallfiles(fs):
    import stat

    for f in fs:
        print f, type(f)
        st = os.stat("/home/gengjie/" + f)
        mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime = st
        print "- size:", size, "bytes"
        print "- owner:", uid, gid
        print "- created:", time.ctime(ctime)
        print "- last accessed:", time.ctime(atime)
        print "- last modified:", time.ctime(mtime)
        print "- mode:", oct(mode)
        print "- inode/dev:", ino, dev
        print st[stat.ST_MODE]


listallfiles(textfiles)
listallfiles(hiddenfiles)

cwd = os.getcwd()
print cwd
os.chdir("/")
print os.getcwd()
print os.pardir
os.chdir(os.pardir)
print os.getcwd()
print os.name
os.system('ls -l')


def run(program, *args):
    pid = os.fork()
    if not pid:
        print '===>'
        os.execvp(program, (program, ) + args)
        return os.wait()[0]


def spawn(program, *args):
    try:
        return os.spawnvp(program, *args)
    except AttributeError:
        pass
    try:
        spawnvp = os.spawnvp
    except AttributeError:
        run(program, *args)


run("wget", "www.ifeng.com")

print os.pathsep
print os.environ

for key, value in os.environ.items():
    print key, '\t', value
# os.system("wget www.ifeng.com")

print os.fork()
print os.name

filename = '/home/gengjie/data.txt'
print os.path.split(filename)
name = os.path.split(filename)[1]
print name
print os.path.splitext(filename)
sufix = os.path.splitext(filename)[1]
print sufix
print os.path.dirname(filename)
print os.path.basename(filename)
print '----------------------------------------'


def callback(arg, dictionary, _files):
    for f in _files:
        print dictionary, f, arg
        filepath = os.path.join(dictionary, f)
        print filepath
        # filePath =
    return None


os.path.walk('/home/gengjie/python', callback, 'some message')

for _tuple in os.walk('/home/gengjie/python'):
    for item in _tuple:
        print item


def index(dictionary):
    stack = [dictionary]
    filelist = []
    while stack:
        dictionary = stack.pop()
        for fileitem in os.listdir(dictionary):
            fullname = os.path.join(dictionary, fileitem)
            if os.path.isdir(fullname) and not os.path.islink(fullname):
                stack.append(fullname)
            else:
                filelist.append(fullname)
    return filelist


for fitem in index('/home/gengjie/'):
    print fitem

    # os.rmdir()