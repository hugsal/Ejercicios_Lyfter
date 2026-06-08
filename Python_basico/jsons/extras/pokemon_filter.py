import json


def read_file(path):
    with open(path, "r", encoding='utf-8') as file:
        return json.load(file)


def get_pokemons_by_type(pokemon_type, pokemons):
    filtered_list = []
    for pokemon in pokemons:
        if pokemon["type"] == pokemon_type:
            filtered_list.append(pokemon)

    return filtered_list


def show_info(pokemons_list):
    if not pokemons_list:
        print("No existen pokemnes con de ese tipo")
        return
    
    print("Los pokemos que existen de ese tipo son: ")
    for pokemon in pokemons_list:
        print(pokemon["name"])


def main():
    pokemons = read_file('pokemon.json')
    pokemon_type = input("Ingrese el tipo de pokemon desea buscar(agua,electrico,fuego,etc): ").capitalize()
    filtered_pokemons = get_pokemons_by_type(pokemon_type, pokemons)
    show_info(filtered_pokemons)

main()