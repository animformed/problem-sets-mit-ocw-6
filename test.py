#while True:                                     #using exception handlers
#        data = raw_input('Enter Text: ')
#        if data == 'stop': break
#        try:
#                num = int(data)
#        except:
#                print(data.upper()*4)
#        else:
#                print(num ** 2)
#print('Bye')

#L = [1, 2, 3, 4]
#while L:
#    front, L = L[0], L[1:]
#    print(front, L)

#x = raw_input('Enter number: ')
#x = int(x)
#while x > 0:
#    if x % 2 == 0:
#        print(x),
#    x -= 1
#x = int(raw_input('Enter a number: '))
#while x:
#    x -= 1
#    if x % 2 != 0:
#        continue
#    print(str(x) + ' '),

#x = int(raw_input('Enter a number: '))
#y = x // 2
#while y > 1:
#    if x % y == 0:
#        print 'x has a factor',
#        break
#    y = y - 1
#else:
#    print 'x is prime'
#File = open('test.txt, 'r')
#print File
#
#File = open('test.txt', 'r')
#for File in ope
#def fib(n):
#    if n == 0: return 0
#    if n == 1: return 1
#    return fib(n-1) + fib(n-2)
#
#print(fib(5))

#def fib2(n):
#    n2, n1 = 0, 1
#    for i in range(n-2):
#        n2, n1 = n1, n1 + n2
#    return n2+n1
#
#print(fib2(1))
#class Person:
#        def __init__(self, name, job=None, pay=0):
#                self.name = name
#                self.job = job
#                self.pay = pay
#        def lastName(self):
#                return self.name.split()[-1]
#        def giveRaise(self, percent):
#                self.pay = int(self.pay * (1 + percent))
#
#if __name__ == '__main__':
#        bob = Person('Bob Smith')
#        sue = Person('Sue Jones', job='dev', pay=100000)
#        print('{0} {1}'.format(bob.name, bob.pay))
#        print('{0} {1}'.format(sue.name, sue.pay))
#        print('{0} {1}'.format(bob.lastName(), sue.lastName()))
#        sue.giveRaise(.10)
#        print(sue.pay)
#        
#class Person:
#        def __init__(self, name, job=None, pay=0):
#                self.name = name
#                self.job = job
#                self.pay = pay
#        def lastName(self):
#                return self.name.split()[-1]
#        def giveRaise(self, percent):
#                self.pay = int(self.pay * (1 + percent))
#        def __str__(self):                                                      # Added overloaded method for print behaviour
#                return '[Person: {0} {1}]'.format(self.name, self.pay)
#if __name__ == '__main__':
#        bob = Person('Bob Smith')
#        sue = Person('Sue Jones', job='dev', pay=100000)
#        print(bob)
#        print(sue)
#        print('{0} {1}'.format(bob.lastName(), sue.lastName()))
#        sue.giveRaise(.10)
#        print(sue)
#class Person:
#        def __init__(self, name, job=None, pay=0):
#                self.name = name
#                self.job = job
#                self.pay = pay
#        def lastName(self):
#                return self.name.split()[-1]
#        def giveRaise(self, percent):
#                self.pay = int(self.pay * (1 + percent))
#        def __str__(self):                                                      
#                return '[Person: {0} {1}]'.format(self.name, self.pay)
#        
#class Manager(Person):                                                          # Make a subclass
#        def giveRaise(self, percent, bonus=0.10):                               # Override the giveRaise() method with the appropriate changes
#                Person.giveRaise(self, percent + bonus)
#                
#if __name__ == '__main__':
#        bob = Person('Bob Smith')
#        sue = Person('Sue Jones', job='dev', pay=100000)
#        print(bob)
#        print(sue)
#        print('{0} {1}'.format(bob.lastName(), sue.lastName()))
#        sue.giveRaise(.10)
#        print(sue)
#        tom = Manager('Tom Jones', 'mgr', 50000)
#        tom.giveRaise(.10)
#        print(tom.lastName())
#        print(tom)
#        print '--All three--'.format()
#        for obj in (bob, sue, tom):
#            obj.giveRaise(0.10)
#            print(obj)

#class Person:
#        def __init__(self, name, job=None, pay=0):
#                self.name = name
#                self.job = job
#                self.pay = pay
#        def lastName(self):
#                return self.name.split()[-1]
#        def giveRaise(self, percent):
#                self.pay = int(self.pay * (1 + percent))
#        def __str__(self):
#                return '[Person: {0}, {1}]'.format(self.name, self.pay)
#
#class Manager(Person):
#        def __init__(self, name, pay):
#                Person.__init__(self, name, 'mgr', pay)                         # We redefine constructor which automatically calls the 
#        def giveRaise(self, percent, bonus=0.10):                               # constructor from its superclass and passes in the 'mgr' as job
#                return Person.giveRaise(self, percent + bonus)
#
#if __name__ == '__main__':
#        bob = Person('Bob Smith')
#        sue = Person('Sue Jones', job='dev', pay=100000)
#        print(bob)
#        print(sue)
#        print('{0} {1}'.format(bob.lastName(), sue.lastName()))
#        sue.giveRaise(.10)
#        print(sue)
#        tom = Manager('Tom Jones', 50000)
#        tom.giveRaise(.10)
#        print(tom.lastName())
#        print(tom)

