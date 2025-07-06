"""
cwh (cont.. 57)
"""
class Person:
    name = 'Kritika'
    occupation = "Software engineer"

    def student(self):
        print(f"{self.name} is an {self.occupation}")


p1=Person()
p1.name='dipa'
p1.occupation='Accountant'
p1.student()


p2=Person()
p2.name='dipesh'
p2.occupation='Web Developer'
p2.student()

p3=Person()
p3.student()  #default