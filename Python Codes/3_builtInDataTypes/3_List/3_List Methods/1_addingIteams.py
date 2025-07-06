mylist=["Apple","Mango","Papaya"]

#1) append   => it add the element to the end
mylist.append("strawberry")
print(mylist)  #['Apple', 'Mango', 'Papaya', 'strawberry']

#2) insert => insert element at index (middle , cornet , last ) etc
mylist.insert(1,"Banana")
print(mylist) #['Apple', 'Banana', 'Mango', 'Papaya', 'strawberry']

#3) extend => 1_Adding multiple items to the end of the list
mylist.extend(["pineapple","Grapes","Orange"])   #['Apple', 'Banana', 'Mango', 'Papaya', 'strawberry', 'pineapple', 'Grapes', 'Orange']
print(mylist)