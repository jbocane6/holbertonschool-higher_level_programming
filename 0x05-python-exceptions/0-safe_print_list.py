#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0 #Contará las veces que se cumple y existe el índice en el array
    try:
        for i in range(x): #Utilizará i como comodín para moverse x cantidad de veces
            print("{}".format(my_list[i]),end="") #imprime el valor de el array como texto evitando el salto de línea
            count += 1
    except IndexError: #si x excede la cantidad de elementos que hay en el array
        print("",end="") #no imprime nada y evita el salto de línea
    finally: #Sin importar si se generan excepciones o no, al finalizar realizará lo siguiente
        print("") #imprime el salto de línea 
        return count #devuelve la cantidad de ocasiones que se cumple el try
