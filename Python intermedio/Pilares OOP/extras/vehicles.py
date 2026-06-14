class Vehicle:
    def __init__(self, brand, year):
        self._brand = brand
        self._year = year

    def get_info():
        print(f"{self._brand} ({self._year})")


class Car(Vehicle):
    def __init__(self, brand, year, doors):
        self._doors = doors
        super().__init__(brand, year)

    def get_info(self):
        print(f"{self._brand} ({self._year}) - {self._doors} doors")


class Motorcycle(Vehicle):
    def __init__(self, brand, year, type_motorcycle):
        self._type = type_motorcycle
        super().__init__(brand, year)

    def get_info(self):
        print(f"{self._brand} ({self._year}) - Tipo: {self._type}")


car1 = Car("Honda", 2008, 2)
motorcycle1 = Motorcycle("Ducati", 2020, "sport")

car1.get_info()
motorcycle1.get_info()
