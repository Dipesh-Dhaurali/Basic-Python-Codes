"""
learn coding (Python Encapsulation) (6:15)
"""
class A:
    _a=10 #protected
    __b=20 #private

    def show(self):
        print(f"a={self._a} b={self.__b}")

obj=A()
obj.show()

print("outisde class",obj._a)

#print("outisde class",obj.__b)  #cannot access directly

print("outisde",obj._A__b)  # can be print with name mangling



""""
Note:
----------------------------------------------------------------
Protected                        ||           Private
----------------------------------------------------------------
=> Can access inside class    ||   Can access inside class 
=> Can access outside class   ||   Cannot access directly outside class 
(not recommended) 
=> Can be used in inheritance ||   Not directly usable in inheritance (name mangling)
=> No name mangling           ||   Uses name mangling


"""