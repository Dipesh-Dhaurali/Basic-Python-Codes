"""
code with harry(#78)
https://youtu.be/U53_Gw55NI8?list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg

+
shradha(cont..(16:55))
"""

class Animal:
    def __init__(self,legs):
        self.legs=legs

    def showAnimal(self):
        print(f"Animal can walk and it has {self.legs} legs")


class Dog(Animal):
    def showDog(self):
        print("It can bark")
        super().showAnimal()

d=Dog(4)
d.showDog()







"""
note:
single inheritance is a type of inheritance
where a class inherits proporties and behaviour form 
a single parent class.

syntax:
------
class ChildClass(ParentClass):
    pass
"""