class Ohjelmoija():
    bonus = 1.05
    def __init__(self, first, last, salary):
        self.first = first
        self.line = ""
        self.last = last
        self.salary = salary

    def get_email(self):
        return f"{self.first}.{self.last}@firma.fi"

    def apply_bonus(self):
        self.salary = self.salary * self.bonus

    def print_salary_with_bonus(self):
        print(f"Salary with bonus: {self.salary * self.bonus}")

class PythonOhjelmoija(Ohjelmoija):
    bonus = 1.1
    def __init__(self, first, last, salary):
        super().__init__(first, last, salary)

oho = Ohjelmoija("j", "j", 100)
pho = PythonOhjelmoija("A", "A", 100)
print(oho.get_email())
print(pho.get_email())

oho.print_salary_with_bonus()
oho.apply_bonus()
Ohjelmoija.bonus = 1.2
oho.print_salary_with_bonus()
oho.get_String()
oho.print_String()