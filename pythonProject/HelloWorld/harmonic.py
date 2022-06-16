'''
n = int(input(" Enter range"))

sum = 0
for i in range(1,n):
    sum = sum + (1/i)

print(sum)

'''

list = []
n = int(input("Enter range: "))

for i in range(0,n):
    x = int(input('write something'))
    list.append(x)

list.sort(reverse = True)
print(list)

num = int(input("Write any number"))

if num not in list:
   print("-1")

print(list.__sizeof__())

