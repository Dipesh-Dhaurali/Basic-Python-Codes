"""
cont...(CWH) (6:28)
"""
# we can fix previous problem by global keyword

x=10 #global variable

def var():
    global y
    y=5        #global variable because of global keyword


var()
print(x)    #10
print(y)    #5       =>  now it will fix

# local variable will be destroyed after return statement but global don't