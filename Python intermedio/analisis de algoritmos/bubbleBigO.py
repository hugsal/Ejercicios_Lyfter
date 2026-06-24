def bubble_sort(unordered_list):
    new_list = unordered_list.copy()  # O(n)
    for iteration in range(0, len(new_list) - 1):  # O(n)
        has_Changes = False  # O(1)
        for index in range(0, len(new_list) - iteration - 1):  # O(n^2)
            current = new_list[index]  # O(1)
            next = new_list[index + 1]  # O(1)
            if current > next:  # O(1)
                new_list[index] = next  # O(1)
                new_list[index + 1] = current  # O(1)
                has_Changes = True  # O(1)

        if not has_Changes:  # O(1)
            break

    return new_list  # O(1)


def main():
    my_list = [9, 34, 12, 6, -1, 23, 10, 1]  # O(1)
    # my_list = [1, 2, 4, 5, 7] # O(1)
    order_list = bubble_sort(my_list)  # O(n^2)
    print(order_list)  # O(1)


main()
