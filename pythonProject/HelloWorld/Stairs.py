'''
def func(n):
    if n<=1:
        return n
    return func(n-1) + func(n-2)

def countWays(s):
    return func(s+1)

s= 3
print(countWays(s))
'''

list1 = []
n1 = int(input("Enter range: "))

for i in range(0,n1):
    x = int(input('write something'))
    list1.append(x)
print(list1)
target = int(input("Enter your target:"))
nums = []

for i in list1:
    for j in list1:
        a = i + j
        if a == target:
            print(target)

