class Vehicle():
    def __init__(self):
        pass

class Car():
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def fill_gas_tank(self):
        return "Filling gas"

    def get_name(self):
        return f"{self.brand} {self.model} {self.year}"

class ElectricCar(Car):
    def __init__(self, brand, model, year):
        super().__init__(brand, model, year)
        self.battery = Battery()
    def fill_gas_tank(self):
        return "It's Electric!!!!!!!"

class Battery:
    def __init__(self, battery_size=75):
        self.battery = battery_size

    def print_battery_info(self):
        return f"This car has {self.battery} kwH battery."
    
    def get_range(self):
        car_range = 0
        if self.battery == 75:
            car_range = 260
        elif self.battery == 100:
            car_range = 315
        return car_range

    def upgrade_battery(self):
        if self.battery != 100:
            self.battery = 100


class Bus(Vehicle):
    def __init__(self):
        super().__init__()
    
    def seating_capacity(self, capacity=50):
        return f"Seats {capacity}"