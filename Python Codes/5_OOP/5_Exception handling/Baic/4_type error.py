"""
bro code (Python EXCEPTION HANDLING)
"""
a=1
b="1"
try:
    sum=a+b
    print(sum)
except TypeError as e:
    print(e)





"""
 type errors occur when you tried to do some operations
 in different data types

example
-------
a=1
b="1"
c=a+b
"""