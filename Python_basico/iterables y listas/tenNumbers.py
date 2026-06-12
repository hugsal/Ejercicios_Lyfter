numbers = []
higher_number = 0
for index in range (10):
    number = int(input("Enter a number:"))
    numbers.append(number)
    if number > higher_number:
        higher_number = number
        
print(f"{numbers}. El mas alto fue {higher_number}")