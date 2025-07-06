"""
follow pdf chapter 3 (64)
"""

mylist=[5,2,3,6,4,8]

#shorting with the number
#Ascending order
mylist.sort()
print(mylist) # [2, 3, 4, 5, 6, 8]

#Decending Order
mylist.sort(reverse=True)
print(mylist) # [8, 6, 5, 4, 3, 2]



#write output also


#######################################################





#shorting with alphabet character
mylist1=['e','z','i','k','b','a','n','q']

#Ascending order
mylist1.sort()
print(mylist1) # ['a', 'b', 'e', 'i', 'k', 'n', 'q', 'z']

#Decending Order
mylist1.sort(reverse=True)
print(mylist1) # ['z', 'q', 'n', 'k', 'i', 'e', 'b', 'a']


############################################################






#Shorting with alphabetical order
mylist2=['mango', 'cherry', 'apple', 'orange','banana']

#short in alphabetical order (Ascending order)
mylist2.sort()
print(mylist2)

#short in alphabetical order (Descending Order)
mylist2.sort(reverse=True)
print(mylist2)





#################################################


#Sorting with a Custom Key

mylist2=['rice', 'egg', 'apple', 'watermelon','banana']


#short according to the  length in order (small to big)
mylist2.sort(key=len)
print(mylist2)

#short according to the  length in order (big to small)
mylist2.sort(key=len,reverse=True)
print(mylist2)
