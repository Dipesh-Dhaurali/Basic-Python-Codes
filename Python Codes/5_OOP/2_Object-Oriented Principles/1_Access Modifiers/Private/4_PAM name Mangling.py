# private access modifier trying to access outside the class indirectly

class Students:
    __College="Morgan College"

    def __init__(self,name,age):
        self.__name=name
        self.__age=age


dip=Students('Dipesh',20)
print(dip._Students__College)
print(dip._Students__name)
# it is name mangling, and we can access private access modifier form outside indirectly

"""
syntax
------
myobj._ClassName__attributeName
"""


"""
Note:
There is no real concept of private or protected in Python, 
It's just a convention or a note to avoid using certain variables or methods. 
Technically, we can still access them from outside the class because 
they're not truly private or protected. 
It's more like a sticky note saying, "Don't touch my car.
"""