def read_file(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            return lines
    except FileNotFoundError as error:
        raise error

def get_total_words(content):
    total = 0
    for record in content:
       count = len(record.split(" "))
       total += count

    return total
    

def main():
    try:
        content = read_file("songs.txt")
        total_words = get_total_words(content)
        print(f"Este archivo contiene {total_words} palabras")
    except FileNotFoundError as error:
        print(error)


main()