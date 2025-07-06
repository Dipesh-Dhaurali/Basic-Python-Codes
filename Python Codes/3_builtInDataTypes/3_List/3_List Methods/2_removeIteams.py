mylist=[1,2,3,4,5,6,7,8,9,10]

#1) remove => removes first occurrence  of element by searching

mylist.remove(5)
print(mylist) #[1, 2, 3, 4, 6, 7, 8, 9, 10]

#2) pop => remove element at index ( start , mid, end ) etc

mylist.pop()  # note : if the pop is empty default it will remove the value from the last element of the list
print(mylist) #[1, 2, 3, 4, 6, 7, 8, 9]

mylist.pop(0)
print(mylist) #[2, 3, 4, 6, 7, 8, 9]

#3) del => # Removing an item by index without returning it

del mylist[2] #it will delete index 2
print(mylist) #[2, 3, 6, 7, 8, 9]

del mylist[1:4]  #it will delete list from index 1 to 3
print(mylist) #[2, 8, 9]

# del mylist    # it will delete entre list with variable name
# print(mylist)  #throw error because it is already deleted

#4 Clear => remove all items from a list using without deleting variable name
mylist.clear()
print(mylist)  #output []




