"For all Armstrong numbers"
'''
num = int(input("Enter any number:"))
sum = 0
for value in str(num):
    sum = sum + int(value) ** len(str(num))

if sum == num:
    print("Armstrong number")
else:
    print("Not an armstrong number")
'''


lower = int(input("range"))
upper = int(input("range"))
sum = 0
for num in range(lower,upper+1):
    for value in str(num):
       sum = sum + int(value) ** len(str(num))











