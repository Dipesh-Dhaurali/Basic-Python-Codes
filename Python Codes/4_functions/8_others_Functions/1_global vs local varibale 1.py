"""

https://youtu.be/RaG6GgcDt54
CWH (Local vs Global Variables in Python #48) (5:15)
"""
# theory local variable and global variable form chatgpt




x=10 #global variable

def var():
    y=5        #local variable

var()
print(x)  #10
#  print(y)      # this will cause an error because y is a local variable

