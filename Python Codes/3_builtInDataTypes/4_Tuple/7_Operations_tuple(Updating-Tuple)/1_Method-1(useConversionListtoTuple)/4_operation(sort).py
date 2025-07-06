tup1=(5, 2, 3, 6, 4, 8)

#Accending Order
temp=list(tup1)
temp.sort()
tup1=tuple(temp)
print(tup1)

#Decending Order
temp=list(tup1)
temp.sort(reverse=True)
tup1=tuple(temp)
print(tup1)

#Accending Order
temp=list(tup1)
temp.sort(reverse=False)
tup1=tuple(temp)
print(tup1)

#Custom Order
tup2=('apple','banana','cat')
temp=list(tup2)
temp.sort(reverse=False,key=len)
tup2=tuple(temp)
print(tup2)