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
        

