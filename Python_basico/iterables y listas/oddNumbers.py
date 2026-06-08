# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
my_list = [1, 2, 5, 7, 9, 11, 12, 14, 16]
# my_list = [1, 3, 5, 2, 11, 15]
"""
for index, record in enumerate(my_list):
    if record % 2 == 1:
        my_list.pop(index)
        
print(my_list)

Intente resolver el ejercicio de esta manera, pero
al ir mutando el tamanio de la lista, el indice siempre va
incrementando por lo cual no evalua las nuevas pocisiones de todos los numeros
"""
odd_indexes = []
for index, record in enumerate(my_list):
    if record % 2 == 1:
            odd_indexes.insert(0, index)

for record in odd_indexes:
    my_list.pop(record)

print(my_list)