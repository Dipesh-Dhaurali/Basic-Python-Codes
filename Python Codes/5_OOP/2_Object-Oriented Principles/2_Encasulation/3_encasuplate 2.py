class Employee:
    def __init__(self,name,salary,role):
        self.name=name
        self.salary=salary
        self.role=role

    def show(self):
        return f"The name is {self.name}.Salary is {self.salary} and role is {self.role}"

    @staticmethod
    def respect(nme):
        print("I am good "+nme)

e=Employee('Dipesh',100000,'Web Dev')

print(e.show())
Employee.respect('sir')


"""
Note:
1) Hiding implementation details: 
------------------------------------------------------------------------
Users of an object don't need to know how it works internally, 
only how to use it (like eating a mango without knowing about the seed).


2) Improving usability and maintainability:
------------------------------------------------------------
By hiding complexity, it makes code easier to use for other 
programmers and simpler to maintain.
"""

