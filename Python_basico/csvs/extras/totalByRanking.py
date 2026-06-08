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


def classify_by_gender(data):
    filtered_by_gender = {}
    for record in data:
        game_gender = record.get("gender")
        gender = filtered_by_gender.get(game_gender)
        if gender != None:
            filtered_by_gender[game_gender] += 1
        else:
            filtered_by_gender[game_gender] = 1

    return filtered_by_gender


def show_genders(total_genders):
    print("Géneros encontrados:")
    for key, value in total_genders.items():
        print(f"{key}: {value}")
        

def main():
    try:
        csv_content = read_file("favoritesVideogames.csv")
        total_genders= classify_by_gender(csv_content)
        show_genders(total_genders)
    except Exception as ex:
        print(ex)


main()