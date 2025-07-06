"""
https://youtu.be/XGBJ89zQLrM
Amit Thinks  (copy of the Python 2_List using copy() method )

"""


lst=[2,3,4,5,6]
l=lst.copy()
l[0]=1
print("Original list : ",lst)
print("Copied list   : ",l)

# it solved the previous problem
# which means modifying to the copied list doesn't affect to the original list