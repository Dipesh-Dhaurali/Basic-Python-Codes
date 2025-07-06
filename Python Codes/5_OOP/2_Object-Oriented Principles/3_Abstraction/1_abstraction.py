"""
shdarhda cont...(47:32)

"""
# hiding the unnecessary implementation details of the class
# and only showing the essential features to the users.

class Car:
    def __init__(self):
        self.acc=False
        self.brk=False
        self.clutch=False

    def start_car(self):
        self.clutch=True
        self.acc=True
        print("Car started...")

c1=Car()
c1.start_car()


