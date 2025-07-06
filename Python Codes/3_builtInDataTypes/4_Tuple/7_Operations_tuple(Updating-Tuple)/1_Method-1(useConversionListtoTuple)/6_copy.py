#copy method

tup1=('a','b','c','d','e')
temp=list(tup1)
tup=temp.copy()
tup1=tuple(temp)
print(tup1)

#assignment method
tup2=tup1
print(tup2)


