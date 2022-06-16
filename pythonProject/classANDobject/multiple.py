class Addition:

    def sum(self,a,b):
        return a+b

class Multiplication:
    def mult(self,a,b):
        return a*b

class Derived_class(Addition,Multiplication):

    def divide(self,a,b):
        return a/b

p = Derived_class()
    
print(p.sum(3,7))