#class Person:
#        def __init__(self, name, job=None, pay=0):
#                self.name = name
#                self.job = job
#                self.pay = pay
#        def lastName(self):
#                return self.name.split()[-1]
#        def giveRaise(self, percent):
#                self.pay = int(self.pay * (1 + percent))
#        def __str__(self):
#                return '[Person: {0}, {1}]'.format(self.name, self.pay)
#
#class Manager(Person):
#        def __init__(self, name, pay):
#                Person.__init__(self, name, 'mgr', pay)                         
#        def giveRaise(self, percent, bonus=0.10):                               
#                return Person.giveRaise(self, percent + bonus)
#
#if __name__ == '__main__':
#        bob = Person('Bob Smith')
#        sue = Person('Sue Jones', job='dev', pay=100000)
#        print(bob)
#        print(sue)
#        print('{0} {1}'.format(bob.lastName(), sue.lastName()))
#        sue.giveRaise(.10)
#        print(sue)
#        tom = Manager('Tom Jones', 50000)
#        tom.giveRaise(.10)
#        print(tom.lastName())
#        print(tom)
#        bob.__class__
#        bob.__class__.__name__
#        bob.__dict__.keys()
#        for key in bob.__dict__:
#                print '{0} => {1}'.format(key, bob.__dict__[key])
#        for key in bob.__dict__:
#                print '{0} => {1}'.format(key, getattr(bob, key)) 

#"""Assorted class utilities and tools"""
#
#class AttrDisplay:
#    """
#    Provides an inheritable print overload method that displays
#    instances with their classes names and a name=value pair for
#    each attribute stored on the instance itself (but not attrs
#    inherited from its classes). Cna be mixed into any class,
#    and will work on any instance.
#    """
#    def gatherAttrs(self):
#        attrs = []
#        for key in sorted(self.__dict__):
#            attrs.append('{0}={1}'.format(key, getattr(self, key)))
#        return ','.join(attrs)
#    def __str__(self):
#        return '[{0}: {1}]'.format(self.__class__.__name__, self.gatherAttrs())
#    
#if __name__ == '__main__':
#    class TopTest(AttrDisplay):
#        count = 0
#        def __init__(self):
#            self.attr1 = TopTest.count
#            self.attr2 = TopTest.count + 1
#            TopTest.count += 2
#    class SubTest(TopTest):
#        pass
#                
#    X, Y = TopTest(), SubTest()
#    print(X)
#    print(Y)
#    
#class AttrDisplay:
#
#   
#    def gatherAttrs(self):
#        attrs = []
#        for key in sorted(self.__dict__):
#            attrs.append('{0}={1}'.format(key, getattr(self, key)))
#        return ','.join(attrs)
#    def __str__(self):
#        return '[{0}: {1}]'.format(self.__class__.__name__, self.gatherAttrs())
#    
#if __name__ == '__main__':
#    class TopTest(AttrDisplay):
#        count = 0
#        def __init__(self):
#            self.attr1 = TopTest.count
#            self.attr2 = TopTest.count + 1
#            TopTest.count += 2
#        def gatherAttrs(self):
#            return 'Spam'
#    class SubTest(TopTest):
#        pass
#                
#    X, Y = TopTest(), SubTest()
#    print(X)
#    print(Y)

#class AttrDisplay:
#
#        def gatherAttrs(self):
#                attrs = []
#                for key in sorted(self.__dict__):
#                        attrs.append('{0} = {1}'.format(key, getattr(self, key)))
#                return ', '.join(attrs)
#        def __str__(self):
#                return '[{0}: {1}]'.format(self.__class__.__name__, self.gatherAttrs())
#
#class Person(AttrDisplay):
#        def __init__(self, name, job=None, pay=0):
#                self.name = name
#                self.job = job
#                self.pay = pay
#        def lastName(self):
#                return self.name.split()[-1]
#        def giveRaise(self, percent):
#                self.pay = int(self.pay * (1 + percent))
#
#class Manager(Person):
#        def __init__(self, name, pay):
#                Person.__init__(self, name, 'mgr', pay)
#        def giveRaise(self, percent, bonus = 0.10):
#                Person.giveRaise(self, percent + bonus)
#
#if __name__ == '__main__':
#        bob = Person('Bob Smith')
#        sue = Person('Sue Jones', job='dev', pay=100000)
#        print(bob)
#        print(sue)
#        print('{0} {1}'.format(bob.lastName(), sue.lastName()))
#        sue.giveRaise(.10)
#        print(sue)
#        tom = Manager('Tom Jones', 50000)
#        tom.giveRaise(.10)
#        print(tom.lastName())
#        print(tom)             
#from person import Person, Manager      # Storing the classes Person, Manager in a file (.py) and importing them
#bob = Person('Bob Smith')
#sue = Person('Sue Jones', job='dev', pay=100000)
#tom = Manager('Tom Jones', 50000)
#
#import shelve                           # importing shelve module from standard library
#db = shelve.open('persondb')            # filename when objects are stored
#for obj in (bob, sue, tom):             # store object's name attr as key
#        db[obj.name] = obj              # store obj on shelve by key
#db.close()

#import glob
#print glob.glob('person*')
#
#import shelve
#db = shelve.open('persondb')
#print len(db)
#print db.keys()
#print db['Bob Smith']
#bob = db['Bob Smith']
#print (bob)
#print bob.lastName()
#
#for key in db:
#    print '{0} => {1}'.format(key, db[key])
#    
#for key in sorted(db, reverse=True):
#    print '{0} => {1}'.format(key, db[key])    
#    
#print db

#import shelve
#db = shelve.open('persondb')
#
#for key in db:
#    print '{0} => {1}'.format(key, db[key])
#    
#sue = db['Sue Jones']
#
#sue.giveRaise(0.10)
#db['Sue Jones'] = sue
#for key in db:
#    print '{0}\t=> {1}'.format(key, db[key])
#db.close()

#class Super:
#        def method(self):
#                print('in Super method')                # default behaviour
#        def delegate(self):
#                self.action()                           # Expect to be defined
#        
#class Inheritor(Super):                                 # Inherit method verbatim
#        pass
#
#class Replacer(Super):
#        def method(self):
#                print('in Replacer.method')             # Redefine or override Super.method()
#
#class Extender(Super):                                  
#        def method(self):                               # Extend method behaviour
#                print('starting Extender.method')
#                Super.method(self)
#                print('ending Extender.method')
#
#class Provider(Super):
#        def action(self):                               # Fill in a required method called in Super
#                print('in Provider.action')
#
#if __name__ == '__main__':
#        for klass in (Inheritor, Replacer, Extender):
#                print('\n' + klass.__name__ + '.....')
#                print klass;print klass()
#                klass().method()
#        print('\nProvider...')
#        x = Provider()
#        x.delegate()
        
