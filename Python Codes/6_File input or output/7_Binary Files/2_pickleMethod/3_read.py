"""
cont...
"""
import pickle
file=open(r"G:\My Drive\Coding\BOARD_EXAMS\6_File input or output\7_Binary Files\Hidden\hidden.dat",'rb')
a=pickle.load(file)
b=pickle.load(file)
c=pickle.load(file)
d=pickle.load(file)
e=pickle.load(file)
f=pickle.load(file)

print(a,b,c,d,e,f)

file.close()