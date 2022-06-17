class Auto():
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    @classmethod
    def from_string(cls, string: str):
        arvo = string.split("-")
        return cls(arvo[0], arvo[1], int(arvo[2]))

    def __str__(self):
        return f"""
                Brand: {self.brand}
                Model: {self.model}
                Year: {self.year}
                """

audi = Auto.from_string("Audi-A4-2000")

print(audi)