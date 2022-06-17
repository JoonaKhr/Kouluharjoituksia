from this import d


class Auto():
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    @classmethod
    def from_string(cls, string: str):
        brand, model, year = string.split("-")
        return cls(brand, model, year)

    def __str__(self):
        return f"""
                Brand: {self.brand}
                Model: {self.model}
                Year: {self.year}
                """

audi = Auto.from_string("Audi-A4-2000")

print(audi)