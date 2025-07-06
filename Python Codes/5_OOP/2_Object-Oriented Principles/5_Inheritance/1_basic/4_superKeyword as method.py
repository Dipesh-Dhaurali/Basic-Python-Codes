"""
code with harry(#72)
+
shradha khapra(24:47)
"""
class ParentClass:
    def parentMethod(self):
        print("This is an parent class")

class ChildClass(ParentClass):
    def childMethod(self):
        print("This is an child class")
        super().parentMethod()

c=ChildClass()
c.childMethod()





"""
note:
The super keyword in python is used to refer to the parent class.
It is especially useful when a class inherit form
multiple parent classes and you want to call a method from
one of the parent classes.
"""