def bubble_sort(unordered_list):
    new_list = unordered_list.copy()
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
    my_list = [9, 34, 12, 6, -1, 23, 10, 1]
    # my_list = [1, 2, 4, 5, 7]
    order_list = bubble_sort(my_list)
    print(order_list)


main()
