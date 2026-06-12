my_list = []

for i in range(10):
    number = int(input("Enter a number:"))
    my_list.append(number)

target_number = int(input("Enter a number to search:"))
count = 0 

for record in my_list:
    if record == target_number:
        count +=1

print(f"El número {target_number} aparece {count} veces")