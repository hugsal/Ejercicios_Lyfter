def get_primo_numbers(list_numbers):
    primos = []
    for record in list_numbers:
        if is_primo(record):
            primos.append(record)
    return primos


def is_primo(num):
    if num == 1:
        return False
    for n in range(2, num):
        if num % n == 0:
            return False
    return True


def main():
    my_list = [1, 2, 4, 6, 7, 13, 9, 67]
    print(get_primo_numbers(my_list))


main()