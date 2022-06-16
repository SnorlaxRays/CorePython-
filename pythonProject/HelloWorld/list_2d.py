list_2d = [[(i*j) for j in range(1,11)] for i in range(2,11)]
print(list_2d)


list = []
for i in range(2,11):
    list2 = []
    for j in range(1,11):
        list2.append(i*j)
    list.append(list2)
print(list)