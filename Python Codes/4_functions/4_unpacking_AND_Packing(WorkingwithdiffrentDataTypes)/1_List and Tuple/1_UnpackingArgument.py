"""
https://youtu.be/grOl8stdLsU
Python Guruji (Mastering 1_List and Tuple and Unpacking in Python: Complete Guide)
"""
# write theory form pdf (23) and same video staring

#Unpacking list

def fun(a,b,c,d):
    print(a,b,c,d)   #1 2 3 4

lst=[1,2,3,4]
fun(*lst)    #unpacking



#Unpacking Tuple
def funs(a,b,c,d):
    print(a,b,c,d)   #1 2 3 4

tup=(9,8,7,6)
funs(*tup)    #unpacking






"""
ERRRORRRR CODEDEEEEEE

def fun(a,b,c,d):
    print(a,b,c,d)

l=[1,2,3,4]
fun(l) # it will through error because we just only pass one argument as list

"""
