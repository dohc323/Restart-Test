from .Car import Car

class ICECar(Car):
    def __init__(self, brand, milage_km, fuel_consumption, fuel_level):
        super().__init__(brand, milage_km)
        self.fuel_consumption=fuel_consumption
        self.fuel_level=fuel_level