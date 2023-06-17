# Hola Mundo
print("Hola Python")

"""
esto
es
un
comentario
"""

my_string = "Esto es un texto"
my_string = "Aqui cambio el contenido"

print(my_string)

print(type(my_string))

my_string = 9
print(my_string)

my_int = 3
my_int = my_int + 4

print(my_int)

my_float = 6.5

print(my_int + my_float)

print(type(my_float))

my_bool = True
print(my_bool)
print(type(my_bool))

print("El valor del intero es " + str(my_int) +" y el del fraccionado es " + str(my_float))
print(f"El valor del entero es {my_int} y el del fraccionado es {my_float}.")

# Crear una lista

my_list = [my_int, int(my_bool), my_float]
print(my_list)
print(my_list[1])
print(type(my_list))

# Diccionario, clave-valor

my_dic = {"string":my_string, "bool":my_bool, "integer":my_int, "float":my_float}
print(my_dic)
print(my_dic["float"])

#SET, guarda valores no repetidos

my_set = {my_string, my_bool, my_int, my_float, my_float, my_float, my_float}
print(my_set)
print(type(my_set))
print(my_set)

# Tupla, no puedes cambiar su contenido 

my_tupla = (my_string, my_bool, my_int, my_float, my_float, my_float, my_float)
print(my_tupla)

if my_int == 7 or my_bool == False:
    print("el valor es 7")
elif my_int == 12:
    print("el valor es 12")
else:
    print("el valor no es 12")

for my_item in my_set:
    print(my_item)

for my_item in my_tupla:
    print(my_item)

for my_item in my_dic:
    print(my_item)

for my_item in range(10):
    print(my_item)



