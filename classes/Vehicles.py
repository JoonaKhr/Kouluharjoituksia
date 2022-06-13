class Vehicle():
    def __init__(self, brand, model, year, wheels, engine):
        self.brand = brand
        self.model = model
        self.year = year
        self.wheels = wheels
        self.engine = engine

    def fill_tank(self):
        if self.engine == "gas":
            return "Filling gas"
        elif self.engine == "electric":
            return "You should either recharge or upgrade your battery"
        else:
            return "Not an engine or a conventional one"
    
    def check_engine_type(self):
        return f"Your vehicles engine type is {self.engine}"

    def get_name(self):
        return f"{self.brand} {self.model} {self.year}"

class Cycle(Vehicle):
    def __init__(self, brand, model, year, wheels, engine):
        super().__init__(brand, model, year, wheels, engine)
        if self.engine == "electric":
            self.battery = Battery()

class Car(Vehicle):
    def __init__(self, brand, model, year, wheels, engine):
        super().__init__(brand, model, year, wheels, engine)
        
    

class ElectricCar(Car):
    def __init__(self, brand, model, year, wheels, engine):
        super().__init__(brand, model, year, wheels, engine)
        self.battery = Battery()

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
        return f"Car can go: {car_range} kilometers"

    def upgrade_battery(self):
        if self.battery != 100:
            self.battery = 100


class Bus(Car):
    def __init__(self, brand, model, year, wheels, engine):
        super().__init__(brand, model, year, wheels, engine)
        if engine == "electric":
            self.battery = Battery()
    
    def seating_capacity(self, capacity=50):
        return f"Seats {capacity}"