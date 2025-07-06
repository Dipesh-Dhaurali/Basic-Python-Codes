"""
learn coding(Python Method Overloading)
+
https://youtu.be/15pZbi_MtcY
"""
class A:
    def show(self):
        print("Welcome")

    def show(self,firstname=''):
        print("Welcome",firstname)

    def show(self,firstname='',lastname=''):
        print("Welcome",firstname,lastname)


obj=A()
obj.show()
obj.show('dipesh')
obj.show('dipesh','dhaurali')
obj.show(4,5)













""""
Note
----
Whenever class contains more than one methods
with same name and different types parameter 
called method overloading
"""