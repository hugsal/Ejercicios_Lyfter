import csv


def read_file(path):
    my_list = []
    with open(path, "r", newline='', encoding='utf-8') as file:
        content = csv.reader(file)
        for record in content:
            my_list.append(record)
    
    return my_list


def show_info(content):
    header = content[0]
    for record_index in range(1, len(content)):
        print(f"Videogame: {record_index}")
        for row_index in range(len(header)):
            print(f"{header[row_index]}: {content[record_index][row_index]}")
        print("")


def main():
    content = read_file("favoritesVideogames.csv")
    show_info(content)


main()