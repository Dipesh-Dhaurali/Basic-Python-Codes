"""
cont..sharadha
+
cwh(#58)
"""
class Student:
    #parametrized constructors
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print(f"My name is {self.name} and my age is {self.age}")


s1=Student('kritika',20)
s1.display()

s2=Student('dipesh',21)
s2.display()


"""
Here,
s1=object
Student() is class name 
('kritika ' 20) this is attribute
def__init__() is constructors also called dunder method
"""