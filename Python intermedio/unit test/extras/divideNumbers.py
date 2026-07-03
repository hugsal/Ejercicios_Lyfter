def divide(number1, number2):
    if number2 == 0:
        raise ValueError("No se puede dividir por cero")
    return number1 / number2


def main():
    number1 = 10
    number2 = 5

    print(divide(number1, number2))


if __name__ == "__main__":
    main()
