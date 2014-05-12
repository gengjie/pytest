# demo for dir(), vars()
__author__ = 'gengjie'


class A(object):
    def function1(self):
        pass

    def function2(self):
        pass

    def testvars(self):
        a = 1
        b = 2
        # print(a + b)
        c = a + b
        print "%(a)d + %(b)d = %(c)d" % vars()

    def getType(self, var):
        self.var = var
        print 'the type of %s is %s' % (self.var, type(self.var))

    def testeval(self, expression):
        return eval(expression)


class B(A):
    pass


if __name__ == '__main__':
    modules = []
    clazzModules = dir(A)
    for m in clazzModules:
        if m not in modules:
            modules.append(m)
        print(m)
    print(modules)

    clazzA = A()
    clazzA.testvars()
    clazzA.getType('one')

    classB = B()

    print(isinstance(classB, A))
    print(isinstance(classB, B))
    print(issubclass(B, A))
    print(issubclass(A, B))
    print(issubclass(A, object))

    ret = clazzA.testeval('1+1')
    print(ret)
    print(clazzA.testeval("__import__('os').getcwd()"))

    # execfile usage:
    execfile('DateTest.py')