#class Super:
#    def delegate(self):
#        self.action()
#    def action(self):
#        raise NotImplementedError('action must be defined !')
#
#X = Super()
#X.delegate()

#def classtree(cls, indent):
#        print('.' * indent + cls.__name__)              # print class name here
#        for supercls in cls.__bases__:
#                classtree(supercls, indent + 3)
#
#def instancetree(inst):
#        print('Tree of %s' % inst)                      # show instance
#        classtree(inst.__class__,3)                     # climb to its class
#
#class Emp: pass
#
#class Person(Emp): pass
#
#bob = Person()
#
#instancetree(bob)
#def selftest():
#        class A:        pass
#        class B(A):     pass
#        class C(A):     pass
#        class D(B, C):  pass
#        class E:        pass
#        class F(D, E):  pass
#        instancetree(B())
#        instancetree(F())
#if __name__ == '__main__':
#        selftest()
#import docstr
# 
#print docstr.__doc__     
#
#print docstr.func.__doc__
#
#print docstr.spam.__doc__
#
#print docstr.spam.method.__doc__  
#
#help(docstr)

#class SkipIterator:
#    def __init__(self, wrapped):
#        self.wrapped = wrapped
#        self.offset = 0
#    def next(self):
#        if self.offset >= len(self.wrapped):
#            raise StopIteration
#        else:
#            item = self.wrapped[self.offset]
#            self.offset += 2
#            return item
#class SkipObject:
#    def __init__(self, wrapped):
#        self.wrapped = wrapped
#    def __iter__(self):
#        return SkipIterator(self.wrapped)
#    
#if __name__ == '__main__':
#    alpha = 'Abcdef'
#    skipper = SkipObject(alpha)
#    I = iter(skipper)
#    print (next(I), next(I), next(I))
#    
#    for x in skipper:
#        for y in skipper:
#            print (x + y),

#class Iters:
#    def __init__(self, value):
#        self.data = value
#    def __getitem__(self, item):                    # Fallback for iteration
#        print ('get[{0}]:'.format(item)),              # Also for index, slice
#        return self.data[item]
#    def __iter__(self):                             # Preferred for iteration
#        print ('iter=>'.format()),                  # Allows only 1 active iterator
#        self.ix = 0
#        return self
#    def next(self):
#        print 'next:',
#        if self.ix == len(self.data):
#            raise StopIteration
#        item = self.data[self.ix]
#        self.ix += 1
#        return item
#    def __contains__(self, x):                      # Preferred for 'in'
#        print 'contains: ',
#        return x in self.data
    
#X = Iters([1, 2, 3, 4, 5])                          # Make instance
#print(3 in X)                                       # Membership
#for i in X:                                         # For loops
#    print ('{0} |'.format(i)),
#
#print()                                             # To get a newline
#print([i**2 for i in X])                            # Other iteration contexts
#print map(bin, X)                                   # map binary conversion to sequence items
#
#I = iter(X)
#while True:                                         # Manual iteration (what other contexts do)
#    try:
#        print ('{0} @'.format(next(I))),
#    except StopIteration:
#        break
#X = Iters('Spam')
#print X[0]
#print 'Spam'[1:]
#print 'Spam'[slice(1, None)]
#print X[1:] 
#print X[:-1]   

#class Employee:
#        def __init__(self, name, salary=0):
#                self.name = name
#                self.salary = salary
#        def giveRaise(self, percent):
#                self.salary = int(self.salary + (self.salary * percent))
#        def work(self):
#                print '{0} does stuff'.format(self.name)
#        def __repr__(self):
#                return '<Employee: name={0}, salary={1}>'.format(self.name, self.salary)
#
#class Chef(Employee):
#        def __init__(self, name):
#                Employee.__init__(self, name, 50000)
#        def work(self):
#                print '{0} makes food'.format(self.name)
#
#class Server(Employee):
#        def __init__(self, name):
#                Employee.__init__(self, name, 40000)
#        def work(self):
#                print '{0} interfaces with customer'.format(self.name)
#
#class PizzaRobot(Chef):
#        def __init__(self, name):
#                Chef.__init__(self, name)
#        def work(self):
#                print '{0} makes pizza'.format(self.name)
#
#if __name__ == '__main__':
#        bob = PizzaRobot('bob')
#        print(bob)
#        bob.work()
#        bob.giveRaise(0.20)
#        print(bob); print('\n'),
#
#        for klass in (Employee, Chef, Server, PizzaRobot):
#                obj = klass(klass.__name__)
#                obj.work() 

