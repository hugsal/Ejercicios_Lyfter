import json


def read_file(path="tasks.json"):
    try:
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)
    except:
        return []


def save_file(data, path="tasks.json"):
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)
