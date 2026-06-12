def read_file(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            return lines
    except FileNotFoundError as error:
        raise error


def write_file(content, path):
    with open(path, 'w', encoding='utf-8') as file:
        file.writelines(content)


def upper_file_lines(content):
    upper_list = []
    for record in content:
        clean_line = record.strip().upper()
        upper_list.append(f"{clean_line}\n")
    
    return upper_list
    

def main():
    try:
        content = read_file("upper.txt")
        format_text = upper_file_lines(content)
        write_file(format_text, "allUpper.txt")
    except FileNotFoundError as error:
        print(error)


main()