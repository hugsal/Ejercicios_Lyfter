def get_total_upper_cases(sentence):
    upper = 0
    for character in sentence:
        if character.isupper():
            upper += 1

    return upper


def get_total_lower_cases(sentence):
    lower = 0
    for character in sentence:
        if character.islower():
            lower += 1

    return lower


def main():
    # my_string = "I love Nación Sushi"
    my_string = "My Name is Hugo SALAZAR"
    upper = get_total_upper_cases(my_string)
    lower = get_total_lower_cases(my_string)

    print(f"There’s {upper} upper cases and {lower} lower cases")


main()