"""
Write a Python program that demonstrates list
operations such as indexing, slicing,
modifying elements, appending items,
sorting, and list comprehension.
"""

list1=[1,2,3,4,5,6,7,8]

#indexing
print(list1[0])
print(list1[7])


#positive slicing
print(list1[1:5])
print(list1[::1])
print(list1[::2])
print(list1[1:6:2])
print(list1[0:len(list1):])

#negative slicing
print(list1[-8::])
print(list1[-8:-3])
print(list1[-8:-3:1])
print(list1[-8:-3:2])
print(list1[::-1]) #rev

#modifying elements
list1[2]=10
print(list1)

#appending items
list1.append(10)
print(list1)


#sorting
list1.sort()  #increasing order
print(list1)

list1.sort(reverse=True) #decreasing order
print(list1)


            #list comprehension

#find squares num from list
num=[3,4,5,6]
sqr=[x**2 for x in num]
print(sqr)


#find even num
even=[x for x in num if x%2==0]
print(even)