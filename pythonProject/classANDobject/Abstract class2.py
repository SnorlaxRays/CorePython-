from abc import ABC, abstractmethod

class Shape(ABC):

    '''You are in abstract class''' #doc string
    def __init__(self,color,borderwidth):
        self.color = color
        self.__borderWidth = borderwidth

    def setColor(self,color):
        self.color = color

    def setBorderWidth(self,borderwidth):
        self.__borderWidth = borderwidth

    def getColor(self):
        return self.color

    def getBorderWidth(self):
        return self.__borderWidth

    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):

    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):

    pi = 3.14 # this is a class variable
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return Circle.pi * self.radius * self.radius

class Triangle(Shape):

    def __init__(self,base,height,color="",borderwidth = 0):
        self.base = base
        self.height = height
        super(Triangle,self).__init__(color,borderwidth) #we can't access private attributes outside parant class

    def area(self):
        return 0.5 * self.base * self.height

    def __str__(self):       ##Method __str__ #this is also an override method
        return "Base = %s ,Height = %s" % (self.base, self.height)

'''
s = Shape()  # cant instantiate abstract class Shape with abstract method area
s.setColor("Red")
print(s.getColor())
'''

r = Rectangle(5,6)
print(r.area())

c = Circle(5)
c.setColor("Red") #color is a public attribute so we can set this attribute
c.setBorderWidth(35) # its useless coz attribute is private
print(c.area())
print(c.color) #now we can fetch or access this attribute coz this is public
##print(c.borderwidth) this is wrong coz this is a private attribute

t = Triangle(5,6,"Blue",35) #coz of super method we can define shape's attributes in this class
print(t.area())
print(t.getColor())
print(t) #string representation of an object

#Metadata
print("Shape.__doc__:", Shape.__doc__)
print("Shape.__module__:", Shape.__module__)
print("Shape.__dict__:",Shape.__dict__)
print(t.__dict__)
print(t.__doc__)

