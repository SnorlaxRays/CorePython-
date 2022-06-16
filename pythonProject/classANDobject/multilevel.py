class Student:

    def getData(self):
        self.name = input("Enter your name:")
        self.age = int(input("Enter your age:"))
        self._class = input("Class")
        self.gender = input("Gender:")

class Test(Student):

    def getMarks(self):
        print("Enter the marks of respective subjects:")
        self.biology = int(input("anything"))
        self.maths = int(input("anything"))
        self.english = int(input("anything"))

class result(Test):

    def display(self):
        print("Total:",self.biology+self.maths+self.english)

    def Data(self):
        print(self.name)


d = result()
print(d.getData())
print(d.getMarks())
print(d.display())
print(d.Data)
print(d.Data())