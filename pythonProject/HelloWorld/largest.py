list = []
n = int(input("Enter number of elements: "))

for i in range(0,n):
    ele = int(input('write something'))
    list.append(ele)

print(list)
'''
list.sort()
print(list)

for i in list:
    if i == list[len(list)-1]:
        print("largest number:",i)
'''

print(max(list))