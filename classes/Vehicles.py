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
    def fill_gas_tank(self):
        return "It's Electric!!!!!!!"

class Bus(Vehicle):
    def __init__(self):
        super().__init__()
    
    def seating_capacity(self, capacity=50):
        return f"Seats {capacity}"