"""
shradha(cont..) (10:50)
"""
# PAM method tries to access inside the class
class Person:
    __name="anonymous"

    def __hello(self):
        print("hello person")

    def welcome(self):
        self.__hello()    #inside the class access

p1=Person()
print(p1.welcome())
