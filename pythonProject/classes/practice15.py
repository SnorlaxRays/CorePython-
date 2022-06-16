
import practice12
from practice12 import *
p = Person()
p.setName("Dexter")
p.setDob("02-06-2022")
p.setAddress("Indore")
p.setAvgage(20)
print(p.getName(),"\t", p.getDob(),"\t", p.getAddress(), "\t", p.getAvgage())
print(p)
print(Person.__dict__)
print("p.__dict__:", p.__dict__)
print(Person.__bases__)
print(Person.__module__)
print(p)


'''
import practice13
from practice13 import *
a = Automobile()
a.setColor("Black")
a.setSpeed("100")
a.setMake("Tata")
a.setNoofgears("6")

print(a.getColor(),"\t", a.getSpeed(),"\t", a.getMake(), "\t", a.getNoofgears())
a.Break(90)
a.No_of_gears(7)
'''
'''
import practice14
from practice14 import *
c = Person("dexter","5")
print(c)
'''

