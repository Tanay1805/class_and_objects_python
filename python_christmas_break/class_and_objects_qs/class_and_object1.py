from datetime import date, datetime

class Person:
    l = []

    def __init__(self, name, country, dob):
        self.name = name
        self.country = country
        self.dob = datetime.strptime(dob, "%d/%m/%Y").date()
        self.calculate_age()
        self.create_list()

    def calculate_age(self):
        today = date.today()
        self.age = today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))

    def create_list(self):
        self.l = [self.name, self.country, str(self.dob), str(self.age)]

name = input("Enter your name: ")
country = input("Enter your country: ")
dob = input("Enter your dob (dd/mm/yyyy): ")

p = Person(name, country, dob)

print(p.l)
