"""
https://youtu.be/ZMCte_LHml0
(8:06)
"""
import copy
lst=[2,3,4,5,6]
l=copy.copy(lst)
l[0]=1
print("Original list : ",lst)
print("Copied list   : ",l)

# it solved the previous problem
# which means modifying to the copied list doesn't affect to the original list
#This is another way to create a shallow copy using the copy module.
