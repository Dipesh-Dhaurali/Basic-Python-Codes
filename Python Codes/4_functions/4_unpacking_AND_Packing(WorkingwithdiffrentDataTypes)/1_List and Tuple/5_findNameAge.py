#example 1 of packing
def person(*args):
    print(args)

person('Dipesh',21,'Male',60000)


#example 2 of packing
def person(*args):
    print(args)

tup1=('Dipa',16,'Female',80000)
person(*tup1)



#example 3 of packing
def emp(*data):
    return data

list1=['Krtika',20,'Female',50000]
a=emp(*list1)
print(a)





#we can also use tuple instead of list just replace bracket other same
#write output also