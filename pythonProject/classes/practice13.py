class Automobile:

    def __init__(self):
        self.color = " "
        self.speed = 0
        self.make = " "
        self.no_of_gears = 6


    def setColor(self,color):
        self.color = color

    def setSpeed(self,speed):
        self.speed = speed

    def setMake(self,make):
        self.make = make

    #def setNoofgears(self,no_of_gears):
    #    self.no_of_gears = no_of_gears

    def getColor(self):
        return self.color

    def getSpeed(self):
        return self.speed

    def getMake(self):
        return self.make

    def getNoofgears(self):
        return self.no_of_gears

    def Break(self,speed):
        if speed >90:
            print("Break")
        else:
            print("Continue")

    def No_of_gears(self,no_of_gears):
        if no_of_gears > 6:
            print("Try bailgaadi")
        else:
            print("Welcome")








