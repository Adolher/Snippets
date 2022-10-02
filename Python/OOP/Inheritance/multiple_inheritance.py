class Vehicle:
    def __init__(self, speed) -> None:
        self.speed = speed
    
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

amphibious_car = AmphibiousVehicle(15, 4, 30)


d = dir(amphibious_car)
for x in d:
    if not x.startswith("__"):
        print(f'amphibious Car {x} = {eval("amphibious_car."+ x)}')
print()
g = globals().copy()
for x in g:
    if not x.startswith("__") and not x.startswith("d") and not x.startswith("x"):
        print(f"{x}: {g[x]}")
