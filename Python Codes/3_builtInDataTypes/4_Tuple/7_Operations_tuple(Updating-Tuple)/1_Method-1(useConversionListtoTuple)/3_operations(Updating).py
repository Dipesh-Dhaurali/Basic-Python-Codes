"""
cont...
"""
#updating the tuple
fruits=("Apple","Banana","Carrot","Mango","Grapes","Pineapple")

#updating the single element of the tuple
temp=list(fruits)
temp[1]="Orange"
fruits=tuple(temp)
print(fruits)


#updating the multiple element of the tuple
temp=list(fruits)
temp[2:5]=["Guava","Tomato","Cherry"]
fruits=tuple(temp)
print(fruits)
