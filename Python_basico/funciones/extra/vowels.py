def get_sentence():
    return input("Ingrese una frase: ")


def is_vowel(character):
    vowels = "aeiou"
    if character in vowels:
        return True
    
    return False


def get_vowels_counter(sentence):
    total = 0
    for char in sentence:
        if is_vowel(char):
            total += 1

    return total


def main():
    my_sentence = get_sentence()
    print(get_vowels_counter(my_sentence))


main()