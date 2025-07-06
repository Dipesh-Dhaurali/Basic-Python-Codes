"""
cont...
"""

class Car:
    color="blue"
    @staticmethod
    def start():
        print("car started...")

    @staticmethod
    def stop():
        print("car stopped...")

class Van(Car):
    def __init__(self,name):
        self.name=name
    def show(self):
        print(self.name)


v=Van('camping van')
v.show()       #child class can call its own method
v.start()      #child class can call parent class
v.stop()       #child class can call parent class
print(v.color) #child class can access parent class variable

c=Car()
c.start()       # parent class can access its own method
c.stop()        # parent class can access its own method
####c.show()    # parent class cannot access child class
