"""
https://youtu.be/DZIiigDWF_M
Gate Smashers (Append(), Extend(), Add(), Update() in Python 🐍 with Execution 💻🙇)
"""
# Joining two list using Append method

list1=[1,2,3,4,5]
list2=[7,8,9,10,11]



list1.append(100)
print(list1) #[1, 2, 3, 4, 5, 100]

list1.append([200,300])
print(list1) #[1, 2, 3, 4, 5, 100 ,[200,300]]

list1.append(list2)
print(list1) #[1, 2, 3, 4, 5, 100, [200, 300], [7, 8, 9, 10, 11]]
"""
note:
append is use to add the next list/element in last index of the existence list 
"""