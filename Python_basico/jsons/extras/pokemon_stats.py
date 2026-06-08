import json


def read_file(path):
    with open(path, "r", encoding='utf-8') as file:
        return json.load(file)


def show_info(pokemon_list):
    for record in pokemon_list:
        print(f"Nombre: {record.get("name")}")
        stats = record.get("stats")
        print(f"Ataque: {stats.get("attack")}")
        print(f"Defensa: {stats.get("defense")}")
        print(f"Velocidad: {stats.get("speed")}\n")


def main():
    pokemons = read_file('pokemon.json')
    show_info(pokemons)


main()