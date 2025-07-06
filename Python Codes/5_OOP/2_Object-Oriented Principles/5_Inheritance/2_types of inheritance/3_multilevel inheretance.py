"""
code with harry (cont.)
https://youtu.be/Il7XMJJeXiA?list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg
+
sharadha(cont..)
"""
class A:
    def showA(self,name):
        print("This is super-class A ",name)

class B(A):
    def showB(self,name):
        print("This is class B which inherit form class A ",name)
        super().showA(1)

class C(B):
    def showC(self,name):
        print("This is class C which inherit form class B",name)


c=C()
c.showC(3)
c.showB(2)    #note we can access class B from the object of class c









"""
note:
Multilevel inheritance is the type of inheritance in OOP
where a derived class is inherit from another derived class. 

It is also called hierarchy inheritance.

This types of inheritance allows you to build a hierarchy 
classes where one class builds of upon another class.


syntax:
-------
class A:
  pass
class B(A):
 pass
class C(B):
 pass
"""