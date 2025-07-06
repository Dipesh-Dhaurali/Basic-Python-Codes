"""
cont..
https://youtu.be/4o7xSHgKlvI?list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg
"""
#assume all three class refers to the same person
class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id

class Dancer:
    def __init__(self,type1,type2):
        self.type1=type1
        self.type2=type2

class DancerEmployee(Employee,Dancer): #refers for personal
    def __init__(self,favcol,favfood):
        Employee.__init__(self,'Kritika',101)
        Dancer.__init__(self,"bharatanatyam","Kathak ")
        self.favcol=favcol
        self.favfood=favfood


    def showPerson(self):
        print(f"""
                My name is {self.name},
                My emp-id is {self.id}
                I like to dance {self.type1} and {self.type2}
                My favourite food is {self.favfood}
                and my fev colour is {self.favcol}           
        """)


d=DancerEmployee('white','pizza')
d.showPerson()






"""
note:
Multiple inheritance is the powerful
features in python that allows a class to
inherit attributes and methods from multiple
parent classes.

syntax:
------
class Child(parent1,parent2,parent3):
    pass 
"""