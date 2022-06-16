import superclass1
from superclass1 import *

class Triangle(Shape):

    def __init__(self):
        self.base = 0
        self.height = 0

    def area(self):
        return 0.5 * self.base * self.height

    def setBase(self,base):
        self.base = base

    def getBase(self):
        return getBase

    def setHeight(self,height):
        self.height = height

    def getHeight(self):
        return self.height


