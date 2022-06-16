'''
num = int(input("enter any digit"))

count = 0
for i in range(1,num):
    if num % i == 0:
        count = count + 1


if count == 1:
    print("prime")
else:
    print("not prime")

'''

for num in range(2,100):
    for i in range(2,num):
        if num % i == 0:
            break
    else:
        print(num)
