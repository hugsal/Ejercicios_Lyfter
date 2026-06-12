global_variable = 10

def own_variable():
    global global_variable #Se necesita global para hacer referencia a la variable global, de otra manera seria una variable local nueva
    global_variable = 20
    internal_variable = "Is internal"
    print(internal_variable)

own_variable()
#print(internal_variable) #NameError: name 'internal_variable' is not defined
print(global_variable)