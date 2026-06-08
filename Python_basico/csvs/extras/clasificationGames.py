import csv

RANKING_VALUES = ["RP", "T", "E10+", "E", "M 17+", "A0"]


def read_file(path):
    my_list = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            read =  csv.DictReader(file)
            for item in read:
                my_list.append(item)
        
        return my_list
    except FileNotFoundError as error:
        raise error


def get_ranking():
    ranking = input("Ingresa una clasificacion ESRB: ")
    if ranking not in RANKING_VALUES:
        raise ValueError("Ingrese una clasificacion valida")

    return ranking


def get_data_by_ranking(data, ranking):
    filtered_by_ranking = []
    for record in data:
        game_ranking = record.get("ranking")
        if ranking == game_ranking:
            filtered_by_ranking.append(record)

    return filtered_by_ranking


def show_info(videogames):
    if not videogames:
        print("No existen videojuegos con esa clasificacion")
        return

    for index, item in enumerate(videogames):
        print(f"Videojuego: {index + 1}")
        print(f"Nombre: {item["name"]}")
        print(f"Generp: {item["gender"]}")
        print(f"Desarrollador: {item["developer"]}")
        print(f"Clasificasion: {item["ranking"]}\n")


def main():
    try:
        csv_content = read_file("favoritesVideogames.csv")
        ranking = get_ranking()
        videogames= get_data_by_ranking(csv_content, ranking)
        show_info(videogames)
    except Exception as ex:
        print(ex)


main()