n = int(input('range'))

num = 0
num1 = 1
print(num)
print(num1)
i = 2
for i in range(n):
    sum = num + num1
    num = num1
    num1 = sum
    print(sum)