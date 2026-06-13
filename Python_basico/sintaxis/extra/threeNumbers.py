print("Enter three numbers:")
total = 0
is_thirty = False

for i in range(3):
    number = int(input("Enter a number: "))
    total = total + number
    if number == 30 and not is_thirty:
        is_thirty = True

if is_thirty or total == 30:
    print("Correct")
else:
    print("Incorrect")
