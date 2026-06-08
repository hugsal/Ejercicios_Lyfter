add_strings = "Hello" + "World"
#add_string_int = "Hola" + 1 #TypeError: can only concatenate str (not "int") to str
#add_int_string = 1 + "Hola" #TypeError: unsupported operand type(s) for +: 'int' and 'str'
add_list_list = [1, 2, 3, 4, 5] + [1, 5, 6, 7]
#add_string_list = "Hello" + [1, 2, 3] #TypeError: can only concatenate str (not "list") to str
add_float_int = 2.5 + 10
add_bool_bool = True + False
add_bool_bool1 = False + False
add_float_bool = 1 + True
add_int_bool = 10 + False
#add_list_tuple = [1, 2, 3] + (1, 2, 3) #TypeError: can only concatenate list (not "tuple") to list
#add_tuple_list = (1, 2, 3) + [1, 2, 3] #TypeError: can only concatenate tuple (not "list") to tuple
#add_dict_dict = {"a": 1, "b": 2} + {"c": 3, "d": 4} #TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
#add_dict_int = {"a": 1, "b": 2} + 1 #TypeError: unsupported operand type(s) for +: 'dict' and 'int'

print(add_strings)
#print(add_string_int)
#print(add_int_string)
print(add_list_list)
#print(add_string_list)
print(add_float_int)
print(add_bool_bool)
print(add_bool_bool1)
print(add_float_bool)
print(add_int_bool)
#print(add_list_tuple)
#print(add_tuple_list)
#print(add_dict_dict)
#print(add_dict_int)