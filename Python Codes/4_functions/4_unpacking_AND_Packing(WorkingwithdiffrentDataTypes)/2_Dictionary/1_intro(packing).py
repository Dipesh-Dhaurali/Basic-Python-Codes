"""
https://youtu.be/grOl8stdLsU
Python Guruji (Mastering Packing and Unpacking in Python) (9:55)
"""
#dictionary unpacking and packing using (**kwargs)
def fun(**data):
    print(data)

fun(name='Dipesh',age=21,address='ktm')



#method 2
def done(**data):
    return data

a=done(name='Dipesh',age=21,address='ktm')
print(a)



#method 3
def sun(**args):
    print(args)

dict1={
    'name':'dipesh',
    'age':21
   }
sun(**dict1)
