'''''
list1 = [1,2,3,4,5]

list1.extend([1,2])
print(list1)
list1.insert(3,'sandeep')
print(list1)
x = list(enumerate(list1))
print(x)
'''''
'''
list2 = [3,9,8,4,6]

print(sorted(list2))


print(len(list2))

X = 'sandeep'
print(list(X))
'''
dict1 = {'name': 'dexter','age':45, 'job': 'pilot'}

D = dict.fromkeys([1,2],'developer')
print(D)

''' Keys must be immutable type, must be unique'''
print(dict1.get('job'))
dict1['job'] = 'doctor'
print(dict1)
dict1['city']= 'Indore'
print(dict1)

dict1.update(D)
print(dict1)

x = dict1.popitem()
print(dict1)
print(x)


















