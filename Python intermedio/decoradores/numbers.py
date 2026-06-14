def int_validator(func):
    def wrapper(*args):
        for arg in args:
            if not isinstance(arg, int):
                raise ValueError(f"{arg} is not an int")
        func(args)

    return wrapper


@int_validator
def numbers_chain(*args):
    print(args)


try:
    numbers_chain(
        1,
        2,
        3,
        4,
        5,
        6,
        "hola",
        343,
        6,
        7,
        8,
    )
except ValueError as ex:
    print(ex)
