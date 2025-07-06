"""
cont..(cwh)#82
"""
class A:
    def showA(self):
        print("It is parent class")

class B(A):
    def showB(self):
        super().showA()
        print("It is Class B extends form A")

class C(A):
    def showC(self):
        print("It is Class C extends form A")

class D(B,C):
    def showD(self):
        super().showB()
        super().showC()
        print("It is Class D extends form B and C")


obj=D()
obj.showD()





"""
Note:
----
Hybrid inheritance is the combination of multiple inheritance and
single inheritance .


syntax:
------
class ChildClass(ParentClass):
    pass

class Child(parent1,parent2,parent3):
    pass 
"""