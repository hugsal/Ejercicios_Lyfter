def get_list_from_string(sentence):
    return sentence.split("-")


def get_string_from_list(list):
    return "-".join(list)


def main():
    my_string = "python-variable-funcion-computadora-monitor"
    my_list = get_list_from_string(my_string)
    my_list.sort()
    print(get_string_from_list(my_list))


main()