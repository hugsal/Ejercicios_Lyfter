from abc import ABC, abstractmethod


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
        perimeter = 2 * 3.1416 * self.radius
        print(f"The perimeter of the circle is {perimeter}")
        return

    def calculate_area(self):
        area = 3.14159 * self.radius**2
        print(f"The area of the circle is {area}")
        return


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_perimeter(self):
        perimeter = 2 * (self.length + self.width)
        print(f"The perimeter of the rectangle is {perimeter}")
        return

    def calculate_area(self):
        area = self.length * self.width
        print(f"The area of the rectangle is {area}")
        return


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_perimeter(self):
        perimeter = 4 * self.side
        print(f"The perimeter of the square is {perimeter}")
        return

    def calculate_area(self):
        area = self.side**2
        print(f"The area of the square is {area}")
        return


circle = Circle(5)
rectangle = Rectangle(5, 10)
square = Square(5)

circle.calculate_perimeter()
circle.calculate_area()

rectangle.calculate_perimeter()
rectangle.calculate_area()

square.calculate_perimeter()
square.calculate_area()
