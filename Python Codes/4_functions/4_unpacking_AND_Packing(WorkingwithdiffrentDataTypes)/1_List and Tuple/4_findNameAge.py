#example 1 of unpacking
def person(name,age,gender,address):
    return name,age,gender,address

list1=['Dipesh',21,'Male','Ktm']
a,b,c,d=person(*list1)
print(a,b,c,d)




#example 2 of unpacking
def emp(name,salary,age):
    print(f"My name is {name},I am {age} years old and my salary is {salary}.")

lst=['kritka',50000,20]
emp(*lst)

#we can also use tuple instead of list just replace bracket other same
