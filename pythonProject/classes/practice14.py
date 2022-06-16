'''
import datetime

d = datetime.datetime.now()
print(d)

#print(d.__doc__)

import random
r = random.randint(1,100)
print(r)

#print(r.__doc__)
'''
'''
class Person:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return "Name = %s ,Age = %s" % (self.name,self.age)
'''
'''
#x = "global"

def f():
    global x
    x = "Enclosing"

    def g():
        y = "local"

    print(x)

    g()
f()
print(x)
'''

'''i = 1
while i <6:
    print(i)
    i = i+1 '''

