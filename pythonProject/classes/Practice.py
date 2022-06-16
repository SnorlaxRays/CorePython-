class Person: # class
    count = 0
    def __init__(self,name,age): #Constructor
        self.name = name # the self is used to represent the instance of a class
        self.age = age
        Person.count = Person.count+1

    def sum(self,a,b): #Function
        c = a+b
        return c

    def getName(self):
        return self.name
        return self.age