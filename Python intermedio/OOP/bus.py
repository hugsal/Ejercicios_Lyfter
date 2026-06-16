class Person:
    def __init__(self, name):
        self.name = name


class Bus:
    max_passengers = 5

    def __init__(self, people_on_bus=0):
        self.people_on_bus = people_on_bus

    def add_passenger(self, person):
        if self.people_on_bus < Bus.max_passengers:
            self.people_on_bus += 1
            print(f"{person.name} welcome aboard.")
            return
        else:
            print("Bus is full")
            return

    def drop_off_a_passenger(self, person):
        if self.people_on_bus > 0:
            self.people_on_bus -= 1
            print(f"{person.name} has left the bus.")
            return
        else:
            print("Bus is empty")
            return


person1 = Person("hugo")
person2 = Person("mabel")
person3 = Person("lucy")
person4 = Person("camila")
person5 = Person("guadalupe")
person6 = Person("fabiola")

bus1 = Bus()

bus1.add_passenger(person1)
bus1.add_passenger(person2)
bus1.add_passenger(person3)
bus1.add_passenger(person4)
bus1.add_passenger(person5)
bus1.add_passenger(person6)

bus1.drop_off_a_passenger(person1)
bus1.drop_off_a_passenger(person2)
bus1.drop_off_a_passenger(person3)
bus1.drop_off_a_passenger(person4)
bus1.drop_off_a_passenger(person5)
bus1.drop_off_a_passenger(person6)
