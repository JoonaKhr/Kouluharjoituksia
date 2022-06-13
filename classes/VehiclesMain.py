from Vehicles import ElectricCar
from Vehicles import Car
from Vehicles import Cycle

tesla = ElectricCar("Tesla", "Model X", 2000, 4, "electric")
mauto = Car("Mauto", "Joo", 1044, 4, "gas")
bicycle = Cycle("Polku", "Pyörä", 1452, 2, "none")

print(bicycle.check_engine_type())
print(bicycle.fill_tank())

print(tesla.get_name())
print(tesla.check_engine_type())
print(tesla.fill_tank())


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