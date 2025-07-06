"""
Telusko (Python Inner class)
https://youtu.be/b7JzgybKvys
"""
class Student:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll


    def show(self):
        print(self.name,self.roll)

    class marks:
        def __init__(self,python,SDD,IS):
            self.python=python
            self.SDD=SDD
            self.IS=IS

        def show(self):
            print(self.python, self.SDD,self.IS)

s1=Student('Dipesh',1)
s2=Student('Kritika',2)

s1.show()
s2.show()

m1=Student.marks(90,80,95)
m2=Student.marks(91,81,96)
m1.show()
m2.show()