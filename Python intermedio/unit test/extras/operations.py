class Operations:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def add(self):
        return self.n1 + self.n2

    def average(self):
        return (self.n1 + self.n2) / 2

    def multiply(self):
        return self.n1 * self.n2


operation1 = Operations(10, 20)
print(f"Result of add: {operation1.add()}")
print(f"Result of average: {operation1.average()}")
print(f"Result of multiply: {operation1.multiply()}")
