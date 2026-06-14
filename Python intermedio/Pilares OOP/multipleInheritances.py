class Flyer:
    def __init__(self):
        self.altitude = 0

    def takeoff(self):
        self.altitude = 10
        print(f"Takeoff. Current altitude: {self.altitude} meters.")

    def land(self):
        self.altitude = 0
        print("Landing. Back on the ground.")


class Attacker:
    def __init__(self):
        self.attack_points = 25

    def attack(self):
        print(f"Attack executed! Damage caused: {self.attack_points} HP.")


class Character:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"I am the character: {self.name}")


class Dragon(Character, Flyer, Attacker):
    def __init__(self, name):
        Character.__init__(self, name)
        Flyer.__init__(self)
        Attacker.__init__(self)


dragon = Dragon("Charizard")

dragon.introduce()
dragon.takeoff()
dragon.attack()
dragon.land()
