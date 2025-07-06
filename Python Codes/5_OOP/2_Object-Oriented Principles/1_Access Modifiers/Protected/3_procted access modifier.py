"""
cont...(code with hary)
"""
#Procted access modifier in inheritance
class Student:
    def __init__(self):
        self._name='dipesh'
        self._age=21
class Subject(Student):
    def __init__(self):
        super().__init__()
        self._mrk=100


s1=Subject()
print(s1._name)
print(s1._mrk)
print(s1._age)

