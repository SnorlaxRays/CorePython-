'''
n = int(input("Range:"))

list = []
list1 = []

for i in range(0,n,2):
    list.append(i)

for j in range(1,n,2):
    list1.append(j)

print(list)
print(list1)

sum = 0
for i in range(len(list)):
    sum = sum + list[i]

sum = sum/2
print(sum)

sum1 = 0
for j in range(len(list1)):
    sum1 = sum1 + list1[j]

sum1 = sum1/2
print(sum1)

for i in range(len(list)):
    print((list[i] + list1[i])/2)

'''

list = [1,2,3,4]
list1 = [1,2,3,4]

list3 = list1 + list
print(list3)
