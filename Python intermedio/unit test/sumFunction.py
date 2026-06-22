def sum_list_elements(list):
    total = 0
    for item in list:
        total = total + item
    
    return total


def main():
    # my_list = [1, 4, 6, 7, 13, 9, 67]
    my_list = [10, 20, 30, 40, 50]
    print(sum_list_elements(my_list))


main()