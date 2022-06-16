#WithoutThreading
import threading


def hello():
    for i in range(15):
        print('Hello',i)

def hi():
    for i in range(15):
        print('Hi',i)

#hello()
#hi()

#WithThread

t1 = threading.Thread(target=hello)
t2 = threading.Thread(target=hi)
#start threads

t1.start()
t2.start()