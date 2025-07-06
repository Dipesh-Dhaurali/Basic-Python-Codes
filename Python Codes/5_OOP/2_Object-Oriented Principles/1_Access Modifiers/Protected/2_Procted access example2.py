# Protected access modifier=>method tries to access inside/outside the class
class Sum:
    _a=5
    _b=10

    def _add(self):
        s=self._a+self._b
        print(s)

    def show(self):
        self._add()

obj=Sum()

obj.show()   #inside class access
obj._add()   #outside class access
#no need to use (name mangling)