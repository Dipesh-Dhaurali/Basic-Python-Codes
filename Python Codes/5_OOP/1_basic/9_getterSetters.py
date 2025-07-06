"""
cwh(#60)

#write a program to calculate
area of rectangle
"""
class Rectangle:
    def __init__(self,l,b):
        self.length=l
        self.breadth=b

    @property #getter decorators
    def area(self):
        return self.length * self.breadth

    @area.setter
    def area(self, dimensions):
        l, b = dimensions #unpacking
        self.length = l
        self.breadth = b

r = Rectangle(10, 20)
print("Initial area:", r.area)

# Use setter to update dimensions
r.area = (5, 4)
print("Updated area:", r.area)




