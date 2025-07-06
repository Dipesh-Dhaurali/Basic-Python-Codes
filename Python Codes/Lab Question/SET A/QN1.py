"""
Implement inheritance with a base class Animal
and a derived class Dog with an
additional method for barking.
"""
class Animal:
    def __init__(self, name):
        self.name = name

    def pet(self):
        print(f"My Dog name is {self.name}")


class Dog(Animal):
    def __init__(self, name, sound):
        super().__init__(name)
        self.sound = sound

    def bark(self):
        print(f"{self.name} can {self.sound}")


d1 = Dog("Lucky", "Bark")
d1.pet()
d1.bark()
