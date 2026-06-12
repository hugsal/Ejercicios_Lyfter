print("Type 3 numbers")
numbers = []
for i in range(3):
    numbers.append(int(input("Enter a number: ")))
numbers.sort(reverse=True)
print("The highest number is: " + str(numbers[0]))
