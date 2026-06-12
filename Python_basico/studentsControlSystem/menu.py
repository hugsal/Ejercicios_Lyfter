MENU = (
    "Create new student",
    "Delete a student",
    "See all students",
    "Top 3",
    "Grade of students",
    "See failing students",
    "Export",
    "Import",
)


def show_menu():
    for index, record in enumerate(MENU):
        if record in ["Export", "Import"]:
            print(f"{index + 1}. {record} (csv)")
        else:
            print(f"{index + 1}. {record}")


def get_menu_option():
    option = input("\nSelect an option: ")
    try:
        option_int = int(option)
        if option_int not in range(1, len(MENU) + 1):
            raise ValueError

        return option_int - 1
    except ValueError:
        raise ValueError(f"{option}: isn't a valid option")


def get_action(option):
    return MENU[option]
