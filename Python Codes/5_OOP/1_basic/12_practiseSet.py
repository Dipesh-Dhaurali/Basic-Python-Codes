"""
cont...shradha(35:03)

Create a student class that takes the name and marks
of 3 subjects as argument in constructor.
"""
class Student:
    def __init__(self,name,marks):     #use *marks for multiple values
        self.name=name
        self.marks=marks

    def totalMarks(self):
        tmark=0
        for i in self.marks:
            tmark+=i
        return tmark

    def display(self):
        print(f"name={self.name} marks={self.marks} totalMark={self.totalMarks()}")

s1=Student('Dipesh',[10,20,30])  #if you use *marks then don't use any brackets
s1.display()
