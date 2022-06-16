'''
name = input("Enter your name  ")
age = int(input("Enter your age "))
print("your name is :" + name)
print("your age is :" +str(age))
'''
'''
num = int(input("Enter any number"))
check = int(input("Enter any number"))

if (num % 2 == 0 and num % 4 != 0 ):
    print("even number")

elif (num % 4==0):
    print("its a multiple of 4")
else:
    print("odd number")

if check % num == 0:
    print("nice")
else :
    print("also nice")
'''
'''a = [1,1,2,3,5,8,13,21,34,55,89]'''
'''
for item in a :
    if item <= 5 :
        print(item)

L = []
for item in a :
    if item <= 5:
       L.append(item)
print(L)
'''
'''
num = int(input("Enter a number"))

if num in a:
    print(num)
else:
    print("Number doesnt exist in list")
'''
'''
num = int(input("enter a number"))
L = []
for num1 in range(1 ,num+1):
    if num % num1 == 0:
        print(num1)
        L.append(num1)
print(L)
'''

'''print("Hello World")'''
'''
num = input("enter any number")



'''
'''
a = [1,4,9,16,25,36,49,64,81,100]


l = [item for item in a if item % 2 == 0]

print(l)
'''

























