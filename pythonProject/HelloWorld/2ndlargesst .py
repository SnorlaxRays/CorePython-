'''
list = [1,2,3,4,5,6]
list1 = []
list1 = list.copy()
list1.reverse()
print(list1)
'''
"list as a input"

list = []
n = int(input("Enter range: "))

for i in range(0,n):
    x = int(input('write something'))
    list.append(x)

print(list)

list.sort()
print(list)

for i in list:
    if i == list[len(list)-2]:
        print("Second largest number:",i)
