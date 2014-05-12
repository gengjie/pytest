__author__ = 'gengjie'
import types


class TypeCheck(object):
    def __init__(self, object):
        self.object = object

    def check(self):
        if type(self.object) is types.BooleanType:
            print 'Boolean'
        elif type(self.object) is types.ClassType:
            print 'Class'
        elif type(self.object) is types.ObjectType:
            print 'Object'
        elif type(self.object) is types.StringType:
            print 'String'
        else:
            print type(self.object)


if __name__ == '__main__':
    TypeCheck(TypeCheck).check()
    TypeCheck('123').check()
    TypeCheck(TypeCheck('123')).check()
    tc = TypeCheck(123)
    TypeCheck(object).check()