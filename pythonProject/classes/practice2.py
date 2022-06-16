import Practice
from Practice import *


p = Person("Dexter",5) # Object
p1 = Person("John",6)  #Object1

print(p.name)
print(p.age) # private variable  #Encapsulation #__age or __name
print(p1.name)
print(p1.age)
print(p.sum(1,2))
print(Person.count)

