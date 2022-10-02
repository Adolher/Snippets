from abc import ABC, abstractmethod     # ABC -> Abstract Base Class

class Vehicle(ABC):
    def __init__(self, designation) -> None:
        self.designation = designation

    @abstractmethod
    def move(self):
        pass

class LandVehicle(Vehicle):
    def move(self):
        print(f"{self.designation} is moving.")

car = LandVehicle("Car")
car.move()