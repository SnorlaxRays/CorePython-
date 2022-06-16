num = input("enter any number")

l = list(num)
print(l)
n = len(l)

for i in range(0,n):
    if l[i] != l[n-i-1]:
        print('not a palindrome number')
        break
else:
    print("palindrome number")
