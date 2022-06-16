import pickle


list = ['Dexter','Snorlax','cooler','1','4567']

f = open('ObjTest','wb')



pickle.dump(list,f)
f.close()

'''
import pickle
f = open('Objtest',"rb")
list = pickle.load(f)
print(list)
f.close()
'''


