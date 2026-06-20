from datetime import date


class User:
    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth

    @property
    def age(self):
        today = date.today()
        return today.year - self.date_of_birth.year


def is_adult(func):
    def wrapper(*args):
        user = None
        for arg in args:
            if isinstance(arg, User):
                user = arg
                break

        if user.age < 18:
            raise PermissionError("You're not an adult")

        func(*args)

    return wrapper


@is_adult
def enter_casino(user):
    print("Welcome")


user1 = User(date(1988, 9, 10))
user2 = User(date(2015, 4, 21))

try:
    enter_casino(user1)
    enter_casino(user2)
except Exception as ex:
    print(ex)
