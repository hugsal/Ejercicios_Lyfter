def get_name():
    input_name = input("Ingrese su nombre: ")
    if input_name.isdigit():
        raise ValueError("El nombre no puede ser un número")
    return input_name


def get_age():
    input_age = input("Ingrese su edad: ")
    try:
        age = int(input_age)
        if age < 1: 
            raise ValueError
        return age
    except ValueError:
        raise ValueError("Número no valido")


def main():
    try:
        name = get_name()
        age = get_age()
        print(f"Hola {name}, su edad es {age}")
    except ValueError as ex:
        print(ex)


main()