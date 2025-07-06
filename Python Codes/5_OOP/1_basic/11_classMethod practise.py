class Employee:
    company="TheNextEducation"
    name="Dipesh"

    def __init__(self,age):
        self.age= age

    def show(self):
        print(f'''My name is {self.name} and 
        I currently works in {self.company}
        and I am {self.age} years old ''')

        #main work
    @classmethod
    def changeCompany(cls,newCompany):
        cls.company=newCompany


e=Employee(20)
e.show() #TheNextEducation


#the main work
e.changeCompany('MercyEducation')
e.show()#MercyEducation

print(Employee.company)  #dont do e.company



"""
Note
-----
With @classmethod → it focuses on the class rather 
than the object, so change in class variable 
is permanent because it is a shared variable, 
and changing it affects all instances.


Without @classmethod → it focuses on the object. 
Objects can be made many times, so it can’t 
change the class variable permanently. 
It only changes it for that specific object, 
which is a temporary override at the instance level.
"""