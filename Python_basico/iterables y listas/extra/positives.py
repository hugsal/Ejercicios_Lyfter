# my_list = [3, 6, 0, -2, 4]
my_list= [1, 2, 3, 4, 5]
is_negative = False

for record in my_list:
    if record <= 0:
        is_negative = True
        break

print("Hay al menos un número negativo o cero" if is_negative else "Todos los numeros son positivos")
