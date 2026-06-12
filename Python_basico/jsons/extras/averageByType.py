import json


def read_file(path):
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def get_pokemons_by_type(pokemons):
    grouped_pokemons = {}
    for pokemon in pokemons:
        pokemon_type = pokemon.get("type")
        target_type = grouped_pokemons.get(pokemon_type)
        if target_type != None:
            grouped_pokemons[pokemon_type].append(pokemon)
        else:
            grouped_pokemons[pokemon_type] = [pokemon]

    return grouped_pokemons


def show_info(pokemons_list):
    for pokemon_type, pokemons in pokemons_list.items():
        total_level = 0
        for pokemon in pokemons:
            total_level += pokemon.get("level")

        average_level = total_level / len(pokemons)
        print(f"Tipo {pokemon_type} => Promedio de nivel: {average_level}")


def main():
    pokemons = read_file("pokemon.json")
    grouped_pokemons = get_pokemons_by_type(pokemons)
    show_info(grouped_pokemons)


main()
