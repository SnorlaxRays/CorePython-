list1 = []
for i in range(100,999):
    for j in range(100,999):
        mult = i*j
        if len(str(mult))==6:
            mult = str(mult)
            for k in range(len(mult)):
                if mult[k] != mult[-(k+1)]:
                    break
            else:
                list1.append(mult)

list1.sort()
a = list1[-1]
a = int(a)

list2 = []
for i in range(2,a):
    if a%i==0:
        if len(str(i))==3:
            list2.append(i)

#print(list2[-2:])
print(list2[-1]*list2[-2])











