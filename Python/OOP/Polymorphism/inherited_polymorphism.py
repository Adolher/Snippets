class Vehicle:
    def __init__(self, speed) -> None:
        self.speed = speed
    def show_speed(self):
        print(f"{self.__class__} can drive {self.speed}")
    
class LandVehicle(Vehicle):
    def __init__(self, speed, wheels) -> None:
        Vehicle.__init__(self, speed)
        self.wheels = wheels

class WaterVehicle(Vehicle):
    def __init__(self, speed, water_displacement) -> None:
        Vehicle.__init__(self, speed)
        self.water_displacement = water_displacement

class AmphibiousVehicle(LandVehicle, WaterVehicle):
    def __init__(self, speed, wheels, water_displacement) -> None:
        LandVehicle.__init__(self, speed, wheels)
        WaterVehicle.__init__(self, speed, water_displacement)

lv = LandVehicle(130, 4)
wv = WaterVehicle(23, 17)
av = AmphibiousVehicle(90, 4, 20)

def func(obj):
    obj.show_speed()

func(lv)
func(wv)
func(av)