#class Employee:
#        def __init__(self, name, salary=0):
#                self.name = name
#                self.salary = salary
#        def giveRaise(self, percent):
#                self.salary = int(self.salary + (self.salary * percent))
#        def work(self):
#                print '{0} does stuff'.format(self.name)
#        def __repr__(self):
#                return '<Employee: name={0}, salary={1}>'.format(self.name, self.salary)
#
#class Chef(Employee):
#        def __init__(self, name):
#                Employee.__init__(self, name, 50000)
#        def work(self):
#                print '{0} makes food'.format(self.name)
#
#class Server(Employee):
#        def __init__(self, name):
#                Employee.__init__(self, name, 40000)
#        def work(self):
#                print '{0} interfaces with customer'.format(self.name)
#
#class PizzaRobot(Chef):
#        def __init__(self, name):
#                Chef.__init__(self, name)
#        def work(self):
#                print '{0} makes pizza'.format(self.name)
#
#class Customer:                                                                 # Expanding here by adding a customer class
#        def __init__(self, name):
#                self.name = name
#        def order(self, server):
#                print '{0} order from {1}'.format(self.name, server)
#        def pay(self, server):
#                print '{0} pays for item to {1}'.format(self.name, server)
#
#class Oven:
#        def bake(self):
#                print('oven bakes')
#
#class PizzaShop:
#        def __init__(self):
#                self.server = Server('Pat')
#                self.chef = PizzaRobot('Bob')
#                self.oven = Oven()
#
#        def order(self, name):
#                customer = Customer(name)
#                customer.order(self.server)
#                self.chef.work()
#                self.oven.bake()
#                customer.pay(self.server)
#
#
##if __name__ == '__main__':
##        scene = PizzaShop()
##        scene.order('Homer')
##        print('...')
##        scene.order('Shaggy')
#
#import pickle
#file = open('filenameP', 'wb')
#objectShop = PizzaShop()
#print '{0}, {1}'.format(objectShop.server, objectShop.chef)
#pickle.dump(objectShop, file)
#
#
#import pickle
#file = open('filenameP', 'rb')
#obj = pickle.load(file)
#print '{0}, {1}'.format(obj.server, obj.chef)
#obj.order('Sue')

#class Person:
#        def __init__(self, name, job=None, pay=0):
#                self.name = name
#                self.job = job
#                self.pay = pay
#        def lastName(self):
#                return self.name.split()[-1]
#        def giveRaise(self, percent):
#                self.pay = int(self.pay * (1 + percent))
#        def __str__(self):
#                return '[Person: {0}, {1}]'.format(self.name, self.pay)
#
#class Manager:
#        def __init__(self, name, pay):
#                self.person = Person(name, 'mgr', pay)                          # Embed a Person object                        
#        def giveRaise(self, percent, bonus=0.10):                               
#                return self.person.giveRaise(percent + bonus)                   # Intercept and Raise
#        def __getattr__(self, attr):
#                return getattr(self.person, attr)                               # Delegate all other attrs
#        def __str__(self):
#                return str(self.person)                                         # Must overload in 3.0
#
#if __name__ == '__main__':
#        bob = Person('Bob Smith')
#        sue = Person('Sue Jones', job='dev', pay=100000)
#        print(bob)
#        print(sue)
#        print('{0} {1}'.format(bob.lastName(), sue.lastName()))
#        sue.giveRaise(.10)
#        print(sue)
#        tom = Manager('Tom Jones', 50000)
#        tom.giveRaise(.10)
#        print(tom.lastName())
#        print(tom)
#class Super:
#        def __init__(self):
#                self.data1 = 'spam'
#        def ham(self):
#                pass
#            
#class ListTree:
#        """
#        Mix-in that returns an __str__ trace of the entire class tree an all its objects' attrs at and above self;
#        run by print(), str() returns constructed string; uses __X attr names to avoid impacting clients; uses
#        generator expr to recurse to superclasses; uses str.format() to make substitutions clearer
#        """
#
#        def __str__(self):                              # print() overloading
#                self.__visited = {}
#                return '<Instance of {0}, address {1}:\n{2}{3}>'.format(self.__class__.__name__,
#                                                                        id(self),
#                                                                        self.__attrnames(self, 0),
#                                                                        self.__listclass(self.__class__, 4))
#
#        def __listclass(self, aClass, indent):          # 
#                dots = '.' * indent
#                if aClass in self.__visited:
#                        return '\n{0}<Class {1}:, address {2}: (see above)>\n'.format(dots,
#                                                                                      aClass.__name__,
#                                                                                      id(aClass))
#                else:
#                        self.__visited[aClass] = True
#                        genabove = (self.__listclass(c, indent + 4) for c in aClass.__bases__)
#                        return '\n{0}<Class {1}, address {2}:\n{3}{4}{5}>\n'.format(dots,
#                                                                                    aClass.__name__,
#                                                                                    id(aClass),
#                                                                                    self.__attrnames(aClass, indent),
#                                                                                    ''.join(genabove),
#                                                                                    dots)
#
#        def __attrnames(self, obj, indent):
#                spaces = ' ' * (indent + 4)
#                result = ''
#                for attr in sorted(obj.__dict__):
#                        if attr.startswith('__') and attr.endswith('__'):
#                                result += spaces + '{0} = <>\n'.format(attr)
#                        else:
#                                result += spaces + '{0}={1}\n'.format(attr, getattr(obj, attr))
#                return result
#            
#class Sub(Super, ListTree): pass
#I = Sub()
#print(I)

#class Set:
#        def __init__(self, value = []):
#                self.data = []
#                self.concat(value)
#
#        def intersect(self, other):
#                res = []
#                for x in self.data:
#                        if x in other:
#                                res.append(x)
#                return Set(res)
#
#        def union(self, other):
#                res = self.data[:]
#                for x in other:
#                        if not x in res:
#                                res.append(x)
#                return Set(res)
#
#        def concat(self, value):
#                for x in value:
#                        if not x in self.data:
#                                self.data.append(x)
#        def __len__(self):
#                return len(self.data)
#
#        def __getitem__(self, key):
#                return self.data[key]
#
#        def __and__(self, other):
#                return self.intersect(other)
#
#        def __or__(self, other):
#                return self.union(other)
#
#        def __repr__(self):
#                return 'Set: ' + repr(self.data)
#
#if __name__ == '__main__':
#        x = Set([1, 3, 5, 7])
#        print(x.union(Set([1, 4, 7])))
#        print(x | Set([1, 4, 6]))

#class MyList(list):
#        def __getitem__(self, offset):
#                print '(indexing {0} at {1})'.format(self, offset)
#                return list.__getitem__(self, offset - 1)
#
#if __name__ == '__main__':
#        print(list('abc'))
#        x = MyList('ABC')
#        print(x)
#
#        print(x[1])
#        print(x[3])
#
#        x.append('spam'); print(x)
#        x.reverse();      print(x)

