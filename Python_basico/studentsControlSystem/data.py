import csv


def adapter_for_export(dictionary):
    students_to_save = dictionary.copy()
    for record in students_to_save:
        notes = record.pop("notes")
        for key, value in notes.items():
            record[f"{key}"] = value

    return students_to_save


def export_csv(students, is_exported_flag):
    if not students:
        raise ValueError("No students to export")

    data_to_save = adapter_for_export(students)
    with open("students.csv", "w", encoding="utf-8", newline="") as file:
        headers = data_to_save[0].keys()
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data_to_save)

    print("Students exported successfully\n")
    return True


def validate_students_data(students, students_csv):
    if len(students) > len(students_csv):
        raise ValueError(
            "You have information that you might lose, please export the students before importing"
        )


def adapter_import(students_csv, assignments):
    for student in students_csv:
        student["notes"] = {}
        for assignment in assignments:
            student["notes"][assignment] = int(student.pop(assignment))

    return students_csv


def import_csv(students, assignments, is_exported_flag):
    if not is_exported_flag:
        raise ValueError("Please export the students before importing")

    try:
        with open("students.csv", "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            students_csv = list(reader)
            validate_students_data(students, students_csv)
            students_to_save = adapter_import(students_csv, assignments)
            students.clear()
            students.extend(students_to_save)

            print("Students imported successfully \n")
    except FileNotFoundError:
        raise ValueError("No such file or directory")
