def validate_list(my_list):
    if not my_list:
        raise ValueError("Error: La lista está vacía")

    for record in my_list:
        if not isinstance(record, (int, float)):
            raise ValueError("Error: La lista contiene elementos no numéricos")


def bubble_sort(unordered_list):
    new_list = unordered_list.copy()
    validate_list(new_list)
    for iteration in range(0, len(new_list) - 1):
        has_Changes = False
        for index in range(0, len(new_list) - iteration - 1):
            current = new_list[index]
            next = new_list[index + 1]
            if current > next:
                new_list[index] = next
                new_list[index + 1] = current
                has_Changes = True

        if not has_Changes:
            break

    return new_list


def main():
    try:
        # my_list = [9, 34, 12, 6, -1, 23, 10, 1]
        # my_list = [4, 3, 2, 1, 3.5, -5, 8.2]
        # my_list = []
        my_list = [1, "hola", 3, 4, 5]
        order_list = bubble_sort(my_list)
        print(order_list)
    except ValueError as ex:
        print(ex)


main()
