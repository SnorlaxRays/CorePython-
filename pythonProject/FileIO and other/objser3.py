import pickle
import re

import objSer2
file = open("Objtest","rb")
file1 = open("Objtest1","w")

newone = pickle.load(file)
for i in newone:
    file1.write( " " +i )

file.close()
file1.close()
