__author__ = 'gengjie'
# class variable, instance member variable
class Demo(object):
    field1 = 123
    field2 = 'str'

    def __init__(self):
        self.field3 = '55'

    def do_something(self):
        print self.field1

    def __private(self):
        print 'private'

    @staticmethod
    def do_static(param):
        print 88, param
        print Demo.field1

    @classmethod
    def do_cls(cls):
        print cls.field1

if __name__ == '__main__':
    d = Demo()
    print '\n'.join(dir(Demo))
    d.do_something()
    #d.__private()
    d._Demo__private();
    print Demo.field1
    print d.field3
    Demo.do_static(88)
    d.do_cls()