"""
https://youtu.be/SgUwPDT9tEs

https://youtu.be/vu5-QWe_iLU
"""

import copy

list1=[1,2,3,[5,6,7],[8,9]]
l=copy.deepcopy(list1)
l[2]=101
l[3][1]=102
l[4][0]=103

print("Original list: ",list1)    #output   Original list:  [1, 2, 3, [5, 6, 7], [8, 9]]
print("Copied list  : ",l)        #Copied list  :  [1, 2, 101, [5, 102, 7], [103, 9]]


#it fixes the nested list problem/ shallow copy problem
# which means modifying to the nested list doesn't affect to the original list

# need to import copy method compulsory
# need to pass value inside deepcopy() function
