def linear_search(my_list, target):  # O(n)
    for item in my_list:  # O(n)
        if item == target:  # O(1)
            return True  # O(1)
    return False  # O(1)


def binary_search(my_list, target):  # O(log n)
    low = 0  # O(1)
    high = len(my_list) - 1  # O(1)
    while low <= high:  # O(log n)
        mid = (low + high) // 2  # O(1)
        if my_list[mid] == target:  # O(1)
            return True  # O(1)
        elif my_list[mid] < target:  # O(1)
            low = mid + 1  # O(1)
        else:  # O(1)
            high = mid - 1  # O(1)
    return False  # O(1)


def main():
    # my_list = [1, 2, 3, 11, 4, 5, 6, 7, 8, 9, 10]
    my_list = [1, 200, 343, 134, 345, 364, 667, 484, 911, 11]
    target = 11
    print(linear_search(my_list, target))
    print(binary_search(my_list, target))


main()

# ¿Cuál es la complejidad de cada algoritmo?
# linear_search es O(n)
# binary_search es O(log n)

# ¿En qué condiciones conviene usar cada uno?
# linear_search conviene usarlo cuando la lista no esta ordenada o cuando la lista es muy pequena.
# binary_search conviene usarlo cuando la lista esta ordenada y es grande.

# ¿Qué pasa si la lista no está ordenada?
# binary_search arroja resultados erroneos (falsos negativos).
