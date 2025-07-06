"""
bro code (cont...)
"""


a=5
try:
    n = int(input("Enter any number : "))   # user supposes to write string name inside integer
    div=a/n
    print(div)
except Exception as e:
    print(e)
