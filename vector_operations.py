from math import sqrt
import operator as op
from itertools import imap


class Vector:
  # TODO: Finish the Vector class.
    def __init__(self, array=[]):
        self.__data = array
  
    def __len__(self):
        return len(self.__data)
    
    def __iter__(self):
        return iter(self.__data)
    
    def __getitem__(self, i):
        return self.__data[i]
    
    def check_length(f):  # @NoSelf
        def wrapper(self, other):
            if len(self) != len(other):
                raise ValueError()
            return f(self, other)
        return wrapper


    @check_length
    def add(self, other):
        res = Vector(map(op.add, self, other))
        return res
      
    @check_length
    def subtract(self, other):
        res = Vector(map(op.sub, self, other))
        return res
        
    @check_length  
    def dot(self, other):
        res = reduce(op.add, imap(op.mul, self, other))
        return res
        
    def norm(self):
        return sqrt(self.dot(self))
        
    def equals(self, other):
        if len(self) != len(other):
            return False
        return all(map(op.eq, self, other))
        
    def __str__(self):
        return '(%s)' % ','.join(str(x) for x in self.__data)
