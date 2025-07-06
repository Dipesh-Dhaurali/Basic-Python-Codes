"""
shradha(cont...(30:39))
"""
#Methods are a function that belongs to objects.

class Person:
    def __init__(self,name):
        self.name=name

    def greet(self):
         print("hello",self.name)

p1=Person("Dipesh")
p1.greet()

p2=Person("Kritika")
p2.greet()
