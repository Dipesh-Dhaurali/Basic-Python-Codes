#creating an empty tuple
tup=()
print(tup)  #()

#creating a single value tuple
tup1=(1,)
print(tup1) #(1,)    #note (comma is compulsory to make a singe tuple if we don't give the comma then  python will understand the value as integer or string)

#creating an numeric tuple
tup2=(1,2,3,4)
print(tup2) #(1, 2, 3, 4)
print(type(tup2))   #<class 'tuple'>

# creating a string tuple
tup3=('a','b','c','d','e')
print(tup3)

#it can hold multiple datatypes
tup4=(1,2,3.0,"Pass","Fail",True)
print(tup4)

#find the length of tuple
print(len(tup4))