def repeat_twice(func):
    def wrapper(parameter):
        for i in range(2):
            func(parameter)

    return wrapper


@repeat_twice
def greeting(name):
    print(f"Hola, {name}")


def main():
    name = input("Enter a name: ")
    greeting(name)


main()
