#parametrized function as thread
import threading


def hello(a):
    for i in range(15):
        print('Hello',i,a)

def hi(b):
    for i in range(15):
        print('Hi',i,b)


t1 = threading.Thread(target=hello, args =('Ram',))
t2 = threading.Thread(target = hi, args =('Shyam',))

t1.start()
t2.start()