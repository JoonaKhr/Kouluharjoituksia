class IOString():
    def __init__(self):
        self.s = ""

    def get_string(self):
        self.s = input()

    def print_string(self):
        print(self.s.capitalize())

olio = IOString()
olio.get_string()
olio.print_string()