class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def validate_values(self):
        if self.length <= 0 or self.width <= 0:
            raise ValueError(
                "Existe un valor negativo, los valores deben ser positivos"
            )

    def area(self):
        self.validate_values()
        return self.length * self.width

    def perimeter(self):
        self.validate_values()
        return 2 * (self.length + self.width)


try:
    length = int(input("Ingrese la altura: "))
    width = int(input("Ingrese el ancho: "))
    rectangle = Rectangle(length, width)
    print(rectangle.area())
    print(rectangle.perimeter())
except ValueError as ex:
    print(ex)
