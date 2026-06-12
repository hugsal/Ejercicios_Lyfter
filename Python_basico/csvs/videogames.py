import csv


def get_videogames_limit():
    limit = input("Cuanto videojuegos deseas almacenar: ")
    try:
        input_number = int(limit)
        if input_number < 0:
            raise ValueError("El numero debe ser mayor a 0")
        return input_number
    except ValueError as ex:
        raise ex


def get_videogames_data(limit):
    videogames = []
    for i in range(1, limit +1):
        game = {}
        print(f"Videojuego {i}")
        game["name"] = input("Ingresa el nombre del juego: ")
        game["gender"] = input("Ingresa el genero del juego: ")
        game["developer"] = input("Ingresa el nombre del desarrollador: ")
        game["rankink"] = input("Clasificacion ESRB del juego: ")
        videogames.append(game)

    return videogames


def write_csv(file_path, data):
    with open(file_path, 'w', encoding='utf-8', newline='') as file:
        headers = data[0].keys()
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)


def main():
    try:
        videogames_limit = get_videogames_limit()
        videogames_dict = get_videogames_data(videogames_limit)
        write_csv("favoritesVideogames.csv", videogames_dict)
    except ValueError as ex:
        print(ex)


main()