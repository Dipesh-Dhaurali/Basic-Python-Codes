# Protected access modifier==> variable tries to access inside/outside the class
class Students:
    _College="Morgan College"

    def __init__(self,name):
        self._name=name

    def show(self):
        print(f"My name is {self._name} and college name is {self._College}")


d=Students("Dipesh")
d.show()             #inside class access
print(d._College)    # outside class access
#no need to use (name mangling)



#by using single underscore we can access the
# protected access modifier directly