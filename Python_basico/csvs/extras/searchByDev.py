import csv


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


def get_data_by_developer(data, developer):
    filtered_by_developer = []
    for record in data:
        game_developer = record.get("developer")
        if developer == game_developer:
            filtered_by_developer.append(record)

    return filtered_by_developer


def show_info(videogames, developer):
    if not videogames:
        print(f"No existen videojuegos desarrollados por {developer}")
        return

    print(f"Videojuegos desarrollados por: {developer}")
    for record in videogames:
        print(f"- {record["name"]} (Clasificacion: {record["ranking"]}, Genero: {record["gender"]})")
        


def main():
    try:
        csv_content = read_file("favoritesVideogames.csv")
        developer = input("Ingresa el nombre del desarrollador de videojuegos: ")
        videogames= get_data_by_developer(csv_content, developer)
        show_info(videogames, developer)
    except FileNotFoundError as ex:
        print(ex)


main()