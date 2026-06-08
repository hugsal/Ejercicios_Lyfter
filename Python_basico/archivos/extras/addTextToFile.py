def write_file(path, new_text):
    with open(path, 'a', encoding='utf-8') as file:
        file.write("\n" + new_text)


def main():
    new_text_line = "Bienvenidos al creador de palabras aleatorias en español, con él puedes crear palabras al azar para ejercicios de creatividad, memorización, etc"
    write_file("loremIpsum1.txt", new_text_line)


main()