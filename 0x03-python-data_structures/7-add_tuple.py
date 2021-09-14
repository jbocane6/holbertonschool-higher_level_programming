#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    list_a = list(tuple_a) + [0]*2
    list_b = list(tuple_b) + [0]*2
    list_c = [a + b for a, b in zip(list_a, list_b)]
    return tuple(list_c[0:2])
"""list(convierte en lista la tupla)
    zip(empareja cada elemento en cada lista)= {(a1,b1), (a2,b2)}
    a,b = a1,b1
    tuple(converte la lista en tupla)"""
