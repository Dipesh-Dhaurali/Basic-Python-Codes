#step slicing
list1=["Apple","Banana","Mango","Grapes","Pineapple","Carrot"]

#postive

print(list1[::]) # print all
print(list1[::1]) # print all

print(list1[0::3]) # ['Apple', 'Grapes']
print(list1[::3]) # ['Apple', 'Grapes']

print(list1[1:5:2]) # ['Banana', 'Grapes']
print(list1[1:6:2]) # ['Banana', 'Grapes']

print(list1[::2])  #['Apple', 'Mango', 'Pineapple']


#negaive

# reverse the list
print(list1[::-1])  #['Carrot', 'Pineapple', 'Grapes', 'Mango', 'Banana', 'Apple']

print(list1[-5:-1:2]) #['Banana', 'Grapes']