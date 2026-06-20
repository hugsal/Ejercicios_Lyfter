from datetime import datetime


def log_call(func):
    def wrapper(*args):
        number1 = args[0]
        number2 = args[1]
        print(
            f"Func: {func.__name__} - args: {", ".join(map(str, args))} - [{datetime.today()}] - Resultado {number1 * number2}"
        )

        func(*args)

    return wrapper


def validate_numbers(func):
    def wrapper(*args):
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise ValueError("The values is not int")

        func(*args)

    return wrapper


@validate_numbers
@log_call
def multiply(number1, number2):
    print(f"Resultado {number1 * number2}")


def main():
    try:
        multiply(4, 5.5)
    except ValueError as ex:
        print(ex)


main()
