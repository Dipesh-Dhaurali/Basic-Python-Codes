"""
cont...
"""
import pickle
file=open(r'G:\My Drive\Coding\BOARD_EXAMS\6_File input or output\7_Binary Files\Hidden\hidden.dat','wb')
a=5
b=5.5
str1='hello'
list1=[1,2,3,4]
tuple1=(5,6,7,8)
dict1={
    'name':"dipesh",
    'age':18
}

pickle.dump(a,file)
pickle.dump(b,file)
pickle.dump(str1,file)
pickle.dump(list1,file)
pickle.dump(tuple1,file)
pickle.dump(dict1,file)


file.close()