from .Car import Car

class ElecticCar(Car):
    def __init__(self, brand, milage_km, range):
        super().__init__(brand, milage_km)
        self.range=range