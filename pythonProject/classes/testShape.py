import subclass1
from subclass1 import *

c = Circle()

c.setRadius(10)
print(c.area())
c.setColor("Blue")
print(c.getColor())

import subclass2
from subclass2 import *

t = Triangle()

t.setBase(12)
t.setHeight(24)
print(t.area())
t.setBorderWidth(10)
print(t.getborderWidth())