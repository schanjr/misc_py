##Code Snippet for playing around with Operators Overloading
class Person:
    def __init__(self, name, job=None, pay=0):
        self.name=name
        self.job=job
        self.pay=pay
        
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self,percent):
        self.pay = int(self.pay * (1 + percent))
    def __repr__(self):
        return '[Person: %s,%s,%s]' % (self.name, self.job, self.pay)
    
    
class Manager(Person):
    def __init__(self, name, pay):
        self.person=Person(name, 'mgr', pay)
    def giveRaise(self, percent, bonus=0.10):
        self.person.giveRaise(percent + bonus)
    def __getattr__(self,attr):
        return getattr(self.person, attr)
    def __repr__(self):
        return '[Manager: %s,%s,%s]' % (self.name, self.job, self.pay)
    
'''
bob = Person('Bob Smith')
sue = Person('Sue Jones', job='dev', 10000)    

print(bob)
print(sue)
print(bob.lastName(), sue.lastName()) 
sue.giveRaise(0.10)
print sue
tom=Manager('Tom Jones', 50000)
tom.giveRaise(0.10)
print(tom.lastName())
print(tom) 
'''
    
    
#Code snippet for playing around the different implementation with Super()

class Super(object):
    def method(self):
        print ('in Super.method')
    def delegate(self):
        self.action()

class Inheritor(Super):
    pass

class Replacer(Super):
    def method(self):
        print ('in Replacer.method')
        
class Extender(Super):
    def method(self):
        print ('starting Extender.method')
        Super.method(self)
        print('ending Extender.method')

class Provider(Super):
    def action(self):
        print ('in Provider.action')

'''
x=Provider()
print x.delegate()
'''

c=[i for i in range(10)]
d=[i for i in range(11)]
e=[i for i in range(10)]

func1 = lambda x: sum(x)
func2 = lambda x: sum(x)/len(x)
func3 = lambda x:  x



def cond_check(*conds):
    for func, base, expected in conds:
        print func(base),"=",expected,"?"
        yield func(base)==expected
        
'''for i in  cond_check((func1,c,d),(func2,c,d), (func3,c,d),(func3, c,e)):
    print i 
'''

class Shape(object):
    def __init__(self, shapename, **kwds):
        self.shapename = shapename
        #super(Shape, self).__init__(**kwds)

class ColoredShape(Shape):
    def __init__(self, color, **kwds):
        self.color = color
        super(ColoredShape,self).__init__(**kwds) #Calls back to the superclass Shape to do the __init__ constructor again. Since shapename key exists, maps to self.shapename

cs = ColoredShape(color='red', shapename='circle')

print cs.__dict__



        

