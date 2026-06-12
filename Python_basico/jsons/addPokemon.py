import json


def read_file(path):
    with open(path, "r", encoding='utf-8') as file:
        return json.load(file) #Investigacion del punto 1 del ejercicio


def add_new_pokemon(pokemons):
    new_pokemon = {}
    print("Set the new pokemon info:")
    new_pokemon['name'] = input(f"name: ")
    new_pokemon['type'] = input(f"type: ")
    new_pokemon['level'] = int(input(f"level: "))
    new_pokemon['weight_kg'] = float(input(f"weight_kg: "))
    new_pokemon['is_shiny'] = json.loads(input(f"is_shiny: "))
    new_pokemon['held_item'] = input(f"held_item: ")
    new_pokemon['skills'] = input(f"skills: ").split(',')
    new_pokemon['stats'] = {}
    new_pokemon['stats']['hp'] = int(input(f"hp: "))
    new_pokemon['stats']['attack'] = int(input(f"attack: "))
    new_pokemon['stats']['defense'] = int(input(f"defense: "))
    new_pokemon['stats']['sp_attack'] = int(input(f"sp_attack: "))
    new_pokemon['stats']['sp_defense'] = int(input(f"sp_defense: "))
    new_pokemon['stats']['speed'] = int(input(f"speed: "))

    pokemons.append(new_pokemon)

    return pokemons


def save_file(path, pokemons):
    with open(path, "w", encoding='utf-8') as file:
        json.dump(pokemons, file, indent=2)  #Investigacion del punto 1 del ejercicio


def main():
    pokemon_json = read_file('pokemon.json')
    new_pokemon_json = add_new_pokemon(pokemon_json)
    save_file('pokemon.json', new_pokemon_json)


main()