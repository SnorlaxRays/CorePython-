list = []
n = int(input("Enter range: "))

for i in range(0,n):
    x = int(input('write something'))
    list.append(x)

list1 = []
n1 = int(input("Enter range: "))

for i in range(0,n1):
    x = int(input('write something'))
    list1.append(x)

for value in list:
    if value not in list1:
        print(value)