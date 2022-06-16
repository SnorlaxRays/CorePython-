
import pickle
class Employee:
    def __init__(self,eno,ename):
        self.eno = eno
        self.ename = ename

    def __str__(self): #this is not nessessary or optional
        return "eno = %s ename = %s" % (self.eno, self.ename)

e = Employee(1,'Sandeep')
f = open('emp.dat','wb')
pickle.dump(e,f)
print(f)
print(e)
f.close()


f = open('emp.dat','rb')
e = pickle.load(f)
print(f)
print(e) # same unnessessary or optional
f.close()
print(e.ename)


