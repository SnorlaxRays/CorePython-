class Car:

    def __init__(self):
        self.color = " "
        self.brand = " "


    #Getter and Setter

    def setName(self,color,brand):
        self.color = color
        self.brand = brand

    def getColor(self):
        return self.color

    def getBrand(self):
        return self.brand