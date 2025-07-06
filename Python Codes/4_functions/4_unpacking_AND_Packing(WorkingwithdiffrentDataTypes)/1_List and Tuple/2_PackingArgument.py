"""
https://youtu.be/grOl8stdLsU
Python Guruji (cont...)
"""

#packing using tuple
#method 1
def fun(*args):
    print(args)


fun(1,2,3,4,5,6)


#method 2
def fun(*args):
    print(args)

tup1=(1,2,3,4,5,6)
fun(*tup1)  #star is most


#####################################################
# packing using list
def fun(*args):
    print(args)

list1=[1,2,3,4]
fun(*list1)   # star is most