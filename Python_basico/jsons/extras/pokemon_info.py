import json


def read_file(path):
    with open(path, "r", encoding='utf-8') as file:
        return json.load(file)


def show_info(pokemon_list):
    for record in pokemon_list:
        print(f"Name: {record["name"]}")
        print(f"Type: {record["type"]}")
        print(f"Level: {record["level"]}")
        print(f"Skills: {record["skills"]}\n")


def main():
    pokemons = read_file('pokemon.json')
    show_info(pokemons)


main()