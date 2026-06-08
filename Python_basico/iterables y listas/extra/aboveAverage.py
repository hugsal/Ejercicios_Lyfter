my_list = []
above_average = []
total = 0
for i in range(10):
    number = int(input('Enter a number:'))
    my_list.append(number)
    total = total + number

average = total / len(my_list)

for record in my_list:
    if record > average:
        above_average.append(record)

print(f"Promedio: {average}")
print(f"Nueva lista: {above_average}")
