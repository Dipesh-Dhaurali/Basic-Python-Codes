"""
https://youtu.be/KEpmUPxxjxI
Jenny's Lectures CS IT (Nested 2_List in Python)
"""
# Nested list referees to the list within the list

#nested list creation
list1=[1,2,3,[5,6,7],10]

#lenght of the nested list
print(len(list1)) #5   (if you count it is 7 ) but its length is 5


#nested list access
print(list1[0]) #1
print(list1[3])  #[5, 6, 7]
print(list1[3][1])  #6
print((list1[-2]))  #[[5, 6, 7]

#slicing in nested list
print(list1[3:]) #[[5, 6, 7], 10]
print(list1[1::2]) #[2, [5, 6, 7]]
