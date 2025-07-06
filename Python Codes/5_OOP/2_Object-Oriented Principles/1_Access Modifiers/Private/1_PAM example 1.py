"""
cont(cwh)

Private members of a class (variables, methods)
are those members which are only accessible inside the class
we cannot use private members outside the class

We need to use double underscore after self. to use
private access modifier

"""

class Student:
    def __init__(self):
        self.__name='dipesh'


s=Student()
print(s.__name)

#so it cannot be accessed directly
# as it is a private access modifier


"""
note:
private attrivute and methods are meant to be used only within
the class and are not same accessible from outside the class. 
"""