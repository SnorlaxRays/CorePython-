class Person:  # class
    count = 0

    def __init__(self):# Constructor
        self.name = " "
        Person.count = Person.count + 1


    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

