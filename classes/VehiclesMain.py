from Vehicles import ElectricCar
from Vehicles import Car

tesla = ElectricCar("Tesla", "Model X", 2000)
mauto = Car("Mauto", "Joo", 1044)

print(tesla.battery.get_range())
tesla.battery.upgrade_battery()
print(tesla.battery.get_range())

""" 
print(Car.__dict__)
__weakref__ list of weak references to the object
__dict__ on "magic metodi", joka printtaa luokan kaikki metodit
print(isinstance(tesla, Car)) #1.parametri on olio, ja funktio
                              # testaa onko 1.parametri instanssi
                              2. parametrista
"""