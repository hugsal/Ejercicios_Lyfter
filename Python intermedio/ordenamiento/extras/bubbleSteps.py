def bubble_sort_steps(unordered_list):
    new_list = unordered_list.copy()
    iterations = 0
    changes = 0
    for iteration in range(0, len(new_list) - 1):
        has_changes = False
        for index in range(0, len(new_list) - iteration - 1):
            current = new_list[index]
            next = new_list[index + 1]
            if current > next:
                new_list[index] = next
                new_list[index + 1] = current
                has_changes = True
                changes += 1

        iterations += 1
        if not has_changes:
            break

    return {"new_list": new_list, "iterations": iterations, "changes": changes}


def main():
    # my_list = [9, 34, 12, 6, -1, 23, 10, 1]
    my_list = [1, 2, 9, 4, 5, 7]
    results = bubble_sort_steps(my_list)
    print(f"Lista ordenada: {results.get("new_list")}")
    print(f"Iteraciones: {results.get("iterations")}")
    print(f"Cambios: {results.get("changes")}")


main()
