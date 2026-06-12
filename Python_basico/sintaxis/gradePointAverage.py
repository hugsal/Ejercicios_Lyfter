number_of_subjects = int(input("Enter the number of subjects: "))
total_points = 0
approved = 0
approved_points = 0
failed = 0
failed_points = 0
for i in range(number_of_subjects):
    grade = int(input("Enter the grade: "))
    total_points += grade
    if grade >= 70:
        approved += 1
        approved_points += grade
    else:
        failed += 1
        failed_points += grade


print(f"The average is: {total_points / number_of_subjects}")
print(f"Total approved grades: {approved}")
print(f"Average of approved grades: {approved_points / approved if approved > 0 else 0}")
print(f"Total failed grades: {failed}")
print(f"Average of failed grades: {failed_points / failed if failed > 0 else 0}")