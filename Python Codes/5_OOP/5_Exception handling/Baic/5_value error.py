"""
cont...(bro code)
"""
a=5

try:
    n = int(input("Enter any number : "))   # user supposes to write string name inside integer
    div=a/n
    print(div)
except ValueError as e:
    print("Enter only number",e)
except ArithmeticError:
    print("It cannot be zero")

"""
value errors occur when we try to typecast
in wrong datatype

example
--------
int("hello")


"""