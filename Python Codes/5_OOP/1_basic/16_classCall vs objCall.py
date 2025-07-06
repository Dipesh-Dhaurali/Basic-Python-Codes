class Employee:
    name = "Dipesh"  # Class variable

    def __init__(self, age):
        self.age = age #Instance variable

    def show(self):
        print(f"name = {self.name}, age = {self.age}")

e = Employee(21)
e.show() # Call the show method using the object (instance method call)
print(e.name)  # it also can be done

print(Employee.name) # Access class variable directly using class name

"""
Note:
- 'name' is a class variable. It belongs to the class and is shared by all instances.
- You can access class variables using the class name: Employee.name
- 'age' is an instance variable. It is unique to each object.
"""
