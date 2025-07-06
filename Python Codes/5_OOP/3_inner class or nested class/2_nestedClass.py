class Student:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
        self.mrk=self.marks()   #inner class object

    def show(self):
        print(self.name,self.roll)
        self.mrk.show()  #inner class show method call

    class marks:
        def __init__(self):
            self.python=10
            self.SDD=20
            self.IS=30

        def show(self):
            print(self.python, self.SDD,self.IS)

s1=Student('Dipesh',1)
s2=Student('Kritika',2)

s1.show()
s2.show()

