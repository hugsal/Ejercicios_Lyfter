def read_file(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            return lines
    except FileNotFoundError as error:
        raise error


def write_file(content, path):
    with open(path, 'w', encoding='utf-8') as file:
        file.write(content)


def format_content (content):
    clean_content = clean_file_lines(content)
    
    return ' '.join(clean_content)


def clean_file_lines(content):
    clean_list = []
    for record in content:
        clean_list.append(record.strip())
    
    return clean_list
    

def main():
    try:
        content = read_file("list.txt")
        format_text = format_content(content)
        write_file(format_text, "singleLine.txt")
    except FileNotFoundError as error:
        print(error)


main()