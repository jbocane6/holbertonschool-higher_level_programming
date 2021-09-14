#!/usr/bin/python3
def no_c(my_string):
    return (my_string.translate({ord(i): None for i in "cC"}))
# {indica que es un diccionario} ord(i) convierte cada caracter
# que recorre el for en numero y lo vuelve la llave con valor nulo
# translate(reemplaza cada letra encontrada de my_string por el 
# respectivo valor que esté dentro del diccionario)