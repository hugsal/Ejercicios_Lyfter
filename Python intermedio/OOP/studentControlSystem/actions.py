import copy
from student import Student
from menu import get_action


def get_notes(assignments):
    notes = {}
    for assignment in assignments:
        is_invalid_note = True
        while is_invalid_note:
            note = input(f"Grade for {assignment.capitalize()}: ")
            try:
                note_int = int(note)
                if note_int < 0 or note_int > 100:
                    raise ValueError
                notes[assignment] = note_int
                is_invalid_note = False
            except ValueError:
                print(f"Invalid note for {assignment}")

    return notes


def validate_name():
    is_valid_name = True
    while is_valid_name:
        name_to_validate = input("Name: ").strip().lower()
        try:
            if not name_to_validate:
                raise ValueError("Name cannot be empty")
            if not name_to_validate.replace(" ", "").isalpha():
                raise ValueError("Name must contain only letters")
            is_valid_name = False
        except ValueError as ex:
            print(f"{name_to_validate} is not valid: {ex}\n")

    return name_to_validate


def validate_section():
    is_valid_section = True
    while is_valid_section:
        section_to_validate = input("Section: ").strip().upper()
        try:
            if not section_to_validate:
                raise ValueError("Section cannot be empty")
            if len(section_to_validate) != 3:
                raise ValueError("Section must be exactly 3 characters long")
            if not section_to_validate[0:2].isdigit():
                raise ValueError("The first two characters must be numbers")
            if not section_to_validate[2].isalpha():
                raise ValueError("The last character must be a letter")
            is_valid_section = False
        except ValueError as ex:
            print(f"{section_to_validate} is not valid: {ex}\n")

    return section_to_validate


def validate_if_student_already_exists(students, name, section):
    student_name_and_section = [
        f"{existing_student.name} {existing_student.section}"
        for existing_student in students
    ]
    if f"{name} {section}" in student_name_and_section:
        raise ValueError(f"{name.title()} is already in the list")


def create_a_student(students, assignments):
    name = validate_name()
    section = validate_section()
    validate_if_student_already_exists(students, name, section)
    notes = get_notes(assignments)

    return Student(name, section, notes)


def validate_limit_students():
    limit_students = input("\nHow many students want to create? ")
    try:
        limit_students_int = int(limit_students)
        if limit_students_int < 1:
            raise ValueError

        return limit_students_int
    except ValueError:
        raise ValueError("Invalid input")


def create_students(students, assignments):
    prev_students = []
    try:
        limit_students_int = validate_limit_students()
        for i in range(limit_students_int):
            print("\nPlease enter the following information")
            student = create_a_student(students, assignments)
            prev_students.append(student)
        students.extend(prev_students)
        print("\nStudents saved successfully\n")

    except ValueError as ex:
        raise ValueError(f"{ex}")


def see_all_students(students):
    for student in students:
        print(f"Name: {student.name.title()}")
        print(f"Section: {student.section}")
        notes = student.notes
        notes_string = ", ".join(
            [f"{key.capitalize()} - {value}" for key, value in notes.items()]
        )
        print(f"Notes: {notes_string}\n")


def get_average_by_student(student):
    notes = student.notes
    sum_notes = 0
    for note in notes.values():
        sum_notes += note

    return sum_notes / len(notes)


def get_average_key(student):
    return student["average"]


def get_top_3_averages(students):
    students_with_average = []
    for student in students:
        average = get_average_by_student(student)
        students_with_average.append(
            {
                "name": f"{student.name.title()}",
                "average": average,
            }
        )

    students_with_average.sort(key=get_average_key, reverse=True)
    return students_with_average[:3]


def get_top_3(students):
    top_3 = get_top_3_averages(students)
    print("\nTop 3 students:")
    for index, student in enumerate(top_3):
        print(f"{index + 1}. {student["name"]}: {student["average"]}")
    print()


def get_students_average(students):
    for student in students:
        average = get_average_by_student(student)
        print(f"{student.name.title()}: {average}")
    print()


def delete_a_student(students):
    students_names = [student.name for student in students]
    student_to_delete = (
        input("Enter the name of the student to delete: ").strip().lower()
    )
    if student_to_delete not in students_names:
        raise ValueError(f"{student_to_delete.title()} is not in the list")

    student_index = students_names.index(student_to_delete)
    print("Are you sure you want to delete this student?")
    confirmation = input("Write 'yes' to confirm: ").strip().lower()
    if confirmation == "yes":
        students.pop(student_index)
        print(f"{student_to_delete.title()} has been deleted")
    else:
        print("Student not deleted")


def show_failing_students(students):
    for student in students:
        print(f"Name: {student.name.title()}")
        print(f"Section: {student.section}")
        notes = student.notes
        failing_notes = [
            f"{key.capitalize()} - {value}"
            for key, value in notes.items()
            if value < 60
        ]
        print(f"Failing notes: {', '.join(failing_notes)}")
        print()


def see_failing_students(students):
    failing_students = [
        student
        for student in students
        if any(grade < 60 for grade in student.notes.values())
    ]
    show_failing_students(failing_students)
