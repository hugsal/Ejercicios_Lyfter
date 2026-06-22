def read_lines(path):
    with open(path, "r") as f:
        return f.readlines()


def main():
    nombreArchivo = input("Ingrese el nombre del archivo: ")
    print(read_lines(nombreArchivo))


if __name__ == "__main__":
    main()
