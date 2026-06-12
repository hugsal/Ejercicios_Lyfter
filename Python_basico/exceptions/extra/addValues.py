def get_list():
    list_input = []
    print("ingrese un grupo de string para convertir a float")
    for i in range(5):
        list_input.append(input())
    
    return list_input


def get_total(input_list):
    total = 0
    for record in input_list:
        try:
            result = float(record)
            total += result
            print(f"{result} sumado correctamente")
        except ValueError:
            print(f"Elemento inválido: {record}")

    return total


def main():
    my_list = get_list()
    total = get_total(my_list)
    print(f"Total de la suma: {total}")


main()