"""
cont...(2:24)(#81)
"""
class CEO:
    def showCEO(self):
        print("I am the CEO of this office")

class Manager1(CEO):
    def showManager1(self):
        print("I am the General manager of this office")

class Manger2(CEO):
    def showManager2(self):
        print("I am the Assistant manager of this office")

class Employee(CEO):
    def showEmployee(self):
        print("I am the Employee of this office")

m=Employee()
m.showEmployee()














"""
Note:-
------
Hierarchical inheritance is a type of inheritance in OOPS
where multiple subclasses inherit form , a single base class.

A single base class act as a parent class for multiple subclasses.
"""
