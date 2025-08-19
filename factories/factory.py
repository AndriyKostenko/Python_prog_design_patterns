from math import sin, cos
from enum import Enum

class CoordinateSystem(Enum):
    CARTESIAN = 1
    POLAR = 2


# A factory method is a method that returns an instance of a class
# based on the input parameters. It is a way to create objects without
# specifying the exact class of object that will be created.
# The factory method pattern is a creational design pattern that provides
# an interface for creating objects in a superclass, but allows subclasses
# to alter the type of objects that will be created.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    @staticmethod
    def new_cartesian_point(x, y):
        return Point(x, y)
    
    @staticmethod
    def new_polar_point(rho, theta):
        return Point(rho * cos(theta), rho * sin(theta))
        
    def __repr__(self):
        return f"Point({self.x}, {self.y})"
    
    def __str__(self):
        return f"Point({self.x}, {self.y})"
    
p = Point(2, 3)
p2 = Point(1, 2)

for _ in range(5):
    x = Point()
    
p3 = p.new_polar_point(2,3)

print(p, p2)




"""
1. check 'else, yield, break, continue, return' in for/while
2. python patterns ~= 20pcs 


"""

x = 5
var = lambda *a, x = x : a[0] + x
   
def some_zamukanie():
    x = 5
    def some_wrapper(x):
        return x + 1
    
some_zamukanie()