def manual_add(number):  # O(n)
    result = 0  # O(1)
    for i in range(1, number + 1):  # O(n)
        result += i  # O(1)
    return result  # O(1)


def add_formula(number):  # O(1)
    return number * (number + 1) // 2  # O(1)


def main():
    number = 100
    print(manual_add(number))
    print(add_formula(number))


main()

# ¿Cuál es la complejidad de cada versión?
# manual_add es O(n)
# add_formula es O(1)

# ¿Qué versión usaría si number = 1 000 000 000? ¿Por qué?
# Usaria add_formula porque es O(1) y es mas rapida.
