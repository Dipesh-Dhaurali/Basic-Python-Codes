"""
sharadha(oop part 2 (1:00))#9
"""


class Student:
    def __init__(self,name):
        self.name=name

    def show(self):
        print(self.name)


s=Student('Dipesh')
del s
s.show()


# it will delete an object