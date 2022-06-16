'''
file = open("Test.txt") # open file
text = file.read(10) #read binary data
print(text)

file.close() #close method


file = open("Test.txt")

for line in file:
    print(line, end="")

file.close()

import re
def readLine():
    file = open("Test.txt")
    for line in file:
        if(re.search("python",line)):
            print(line,end='')
    file.close()

readLine()


file = open("C:\\Users\\Sandeep Ratnawat\\Desktop\\Snorlax\\Dexter.txt","w")
file.write("Hi\n")
file.write("This is Python file")
file.close()

with open("C:\\Users\\Sandeep Ratnawat\\Desktop\\Snorlax\\DeeDee.txt","w") as file:
    file.write(("Hello\n"))
    file.write("I am Dexter's elder sister")

'''
'''


import os
os.rename("test1.txt","test2.txt")
os.remove("test2.txt")


file = open("test1.txt")
str = file.read(10)
print(str)
position = file.seek(5)
str1 = file.read(10)
print(str1)
position = file.tell()
print(position)

file1 = open("Dexter1.py","x")
print(file1)
'''
f = open('snorlax.txt')
f = open('snorlax.txt','w')
f = open('snorlax.txt','r+')
f = open('snorlax.txt','rb')


