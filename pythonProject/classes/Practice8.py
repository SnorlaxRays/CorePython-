#Define class and instance attributes

class Cylinder:
    #class variable
    pi = 3.14
    def __init__(self,radius,height):
        self.radius = radius
        self.height = height

#Area = pi * radius * radius * height
#volume = 2 * pi * radius *(height + radius)

    def area(self):
        return Cylinder.pi * self.radius * self.radius * self.height    #class.classVariable = if we want to use class variable

    def volume(self):
        return 2 * Cylinder.pi * self.radius *(self.height + self.radius)

    def getRadius(self):
        return self.radius

    def getHeight(self):
        return self.height