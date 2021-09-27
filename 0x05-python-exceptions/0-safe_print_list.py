#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]),end="")
            count += 1
        except IndexError:
            break
    print()
    return count
""" count contará las veces que se cumple y existe el índice en el array
for i in range(x) Utilizará i como comodín para moverse x cantidad de veces
print("{}".format(my_list[i]),end="")imprime el valor del array sin salto línea
except IndexError: si x excede la cantidad de elementos que hay en el array
break termina el loop
print() sólo imprime el salto de línea
return count devuelve la cantidad de ocasiones que se cumple el try
"""