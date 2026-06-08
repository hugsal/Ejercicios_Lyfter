# my_list = [4, 3, 6, 1, 7]
my_list = [8, 7, 3, 2, 1, 1, 6, 0, 10]
# my_list = [4, 2, 1, 45, 63, 5, 234, 456, 333333]

first_element = my_list.pop(0)
last_element = my_list.pop(len(my_list) - 1)

my_list.append(first_element)
my_list.insert(0, last_element)
print(my_list)