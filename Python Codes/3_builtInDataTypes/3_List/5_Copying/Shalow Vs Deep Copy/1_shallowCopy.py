"""
https://youtu.be/SgUwPDT9tEs

https://youtu.be/vu5-QWe_iLU
"""

list1=[1,2,3,[5,6,7],[8,9]]
l=list1.copy()
l[2]=101  #[1,2,101,[5,6,7],[8,9]]
l[3][1]=102 #list1=[1,2,101,[5,102,7],[8,9]]
l[4][0]=103 ##list1=[1,2,101,[5,102,7],[103,9]]

print("Original list: ",list1)    #output   Original list:  [1, 2, 3, [5, 102, 7], [103, 9]]
print("Copied list  : ",l)        #Copied list  :  [1, 2, 101, [5, 102, 7], [103, 9]]


"""
note:-
1) At index [2] shallow copy doesn't affect because it is not nested list and shallow copy only not work in nested list
2) At index [3][1] it is affected in shallow copy because it is nested list
3) which means modifying to the nested list affect to the original list in shallow copy
"""