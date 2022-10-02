class Vehicle:
    def __init__(self, tank_volume, tank_level, consumption_per_100km) -> None:
        self.tank_volume = tank_volume
        self.tank_level = tank_level
        self.consumption_per_100km = consumption_per_100km

    def get(self, obj, to_fill):
       get = obj.give(to_fill)
       self.tank_level += get

    def drive(self, distance):
        self.tank_level -= distance/100 * self.consumption_per_100km


class GasDistributer:
    def __init__(self, store_volume, store_level) -> None:
        self.store_volume = store_volume
        self.store_level = store_level

    def get(self, obj, to_fill):
        get = obj.give(to_fill)
        self.store_level += get

    def give(self, to_give):
        given = to_give if self.store_level >= to_give else self.store_level
        self.store_level -= given
        return given


class MobileGasDistributer(GasDistributer, Vehicle):
    def __init__(self, store_volume, store_level, tank_volume, tank_level, consumption_per_100km) -> None:
       GasDistributer.__init__(self, store_volume, store_level)
       Vehicle.__init__(self, tank_volume, tank_level, consumption_per_100km)

    def get(self, obj, to_fill, target):
        Vehicle.get(self, obj, to_fill) if target == "tank" else GasDistributer.get(self, obj, to_fill)

my_car = Vehicle(25, 2, 7.3)
my_favorite_gas_station = GasDistributer(12600, 4839)
petrol_lorry = MobileGasDistributer(2150, 2150, 250, 176, 14.9)


my_car.drive(58)    # to gas_station
my_car.get(my_favorite_gas_station, my_car.tank_volume-my_car.tank_level)
