from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def calculate_perimeter(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_perimeter(self):
        perimeter = 2 * math.pi * self.radius
        return perimeter

    def calculate_area(self):
        area = math.pi * self.radius**2
        return area


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_perimeter(self):
        perimeter = 2 * (self.length + self.width)
        return perimeter

    def calculate_area(self):
        area = self.length * self.width
        return area


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_perimeter(self):
        perimeter = 4 * self.side
        return perimeter

    def calculate_area(self):
        area = self.side**2
        return area


circle = Circle(5)
rectangle = Rectangle(5, 10)
square = Square(5)

print(circle.calculate_perimeter())
print(circle.calculate_area())

print(rectangle.calculate_perimeter())
print(rectangle.calculate_area())

print(square.calculate_perimeter())
print(square.calculate_area())
