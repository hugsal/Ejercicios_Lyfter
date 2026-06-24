def print_all_pairs(my_dict):
    for key1 in my_dict:  # O(n)
        for key2 in my_dict:  # O(n)
            print(f"{key1}-{key2}")  # O(1)


def main():
    my_dict = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
    print_all_pairs(my_dict)


main()

# ¿Cuál es la complejidad temporal?
# O(n^2)

# ¿Cuanto dura si hay 1 millón de claves?
# 1 billón de iteraciones
