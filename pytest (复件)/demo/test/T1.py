__author__ = 'gengjie'
class T1(object):
    def handle(self):
        print 'T1'
        print self.__class__.__name__

    def do(self, text):
        print 't1-do'
        print text

class T2(T1):
    def do(self):
        print 't2-do'
        T1.do(self, 'sdf')


t2 = T2()
t2.handle()
t2.do()