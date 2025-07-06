"""
https://youtu.be/8-H-wIEbmjw
Digital Academy (Merge two Lists in Python (Extend))
"""
# Joining two list using extend method
list1=[1,2,3,4,5]
list2=[7,8,9,10,11]

list1.extend(list2)
print(list1) #[1, 2, 3, 4, 5, 7, 8, 9, 10, 11]

list2.extend([1,2,3])
print(list2) #[7, 8, 9, 10, 11, 1, 2, 3]