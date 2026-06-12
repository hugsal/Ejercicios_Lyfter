def get_list(limit):
    my_list = []
    for i in range(limit):
        word = input("Ingrese un palabra: ")
        my_list.append(word)

    return my_list


def get_minimum_character():
    return int(input("Ingrese el numero de letras minimas en la palabra: "))


def get_filtered_list(input_list, limit):
    filtered_list = []
    for record in input_list:
        if len(record) > limit:
            filtered_list.append(record)

    return filtered_list


def main():
    LIMIT_OF_WORDS = 5
    my_list = get_list(LIMIT_OF_WORDS)
    minimum_character = get_minimum_character()
    filtered_list = get_filtered_list(my_list, minimum_character)

    print(filtered_list)


main()