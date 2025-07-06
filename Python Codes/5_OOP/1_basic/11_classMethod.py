"""
code with harry(#69)
https://youtu.be/9ynmDLc5FYo
+
shradha khapra(#9/9 (26:55))
https://youtu.be/bAwmZVJeO5s?list=PLGjplNEQ1it8-0CmoljS5yeV-GlKSUEt0
"""

class Student:
    college="MorganCollege"

    def __init__(self,name):
        self.name = name

    def display(self):
        print(f"College_name={self.college} Name={self.name}")

    @classmethod  #it is compulsory
    def changeCollege(cls,newCollege):
        cls.college=newCollege

s=Student('Dipesh')
s.display()

s.changeCollege('Padmodaya College')
s.display()

print(Student.college)



"""
note:
1) A class method in Python is a method that is bound 
to the class and not the instance of the class, 
and it takes the class (cls) as its first argument.

2) it helps to change the class variable permanent
"""