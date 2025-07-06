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

class Programmer:
    def work(self,comp):
        print("Solving bugs")
        comp.Process()

c=Laptop()

p1=Programmer()
p1.work(c)
