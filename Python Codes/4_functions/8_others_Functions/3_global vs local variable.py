"""
cont...(CWH)
"""
# we can overwrite the global variable inside function using global keyword
x=10 #global variable

def var():
    global x
    x=5        #global variable override and change value


var()
print(x)    #5     => change the value 10 to 5 because of global variable

