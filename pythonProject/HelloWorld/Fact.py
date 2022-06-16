n = int(input("Enter any number"))

mult = 1
for i in range(1,n):
    mult = mult * (n-i+1)
print(mult)
