import time
import threading
from threading import *

class Account:

    balance = 0

    def __init__(self):
        self.lock = threading.Lock()

    def get_balance(self):
        time.sleep(0.00000000000000000001)
        return self.balance

    def set_balance(self, amount):
        time.sleep(0.000000000000000000001)
        self.balance = amount

    def deposit(self,amount):
        self.lock.acquire()
        bal = self.get_balance()
        self.set_balance(bal + amount)
        self.lock.release()


