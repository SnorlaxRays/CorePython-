import threading
from threading import *
import thrfive
from thrfive import *

class Racing(Thread):
    account: Account
    name = " "

    def __init__(self, account, name):
        super().__init__() # here racing,self is optional
        self.account = account
        self.name = name

    def run(self):
        for i in range(1, 6):
            self.account.deposit(100)
            print(self.name, self.account.get_balance())

acc = Account()

t1 = Racing(acc, "Ram")
t2 = Racing(acc, "Shyam")

t1.start()
t2.start()

