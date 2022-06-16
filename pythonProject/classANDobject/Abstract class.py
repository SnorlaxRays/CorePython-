from abc import ABC,abstractmethod

class Polygon(ABC): #Polygon is an abstract class

    def __init__(self):
        pass

    @abstractmethod
    def noofsides(self):
        pass

class Triangle(Polygon):

  def noofsides(self):
        print("I have 3 sides")


class Pentagon(Polygon):

    def noofsides(self):
        print("I have 5 sides")

t = Triangle()
t.noofsides()

p = Pentagon()
p.noofsides()