#class Set(list):
#        def __init__(self, value = []):
#                #list.__init__([])
#                self.concat(value)
#
#        def intersect(self, other):
#                res = []
#                for x in self:
#                        if x in other:
#                                res.append(x)
#                return Set(res)
#
#        def union(self, other):
#                res = Set(self)
#                res.concat(other)
#                return res
#
#        def concat(self, value):
#                for x in value:
#                        if not x in self:
#                                self.append(x)
#
#        def __and__(self, other):
#                return self.intersect(other)
#
#        def __or__(self, other):
#                return self.union(other)
#
#        def __repr__(self):
#                return 'Set: ' + list.__repr__(self)
#        
#if __name__ == '__main__':
#        x = Set([1, 3, 5, 7])
#        y = Set([2, 1, 4, 5, 6])
#        print(x, y, len(x))
#        print(x.intersect(y), y.union(x))
#        print(x & y, x | y)
#        x.reverse(); print(x)
#class Employee:
#    def __init__(self, name, salary=0):
#        self.name = name
#        self.salary = salary
#    def giveRaise(self, percent):
#        self.salary = int(self.salary * (1 + percent))
#    def work(self):
#        print '{0} does stuff'.format(self.name)
#    def __repr__(self):
#        return '<Employee: name={0}, salary={1}>'.format(self.name, self.salary)
#    
#class Chef(Employee):
#    def __init__(self, name):
#        Employee.__init__(self, name, 50000)
#    def work(self):
#        print '{0} makes food'.format(self.name)
#
#class Server(Employee):
#    def __init__(self, name):
#        Employee.__init__(self, name, 40000)
#    def work(self):
#        print '{0} interfaces with customer'.format(self.name)
#
#class PizzaRobot(Chef):
#    def __init__(self, name):
#        Chef.__init__(self, name)
#    def work(self):
#        print '{0} makes pizza'.format(self.name)
#        
#class Customer:
#    def __init__(self, name):
#        self.name = name
#    def order(self, server):
#        print '{0} order from {1}'.format(self.name, server)
#    def pay(self, server):
#        print '{0} pays for item to {1}'.format(self.name, server)
#        
#class Oven:
#    def bake(self):
#        print 'Oven Bakes'
#        
#class PizzaShop:
#    def __init__(self):
#        self.server = Server('Pat')
#        self.chef = PizzaRobot('Bob')
#        self.oven = Oven()
#    def order(self, name):
#        customer = Customer(name)
#        customer.order(self.server)
#        #print 'p {0}'.format(self.server)
#        self.chef.work()
#        self.oven.bake()
#        customer.pay(self.server)
#        
#scene = PizzaShop()
#scene.order('Homer')
#print('...')
#scene.order('Shaggy')

#def kaboom(x, y):
#    print x + y
#    
#try:
#    kaboom([0, 2, 1], [3, 4, 5])
#finally:
#    print 'Hello world'
#print 'Resuming here'
#class MyError(Exception): pass
#
#def stuff(file):
#        raise MyError()
#file = open('data', 'w')
#
#try:
#        stuff(file)
#except MyError:
#    print 'File Error'
#finally:
#        file.close()
#        print 'File closed'
#print 'After try'

#sep = '-' * 32 + '\n'
#print(sep + 'EXCEPTION RAISED AND CAUGHT')
#
#try:
#        x = 'spam'[99]
#except IndexError:
#        print 'except run'
#finally:
#        print 'finally run'
#print 'after try' 
#sep = '-' * 32 + '\n'
#
#print(sep + 'EXCEPTION RAISED AND CAUGHT')
#try:
#        x = 'spam'[99]
#except IndexError:
#        print 'except run'
#finally:
#        print 'finally run'
#print 'after try'
#
#print(sep + 'NO EXCEPTION RAISED')
#try:
#        x = 'spam'[3]
#except IndexError:
#        print 'except run'
#finally:
#        print 'finally run'
#print 'after try'
#
#print(sep + 'NO EXCEPTION RAISED, WITH ELSE')
#try:
#        x = 'spam'[3]
#except IndexError:
#        print 'except run'
#else:
#        print 'else run'
#finally:
#        print 'finally run'
#print 'after try'        
#        
#print(sep + 'EXCEPTION RAISED, BUT NOT CAUGHT')
#try:
#        x = 1 / 0
#except IndexError:
#        print 'except run'
#finally:
#        print 'finally run'
#print 'after try'   
#try:
#        raise IndexError('spam')        # Exceptions remembers arguments
#except IndexError:
#        print 'propagating'
#        #raise 

#def f(x):
#        assert x < 0, 'x is negative'   # if assert condition is true, then exception is raised with the data statement.
#        return x ** 2
#    
#f(1)

#class TraceBlock:
#        def message(self, arg):
#                print 'running', arg
#        def __enter__(self):
#                print 'starting with block'
#                return self
#        def __exit__(self, exc_type, exc_value, exc_tb):
#                if exc_type is None:
#                        print 'exiting Normally\n'
#                else:
#                        print 'exception raised !', exc_type
#                        return False
#
#with TraceBlock() as action:
#        action.message('test 1')
#        print 'reached'
#
#with TraceBlock() as action:
#        action.message('test 2')
#        raise TypeError
#        print 'not reached'

#class General(Exception): pass
#class Specific1(General): pass
#class Specific2(General): pass
#
#def raiser0():
#        X = General()                   # raise superclass instance
#        raise X
#
#def raiser1():
#        X = Specific1()                 # raise subclass instance
#        raise X
#
#def raiser2():
#        X = Specific2()                 # raise subclas instance
#        raise X
#
#for func in (raiser0, raiser1, raiser2):
#        try:
#                func()
#        except General:                 # match general or any subclass of it
#                import sys
#                print 'caught: ' + str(sys.exc_info()[0])

