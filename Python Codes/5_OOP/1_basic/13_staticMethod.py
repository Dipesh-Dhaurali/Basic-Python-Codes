"""
sharadha(cont...40:09)
"""
#Method that don't use the self-parameter (work at class level)
# if you are not using the self-method then make it as static class
# to make any function to static use the @staticmethod decorator

"""
Decorator allows us to wrap another function in order to 
extend the behaviour of the wrapped function,without permanently
modifying it
"""

class Student:

    @staticmethod
    def college():
        print("Morgan College")

s=Student()
s.college()


#note if you don't make a decorator and try to make a method without a self-parameter than it will through error

