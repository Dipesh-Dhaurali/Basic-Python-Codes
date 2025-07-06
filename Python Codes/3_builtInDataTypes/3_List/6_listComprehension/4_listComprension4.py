"""
https://youtu.be/YlY2g2xrl6Q

bro Code (Learn Python LIST COMPREHENSIONS in 10 minutes!)
"""
# 2_List Comprehension = A way to create lists in python compact
#                      and easier to read than traditional loops

# syntax
# list = [expression    for value in iterable      if condition]

#################################################################
#normal way to print double of numbers
double=[]
for i in range(1,11):
    double.append(i*2)

print(double)




#list comprehension
dbl=[i*2 for i in range(1,11)]
tpl=[i*3 for i in range(1,11)]
square=[i*i for i in range(1,11)]

print(dbl)
print(tpl)
print(square)