#class General(Exception): pass
#class Specific1(General): pass
#class Specific2(General): pass
#
#def raiser0(): raise General()
#def raiser1(): raise Specific1()
#def raiser2(): raise Specific2()
#
#for func in (raiser0, raiser1, raiser2):
#    try:
#        func()
#    except General as X:
#        print 'caught: ' + str(X.__class__)

#class Exp(Exception): pass
#
#try:
#        raise Exp('spam', 'eggs', 'ham')
#except Exp as X:                        
#    print 'Exp exception'
#    print X, X.args                     
#print 'Out'
#class MyBad(Exception):
#        def __str__(self):
#                return 'Always look on the bright side!'
#
#try:
#        raise MyBad
#
#except MyBad as X:
#        print X

#class FormatError(Exception):
#        def __init__(self, line, file):
#                self.line = line
#                self.file = file
#
#def raiser():
#        raise FormatError(42, file = 'myfile.txt')              # keyword argument as well
#
#try:
#        raiser()
#except FormatError as X:
#        print 'Error at, %s %s' % (X.file, X.line)
#class FormatError(Exception): pass
#
#def raiser():
#        raise FormatError(42, 'myfile.txt')
#try:
#        raiser()
#except FormatError as X:
#        print 'Error at, %s %s' % (X.args[0], X.args[1])

#def action2():
#        print(1 + [])
#
#try:
#        try:
#                action2()
#        except TypeError:
#                print 'Inner try'
#except TypeError:
#        print 'Outer try'
#try:
#        try:
#                raise IndexError
#        finally:
#                print 'spam'
#finally:
#        print 'SPAM'
#def raise1(): raise IndexError
#def noraise(): return
#def raise2(): raise SyntaxError
#
#for func in (raise1, noraise, raise2):
#        print '\n {0}'.format(func)
#        try:
#                try:
#                        func()
#                except IndexError:
#                        print 'caught IndexError'
#        finally:
#                print 'finally run'
#while True:
#    try:
#        data = raw_input()
#    except EOFError:
#        break
#print data
#import sys
#
#def bye():
#        sys.exit(40)                    # Crucial Error! Abort Now
#
#try:
#        bye()
#except SystemExit:
#        print 'Got it!'
#print 'Continuing!'
#class TraceBlock:
#    def message(self, arg):
#        self.arg = arg
#        print 'running', arg
#    def __enter__(self):
#        print 'in context'
#        return self
#    def __exit__(self, exc_name, exc_value, exc_tb):
#        if exc_name is None:
#            print 'exiting normally'
#            return
#        else:
#            print 'exception raised', exc_name
#            return False
#with TraceBlock() as exc:
#    exc.message('test1')
#    print 'block reached'
#    
#with TraceBlock() as exc:
#    exc.message('test2')
#    print 'block reached'
#    raise TypeError
#mailBody = ''
#signature = 'Later!'
#print 'Compose your mail:'
#while True:
#    try:
#        # Hit ^D after entering some text
#        mailBody+= raw_input()
#        mailBody+='\n'
#    except EOFError:
#        break
#
## This raw_input() throws EOFError too. Because, stdin is terminated for the session
## when EOF (^D) is issues at first raw_input() method (Where as, it doesn't raise EOFError in Linux)
#opt = raw_input("Do you want to add signature to your mail? (y/N): ")
#opt = opt.lower()
#print '-'*10+'Your Mail'
#if opt == 'y':
#    print mailBody+"\n"+signature
#else:
#    print mailBody
#print '-'*19
#while True:
#        try:
#                line = raw_input()          # Read line from stdin
#        except EOFError:
#                break                   # Exit loop at end-of-file
#        else:
#            print line

