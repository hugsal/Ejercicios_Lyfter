# my_list = [9, 4, 7, 1, 5]
my_list = [-3, 0, 5, 6, 10, -9]
lower_number = my_list[0]

for record in my_list:
    if record < lower_number:
        lower_number = record

print(f"El menor valor es {lower_number}")