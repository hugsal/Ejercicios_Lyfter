def get_number(operation = 0):
    try:
        input_number = int(input("Ingresa un numero positivo: "))
        if input_number < 0:
            raise ValueError("El numero es negativo")
        if operation == 4 and input_number == 0:
            raise ValueError("No se puede dividir entre cero")
        return input_number
    except ValueError as ex:
        print(f"Error [ValueError]: {ex}")
        raise ex


def get_operator():
    try:
        operation_input = int(input(
"""Selecciona una operacion:
1. Suma
2. Resta
3. Multiplicación
4. División  
5. Borrar resultado \n"""))
        if operation_input < 1 or operation_input > 5:
            raise ValueError("Opcion no valida")
        return operation_input
    except ValueError as ex:
        print(f"Error [ValueError]: {ex}")
        raise ex


def get_result(number_1, number_2, operation):
    match operation:
        case 1:
            return number_1 + number_2
        case 2:
            return number_1 - number_2
        case 3:
            return number_1 * number_2
        case _:
            return number_1 / number_2


def main():
    try:
        actual_value = get_number()
        while True :
            operation = get_operator()
            if operation == 5:
                actual_value = get_number()
                operation = get_operator()
            second_number = get_number(operation)
            actual_value = get_result(actual_value, second_number, operation)
            print(f"Resultado: {actual_value}")
    except ValueError as ex:
        print(ex)


main()