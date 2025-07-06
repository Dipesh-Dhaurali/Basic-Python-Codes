# convert list to string
list1=["apple","banana","carrot"]

str1=str(list1) #use str constructor to convert list to string
print(str1) #['apple', 'banana', 'carrot']
print(type(str1)) #<class 'str'>


#--------------- #method 2 for list to string
str=" ".join(list1)
print(str)     # apple banana carrot
print(type(str))  #<class 'str'>



#########################################################

# convert string to list
str2="Hello"

list2=list(str2)
print(list2) #['H', 'e', 'l', 'l', 'o']
print(type(list2)) #<class 'list'>


#--------------- #method 2 for string to list
list3=str2.split()  #it converts the string to the list
print(list3)     #['Hello']


