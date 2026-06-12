def get_sentence():
    return input("Ingrese una frase:")


def get_character():
    return input("Ingrese el carácter que desea buscar:")


def get_character_counter(sentence, character):
    total = 0
    for char in sentence:
        if char ==character:
            total += 1

    return total


def main():
    my_sentence = get_sentence()
    character_to_search = get_character()
    total = get_character_counter(my_sentence, character_to_search)

    print(f"Se ha encontrado {total} veces el carácter")


main()