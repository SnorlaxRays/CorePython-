#Inherit thread class
import threading
from threading import *

class Hi(Thread):
    def run(self):
        for i in range(10):
            print("Hi",i)

t1 = Hi()
t1.start()
