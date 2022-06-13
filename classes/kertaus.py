class Vehicle:
    wheels = 4
    def __init__(self, _max_speed, _mileage=0):
        self.max_speed = _max_speed
        self.mileage = _mileage


v = Vehicle(100, 10000)
print(v.max_speed, ' ', v.mileage)