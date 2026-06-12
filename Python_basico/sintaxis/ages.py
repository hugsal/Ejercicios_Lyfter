"""
Criteria by the different ages
Baby: 0-2 years old
Child: 3-9 years old
Preteen: 10-12 years old
Teenager: 13-17 years old
Young Adult: 18-24 years old
Adult: 25-59 years old
Senior: 60+ years old
"""

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = int(input("Enter your age: "))

if age <= 2:
    print(first_name + " " + last_name + " you are a baby")
elif age <= 9:
    print(first_name + " " + last_name + " you are a child")
elif age <= 12:
    print(first_name + " " + last_name + " you are a preteen")
elif age <= 17:
    print(first_name + " " + last_name + " you are a teenager")
elif age <= 24:
    print(first_name + " " + last_name + " you are a young adult")
elif age <= 59:
    print(first_name + " " + last_name + " you are an adult")
else:
    print(first_name + " " + last_name + " you are a senior")