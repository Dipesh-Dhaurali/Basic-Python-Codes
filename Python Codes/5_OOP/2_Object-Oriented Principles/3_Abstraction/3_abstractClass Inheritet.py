"""
cont... telusko
"""

from abc import ABC, abstractmethod

class Computer(ABC):
    @abstractmethod
    def Process(self):
        pass

#to inherit it
class Laptop(Computer):
    def Process(self):
        print("Its working...")



c=Laptop()
c.Process()


# the same method name is required
# to need one method to implement inheritance