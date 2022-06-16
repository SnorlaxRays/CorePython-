num = int(input("enter any digit"))

count = 0
list = []
for i in range(1,num):
    if num % i == 0:
        count = count + 1

n = int(input("Range"))
for num in range(1,n):
    if count == 1 :
       list.append(num)
    else:
       print("NP")


print(list)








