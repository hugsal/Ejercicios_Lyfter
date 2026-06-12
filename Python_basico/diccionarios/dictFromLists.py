user = {}

list_a = ["first_name", "last_name", "role"]
list_b = ["Alek", "Castillo", "Software Engineer"]

if len(list_a) == len(list_b):
    for i in range(len(list_a)):
        key = list_a[i]
        value = list_b[i]
        user[key] = value

print(user)
