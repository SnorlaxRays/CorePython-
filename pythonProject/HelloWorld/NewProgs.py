'''
x = 10
while x:
    print(x)
    x = x-1

while True:
    name = input('Enter name:')
    if name == 'noface': break
    print(('hello',name))
'''
'''
x = 6
while x:
    print(x)
    
    x = x-1
    if x == 3:
        break

'''
'''
x = 6
while x:
    x = x-1
    if x % 2 != 0:
        continue
    print(x)
'''

evenOdd = (lambda x : 'odd' if x % 2 else 'even')
print(evenOdd(9))









