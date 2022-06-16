'''
# Define a class that can add and subtract two numbers
#print(f'{x}-{y} = {a.subtract()}')
class add_sub:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    def subtract(self):
        return self.x - self.y

a = add_sub(10,20)
print(a.add())

print(a.subtract())
'''

class Car:

    def __init__(self,brand,model,color):
        self.__brand = brand
        self.__color = color
        self.__model = model

    def getBrand(self):
        return self.__brand

    def getColor(self):
        return self.__color

    def getModel(self):
        return self.__model

c = Car("Mahindra","SUV","black")
#print(c.__brand)  #private Attribute # Encapsulation

print(c.getBrand())
print(c.getColor())
print(c.getModel())









