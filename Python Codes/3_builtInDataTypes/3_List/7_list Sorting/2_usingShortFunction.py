#Using Short Function
"""
Returns a new sorted list and leaves the original list unchanged.
Supports the same parameters as sort()


follow pdf chapter 3 (66)
"""

mylist=[5,2,3,6,4,8]

#Assending order
s=sorted(mylist)
print(s) #[2, 3, 4, 5, 6, 8]

#Decending order
s=sorted(mylist,reverse=True)
print(s) #[8, 6, 5, 4, 3, 2]

########################################

mylist2=['rice', 'egg', 'apple', 'watermelon','banana']

#Assending order
s=sorted(mylist2)
print(s) #['apple', 'banana', 'egg', 'rice', 'watermelon']

#Decending order
s=sorted(mylist2,reverse=True)
print(s) #['watermelon', 'rice', 'egg', 'banana', 'apple']

#custom key (small to big)
s=sorted(mylist2,key=len)
print(s) #['egg', 'rice', 'apple', 'banana', 'watermelon']

#custom key (big to small)
s=sorted(mylist2,key=len,reverse=True)
print(s)  #['watermelon', 'banana', 'apple', 'rice', 'egg']

# write with output
