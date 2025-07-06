"""
Telusko(Abstract Class and Abstract Method in Python)
+
https://youtu.be/UDmJGvM-OUw
"""
from abc import ABC, abstractmethod  #need this

class Computer(ABC):                  #point to note (ABC) required
    @abstractmethod
    def Process(self):
        pass

c=Computer()
c.Process()  #it will through error because Abstract class cannot be created an object



"""
note

1) An abstract method in Python is a method that is declared in a 
base class but does not have any implementation. 
It acts as a blueprint and must be overridden by any 
subclass that inherits from the abstract base class.

2) any method that has declaration but not any definition 
inside class is called abstract method

3) To create an abstract method in Python, 
you use the abc module, 
which stands for Abstract Base Classes.

4) The class which have abstract method is called abstract classes

5) we cannot create an object of abstract classes
"""