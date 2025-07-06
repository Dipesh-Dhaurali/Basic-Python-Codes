"""
shradha(cont... 26:34)

#attribue inside class => same for all

# attribute inside constructure/
 object attribute => different of each

"""

class Student:
    college_name="Morgan College"  #class attribute / class variable

    def __init__(self,name,age):
        self.name=name #obj attribute / object variable
        self.age=age

    def info(self):
        print(f"College={self.college_name}Name={self.name} Age={self.age}")


s1=Student('Dipesh',22)
s1.info()

s2=Student('Kritika',22)
s2.info()


#note college is for everyone because of class attribute