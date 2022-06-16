'''
str = "i am indian"

print(str.count('a'))
'''

'''
list = [1,2,3,4,5]
list1 = []

for i in range(0,5):
    list1.append(list[len(list)-i-1])
print(list1)

list3 = []
for i in range(len(list)):
    list3.append(list[i] + list1[i])
print(list3)
'''

'''
str = "i am indian"
count = 0

for i in str:
    if i == 'a':
       count = count+1

print(count)

'''
'''
list = []
n = int(input("Enter range: "))

for i in range(0,n):
    x = int(input('write something'))
    list.append(x)

print(list)

for a in list:
    n = list.count(a)
    if n > 1:
       list.remove(a)

print(list)
'''

##program to check if two strings are anagram

'''
list = []
n = int(input("Enter range: "))

for i in range(0,n):
    x = int(input('write something'))
    list.append(x)

print(list)
'''
'''
list = []
list1 = []
n = int(input("Enter range: "))

def firstLast():
    for i in range(0, n):
        x = int(input('write something'))
        list.append(x)


    list1.append(list[0])
    list1.append(list[n-1])
    print(list1)
firstLast()
'''

'''
import random

s = "qwertyuiopasdfghjklzxcvbnm0123456789QWERTYUIOPLKJHGFDSAZXCVBNM!@#$%^&*"

passlen = 8
p = " ".join(random.sample(s,passlen))
print(p)
'''
'''
import random
n = "0123456789"
len = 4
print("".join(random.sample(n,len)))
'''
import random
#random.seed(1)
#print(random.random())
print(random.random())
state = random.getstate()
print(random.random())
random.setstate(state)
print(random.random())






