# PAM method tries to access inside/outside the class
class Sum:
    __a=5
    __b=10

    def __init__(self,dip):
        self.__c=dip        #don't worry its 'dip' because it works like this also

    def __add(self):
        s=self.__a+self.__b+self.__c
        print(s)

    def show(self):
        self.__add() #inside access of method (private access modifier method)

obj=Sum(5)
obj.show()   #inside access


# obj.__add() #outisde access of method (private access modifier method)
            # so not work so it will give error

#to access indirectly, we need to use name mangling
obj._Sum__add()



