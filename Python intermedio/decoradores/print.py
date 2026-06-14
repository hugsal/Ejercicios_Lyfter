def printer(func):
    def wrapper(*args):
        print(f"the numbers to be added are: {args}")
        result = func(*args)
        print(result)

    return wrapper


@printer
def add(number1, number2):
    return f"the sum is: {number1 + number2}"


add(5, 6)
