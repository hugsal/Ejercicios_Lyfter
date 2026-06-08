def get_list():
    list_input = []
    print("ingrese un grupo de string para convertir a entero")
    for i in range(5):
        list_input.append(input())
    
    return list_input


def convert_to_int(input_list):
    converted_list = []
    for record in input_list:
        try:
            result = int(record)
            converted_list.append(f"'{record}' convertido a {result}")
        except ValueError:
            converted_list.append(f"No se pudo convertir el elemento: {record}")

    return converted_list


def main():
    my_list = get_list()
    result = convert_to_int(my_list)
    print("\nResultado:")
    for record in result:
        print(record)


main()