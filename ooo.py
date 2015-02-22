

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
    
p = Person("James Mayer")
c = Manager("John Adams", pay=100000)
print c 
c.giveRaise(percent=0.05)
print c 
print p 
