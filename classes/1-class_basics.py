""" 
Olio-ohjelmointi
1 - Luokkien perusteet

Miksi käyttää luokkia
- data ja funktiot voidaan ryhmitellä
- Luokkia voidan uudelleenkäyttää
- Luokkia voi periä (subclasses)

Luokkien funktioita sanotaan metodeiksi
Luokkien muuttujia(variables) sanotaan attribuuteiksi
"""

class Employee:

    num_of_employees = 0
    raise_amount = 1.04 # Luokan muuttuja eli class variable

    def __init__(self, _name, _surname, _salary): # Ns. konstruktori
        self.name = _name
        self.surname = _surname
        self.salary = _salary
        self.email = _name+"."+_surname+"@company.org"
        Employee.num_of_employees += 1
    
    def fullname(self):
        return ('{} {}'.format(self.name, self.surname))

print(Employee.num_of_employees)
emp1 = Employee('Pekka', 'Kovajalka', 1999) #self välittyy automaattisesti
emp2 = Employee('Pertti', 'Jalokarva', 12525612)
print(Employee.num_of_employees)
print(emp1.name, emp2.name, emp2.surname, emp2.salary, emp2.fullname(), emp2.email)


class Restaurant:
    def __init__(self, _restaurant_name, _cuisine_type):
        self.restaurant_name = _restaurant_name
        self.cuisine_type = _cuisine_type
    
    def describe_restaurant(self):
        return ('Restaurant name: {} : Cuisine type: {}'.format(self.restaurant_name, self.cuisine_type))

restaurant = Restaurant('Noodle bar', 'Japanese')
print(restaurant.restaurant_name)
print(restaurant.describe_restaurant())

restaurant2 = Restaurant('Breastaurant', 'Space Dandy')
print(restaurant2.describe_restaurant())
restaurant3 = Restaurant('Puhvelirafla', 'American')
print(restaurant3.describe_restaurant())

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    def describe(self):
        return ('Brand: {}, Model: {}, Year: {}'.format(self.brand, self.model, self.year))


c = Car('Saab', '900', 1978)

print(c.describe())

a = Car('Audi', 'Joo', 1941)

print(a.describe())