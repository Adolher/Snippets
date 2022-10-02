class Vehicle:
    def __init__(self, designation) -> None:
        self.designation = designation
    def say(self):
        print(f"They call me {self.designation}")

class Food:
    def __init__(self, designation) -> None:
        self.designation = designation
    def say(self):
        print(f"They call me {self.designation}")

class Furniture:
    def __init__(self, designation) -> None:
        self.designation = designation
    def say(self):
        print(f"They call me {self.designation}")

car = Vehicle("Car")
bread = Food("Bread")
chair = Furniture("Chair")
list = [car, bread, chair]

for x in list:
    x.say()