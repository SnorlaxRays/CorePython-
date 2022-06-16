class Person:
    def __del__(self):
       className = self.__class__.__name__
       print(className)

    def __init__(self):
        self.name = ""
        self.dob = " "
        self.address = " "
        self.Avg_age = 0

    def setName(self,name):
        self.name = name

    def setDob(self,dob):
        self.dob = dob

    def setAddress(self,address):
        self.address = address

    def setAvgage(self,Avgage):
        self.Avg_age = Avgage

    def getName(self):
        return self.name

    def getDob(self):
        return self.dob

    def getAddress(self):
        return self.address

    def getAvgage(self):
        return self.Avg_age

    def __str__(self):
        return "Name = %s ,Address = %s ,Age = %s" % (self.name,self.address,self.Avg_age)