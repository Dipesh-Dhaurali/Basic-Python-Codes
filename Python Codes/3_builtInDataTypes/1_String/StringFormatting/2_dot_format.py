name="Dipesh"
age=21
address="Kathmandu"

#method 1
print("Hi! My name is {}, I am {} years old and I live in {}".format(name,age,address))


#method 2
str1="Name: {} , Age:{} , Address:{}"
print(str1.format(name,age,address))

#method 3
str1="Name: {} , Age:{} , Address:{}"
print(str1.format(name,age,address))

#method 4
str1="Name: {0} ,Address: {2} , age: {1}"
print(str1.format(name,age,address))

#method 5
str1="Name: {n} ,Address: {A} , age: {a}"
print(str1.format(n=name,a=age,A=address))

