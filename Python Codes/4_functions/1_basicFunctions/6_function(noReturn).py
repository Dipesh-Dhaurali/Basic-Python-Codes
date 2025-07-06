"""
cont...12:30 (sharada)
"""

# function without return

def greet():
    print("Namaste!")

print(greet())

#I am trying to print the function so it returns none
# because this function does not return anything's

"""
output
Namaste!
None
"""


# function with return
def greet():
    print("Namaste!")
    a=5
    b=10
    s=a+b
    return s

print(greet())

#I am trying to print the function, and it has rerun statement
# so it never return none
"""
output
Namaste!
15
"""