import superclass1
from superclass1 import *

class Circle(Shape):
    pi = 3.14

    def __init__(self):
        self.radius = 0

    def area(self):
        return Circle.pi * self.radius * self.radius

    def setRadius(self,radius):
        self.radius = radius

    def getRadius(self):
        return self.radius
