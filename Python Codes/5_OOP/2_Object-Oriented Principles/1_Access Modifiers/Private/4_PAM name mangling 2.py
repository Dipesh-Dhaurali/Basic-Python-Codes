"""
cont...
"""

class Student:
    def __init__(self):
        self.__name='dipesh'


s=Student()
print(s._Student__name)
# can be accessed private access modifier
# indirectly 


"""
note:
In python , There is no strict concept of "private" access
modifier like in some other programming languages however 
conversions has been established to indicate that variable or method 
should considered private by prefixing its name with underscore(__).
This is known as a "weak internal  use indicator"and its convention only,
not a strict rule. Code outside the class can still access this"private"
and variables and methods , but it is generally understood that they
should not be access or modifier.
"""