#Daemon Threads

import threading
import time
from threading import *


def first_thread():
    print("Hi are u deamon thread?")
    for i in range(10):
        time.sleep(2)
        print("yes i am a daemon thread",i)

def second_thread():
    print("are u non-daemon?")
    for i in range(10):
        time.sleep(2)
        print("Yes i am a non-daemon thread",i)

t2 = threading.Thread(target=first_thread, daemon=True)
t1 = threading.Thread(target=second_thread)

t1.start()
time.sleep(3)
t2.start()
