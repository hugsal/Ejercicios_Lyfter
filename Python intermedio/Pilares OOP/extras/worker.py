class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = 0
        self.salary = salary

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        if salary < 0:
            raise ValueError("Salary cannot be negative")
        self.__salary = salary

    def promote(self, percentage):
        self.__salary *= 1 + percentage


employee = Employee("Hugo", 1000)
employee.promote(0.1)
print(employee.name)
print(employee.salary)

try:
    employee2 = Employee("Ana", -100)
except ValueError as ex:
    print(ex)
