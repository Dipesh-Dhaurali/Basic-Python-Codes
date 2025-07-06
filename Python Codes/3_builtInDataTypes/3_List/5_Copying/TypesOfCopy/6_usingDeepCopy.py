"""
https://youtu.be/UTQgpP5o3-o
"""
import copy
lst=[2,3,4,5,6]
l=copy.deepcopy(lst)
l[0]=1
print("Original list : ",lst)
print("Copied list   : ",l)

# it solved the previous problem
# which means modifying to the copied list doesn't affect to the original list
#This is the way to create a deep copy using the copy module.
