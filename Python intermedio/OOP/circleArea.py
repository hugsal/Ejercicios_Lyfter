class Circle:
    pi = 3.1416

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.pi * self.radius**2


circle = Circle(5)
print(circle.area())