#def nestEggFixed(salary, save, growthRate, years):
#    """
#    - salary: the amount of money you make each year.
#    - save: the percent of your salary to save in the investment account each
#      year (an integer between 0 and 100).
#    - growthRate: the annual percent increase in your investment account (an
#      integer between 0 and 100).
#    - years: the number of years to work.
#    - return: a list whose values are the size of your retirement account at
#      the end of each year.
#    """
#    res = []
#    for year in range(years):
#        if year == 0:
#            t_fund = salary * save * 0.01
#            res.append(t_fund)
#        if year > 0:
#            t_fund = res[year-1] * (1 + 0.01 * growthRate) + salary * save * 0.01
#            res.append(t_fund)
#    return res
#        
#def testNestEggFixed():
#    salary     = 10000
#    save       = 10
#    growthRate = 15
#    years      = 5
#    savingsRecord = nestEggFixed(salary, save, growthRate, years)
#    print savingsRecord
#
#testNestEggFixed()
#def nestEggVariable(salary, save, growthRates):
#    """
#    - salary: the amount of money you make each year.
#    - save: the percent of your salary to save in the investment account each
#      year (an integer between 0 and 100).
#    - growthRate: a list of the annual percent increases in your investment
#      account (integers between 0 and 100).
#    - return: a list of your retirement account value at the end of each year.
#    """
#    res = [0]
#    res[0] = salary * save * 0.01
#    for i in range(1,len(growthRates)):
#        t_fund = res[i-1] * (1 + 0.01 * growthRates[i]) + salary * save * 0.01
#        res.append(t_fund)
#    return res
#    
#def testNestEggVariable():
#    salary      = 10000
#    save        = 10
#    growthRates = [3, 4, 5, 0, 3]
#    savingsRecord = nestEggVariable(salary, save, growthRates)
#    print savingsRecord
#testNestEggVariable()
#def postRetirement(savings, growthRates, expenses):
#    """
#    - savings: the initial amount of money in your savings account.
#    - growthRate: a list of the annual percent increases in your investment
#      account (an integer between 0 and 100).
#    - expenses: the amount of money you plan to spend each year during
#      retirement.
#    - return: a list of your retirement account value at the end of each year.
#    """
#    res = [0]
#    res[0] = (savings * (1 + 0.01 * growthRates[0])) - expenses
#    for i in range(1,len(growthRates)):
#        t_fund = (res[i-1] * (1 + 0.01 * growthRates[i])) - expenses
#        res.append(t_fund)
#    return res
#    
#def testPostRetirement():
#    savings     = 100000
#    growthRates = [10, 5, 0, 5, 1]
#    expenses    = 30000
#    savingsRecord = postRetirement(savings, growthRates, expenses)
#    print savingsRecord
#testPostRetirement()
#    # Output should have values close to:
#    # [80000.000000000015, 54000.000000000015, 24000.000000000015,
#    # -4799.9999999999854, -34847.999999999985]
#def postRetirement(savings, growthRates, expenses):
#    """
#    - savings: the initial amount of money in your savings account.
#    - growthRate: a list of the annual percent increases in your investment
#      account (an integer between 0 and 100).
#    - expenses: the amount of money you plan to spend each year during
#      retirement.
#    - return: a list of your retirement account value at the end of each year.
#    """
#    res = [0]
#    res[0] = (savings * (1 + 0.01 * growthRates[0])) - expenses
#    for i in range(1, len(growthRates)):
#        t_fund = (res[i-1] * (1 + 0.01 * growthRates[i])) - expenses
#        res.append(t_fund)
#    return res
#    
#def testPostRetirement():
#    savings     = 5266.26
#    growthRates = [10, 5, 0, 5, 1]
#    expenses    = 1229.95548986
#    savingsRecord = postRetirement(savings, growthRates, expenses)
#    print savingsRecord
#testPostRetirement()
#def get_frequency_dict(sequence):
#    """
#    Returns a dictionary where the keys are elements of the sequence
#    and the values are integer counts, for the number of times that
#    an element is repeated in the sequence.
#
#    sequence: string or list
#    return: dictionary
#    """
#    # freqs: dictionary (element_type -> int)
#    freq = {}
#    for x in sequence:
#        freq[x] = freq.get(x,0) + 1
#    print freq
#    return freq
#get_frequency_dict('sequence')
# Problem Set 5: 6.00 Word Game
# Name: 
# Collaborators: 
# Time: 
#

#import random
#import string
#
#VOWELS = 'aeiou'
#CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
#HAND_SIZE = 7
#
#SCRABBLE_LETTER_VALUES = {
#    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 
#    'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 
#    'y': 4, 'z': 10
#}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

#WORDLIST_FILENAME = "words.txt"
#
#def load_words():
#    """
#    Returns a list of valid words. Words are strings of lowercase letters.
#    
#    Depending on the size of the word list, this function may
#    take a while to finish.
#    """
#    print "Loading word list from file..."
#    # inFile: file
#    inFile = open(WORDLIST_FILENAME, 'r', 0)
#    # wordlist: list of strings
#    wordlist = []
#    for line in inFile:
#        wordlist.append(line.strip().lower())
#    print "  ", len(wordlist), "words loaded."
#    return wordlist
#
#def get_frequency_dict(sequence):
#    """
#    Returns a dictionary where the keys are elements of the sequence
#    and the values are integer counts, for the number of times that
#    an element is repeated in the sequence.
#
#    sequence: string or list
#    return: dictionary
#    """
#    # freqs: dictionary (element_type -> int)
#    freq = {}
#    for x in sequence:
#        freq[x] = freq.get(x,0) + 1     # if an item in said iteration already exists in freq, add 1
#    return freq


# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
#def get_word_score(word, n):
#    """
#    Returns the score for a word. Assumes the word is a
#    valid word.
#
#    The score for a word is the sum of the points for letters
#    in the word, plus 50 points if all n letters are used on
#    the first go.
#
#    Letters are scored as in Scrabble; A is worth 1, B is
#    worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.
#
#    word: string (lowercase letters)
#    returns: int >= 0
#    """
#    score = 0
#    
#    if len(word) == 0:
#        return score
#    assert n > 0, 'No letters at hand.'
#    
#    for item in word:
#        score += SCRABBLE_LETTER_VALUES.get(item, 0)
#    
#    if len(word) == n:
#        score += 50
#    
#    return score
##
## Make sure you understand how this function works and what it does!
##
#def display_hand(hand):
#    """
#    Displays the letters currently in the hand.
#
#    For example:
#       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
#    Should print out something like:
#       a x x l l l e
#    The order of the letters is unimportant.
#
#    hand: dictionary (string -> int)
#    """
#    tmp = []
#    for letter in hand.keys():
#        for j in range(hand[letter]):
#            tmp.append(letter)          # print all on the same line
#    return ' '.join(tmp)                 # print an empty line
#
##
## Make sure you understand how this function works and what it does!
##
#def deal_hand(n):
#    """
#    Returns a random hand containing n lowercase letters.
#    At least n/3 the letters in the hand should be VOWELS.
#
#    Hands are represented as dictionaries. The keys are
#    letters and the values are the number of times the
#    particular letter is repeated in that hand.
#
#    n: int >= 0
#    returns: dictionary (string -> int)
#    """
#    hand={}
#    num_vowels = n / 3
#    
#    for i in range(num_vowels):
#        x = VOWELS[random.randrange(0,len(VOWELS))]
#        hand[x] = hand.get(x, 0) + 1
#        
#    for i in range(num_vowels, n):    
#        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
#        hand[x] = hand.get(x, 0) + 1
#        
#    return hand
#
##
## Problem #2: Update a hand by removing letters
##
#def update_hand(hand, word):
#    """
#    Assumes that 'hand' has all the letters in word.
#    In other words, this assumes that however many times
#    a letter appears in 'word', 'hand' has at least as
#    many of that letter in it. 
#
#    Updates the hand: uses up the letters in the given word
#    and returns the new hand, without those letters in it.
#
#    Has no side effects: does not mutate hand.
#
#    word: string
#    hand: dictionary (string -> int)    
#    returns: dictionary (string -> int)
#    """
#    newHand = hand.copy()
#    assert len(word) > 0, 'Enter a valid word'
#    
#    check = 0
#    for item_c in word:
#        check = hand.get(item_c, 0)
#        assert check > 0, str(item_c) + ' letter in your word does not exist at your hand. Use a new word.'
#    
#    for item in word:
#        if newHand.get(item, 0) > 1:
#            newHand[item] -= 1
#        else:
#            newHand.pop(item)
#    return newHand
#       
##
## Problem #3: Test word validity
##
#def is_valid_word(word, hand, word_list):
#    """
#    Returns True if word is in the word_list and is entirely
#    composed of letters in the hand. Otherwise, returns False.
#    Does not mutate hand or word_list.
#    
#    word: string
#    hand: dictionary (string -> int)
#    word_list: list of lowercase strings
#    """
#    val = False
#    
#    c1 = 0 
#    c2 = 0
#    
#    for item in word_list:
#        if word.lower() == item:
#            c1 = 1
#    
#    check_d = hand.copy()
#         
#    for item in word:
#        check = check_d.get(item, 0)
#        if check == 0:
#            break
#        if check_d.get(item, 0) > 1:
#            check_d[item] -= 1
#        else:
#            check_d.pop(item)
#    else:
#        c2 = 1
#        
#    if c1 == 1:
#        if c2 == 1:
#            val = True
#        
#    return val
##
## Problem #4: Playing a hand
##
#def play_hand(hand, word_list):
#    """
#    Allows the user to play the given hand, as follows:
#
#    * The hand is displayed.
#    
#    * The user may input a word.
#
#    * An invalid word is rejected, and a message is displayed asking
#      the user to choose another word.
#
#    * When a valid word is entered, it uses up letters from the hand.
#
#    * After every valid word: the score for that word and the total
#      score so far are displayed, the remaining letters in the hand 
#      are displayed, and the user is asked to input another word.
#
#    * The sum of the word scores is displayed when the hand finishes.
#
#    * The hand finishes when there are no more unused letters.
#      The user can also finish playing the hand by inputing a single
#      period (the string '.') instead of a word.
#
#    * The final score is displayed.
#
#      hand: dictionary (string -> int)
#      word_list: list of lowercase strings
#    """
#    t_score = 0
#    print 'Current Hand:', display_hand(hand)
#    inp = raw_input("Enter word, or a (.) to indicate that you're finished: ")
#    
#    def hand_size(hand):
#        size = 0
#        value_list = hand.values()
#        for i in range(len(value_list)):
#            size += value_list[i]
#        return size
#    
#    while(inp != '.'):
#        print 'continue'
#        if is_valid_word(inp, hand, word_list):
#            print 'hand_size(hand)',hand_size(hand), 't_score', t_score
#            t_score += get_word_score(inp, hand_size(hand))
#            print 't_score', t_score, 'inp', inp, 'get_word_score(inp, hand_size(hand))', get_word_score(inp, hand_size(hand)), 'hand_size(hand)', hand_size(hand)
#            print inp, 'has earned', get_word_score(inp, hand_size(hand)),'points. Total:', t_score, 'points'
#            hand = update_hand(hand, inp)
#            if hand_size(hand) <= 0:
#                print 'Hand empty.'
#                break
#            print 'Current Hand:', display_hand(hand)
#            inp = raw_input("Enter word, or a (.) to indicate that you're finished: ")
#        else:
#            print 'Invalid word, please try again.'
#            print 'Current Hand:', display_hand(hand)
#            inp = raw_input("Enter word, or a (.) to indicate that you're finished: ")
#            #continue
#    print 'Total score:', t_score, 'points.'
#play_hand({'a':1, 's':1, 't':2, 'w':1, 'f':1, 'o':1}, load_words())
##play_hand({'a':1, 'c':1, 'i':1, 'h':1, 'm':2, 'z':1}, load_words())
#import string, pprint
#
#SCRABBLE_LETTER_VALUES = {
#    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
#}
#
#WORDLIST_FILENAME = "words2.txt"
#
#def load_words():
#    """
#    Returns a list of valid words. Words are strings of lowercase letters.
#    
#    Depending on the size of the word list, this function may
#    take a while to finish.
#    """
#    print "Loading word list from file..."
#    # inFile: file
#    inFile = open(WORDLIST_FILENAME, 'r', 0)
#    # wordlist: list of strings
#    wordlist = []
#    for line in inFile:
#        wordlist.append(line.strip().lower())
#    print "  ", len(wordlist), "words loaded."
#    return wordlist
#
#def get_words_to_points(word_list):
#    """ 
#    Return a dict that maps every word in word_list to its point value.
#    """
#    w_points = {}
#    for word in word_list:
#        tmp_val = 0
#        for letter in word:
#            tmp_val += SCRABBLE_LETTER_VALUES.get(letter, 0)
#        w_points[word] = tmp_val
#    return w_points
#c = get_words_to_points(load_words())
#print c
SUBJECT_FILENAME = "subjects.txt"
def loadSubjects(filename):
    """
    Returns a dictionary mapping subject name to (value, work), where the name
    is a string and the value and work are integers. The subject information is
    read from the file named by the string filename. Each line of the file
    contains a string of the form "name,value,work".

    returns: dictionary mapping subject name to (value, work)
    """

    # The following sample code reads lines from the specified file and prints
    # each one.
    subInfo = {}
    inputFile = open(filename)
    for line in inputFile:
        name, value, hours = line.strip().split(',')
        subInfo[name] = (value, hours) 
    return subInfo
         
c = loadSubjects(SUBJECT_FILENAME)
print c

        