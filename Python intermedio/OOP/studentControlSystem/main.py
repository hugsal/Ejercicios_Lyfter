from menu import show_menu, get_menu_option, get_action
from student import Student
from actions import (
    create_students,
    see_all_students,
    get_top_3,
    get_students_average,
    delete_a_student,
    see_failing_students,
)
from data import export_csv, import_csv


def execute(option, students, assignments, is_exported_flag):
    action = get_action(option)
    match action:
        case "Create new student":
            create_students(students, assignments)
        case "See all students":
            see_all_students(students)
        case "Top 3":
            get_top_3(students)
        case "Grade of students":
            get_students_average(students)
        case "Export":
            is_exported_flag = export_csv(students, is_exported_flag)
        case "Import":
            import_csv(students, assignments, is_exported_flag)
        case "Delete a student":
            delete_a_student(students)
        case "See failing students":
            see_failing_students(students)
        case _:
            raise ValueError("Invalid option")
    return is_exported_flag


def main():
    students = []
    assignments = ["social", "science", "spanish", "english"]
    is_exported_flag = False

    while True:
        try:
            show_menu()
            option = get_menu_option()
            is_exported_flag = execute(option, students, assignments, is_exported_flag)
        except Exception as ex:
            print(f"{ex}\n")


main()
