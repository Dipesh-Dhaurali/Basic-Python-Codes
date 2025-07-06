"""
learn coding(Python Method Overriding)
"""

class A:  #parent
    def show(self):
        print("This is parent class")

class B(A): #child class
    def show(self):
        print("This is child class")

obj=B()
obj.show()

# note function name should be compulsory for method overriding inside
# inheritance






"""
note
----
1) whenever we writing method name with same signature in parent and 
child class called method overriding

2) inheritance is compulsory for method overriding
"""