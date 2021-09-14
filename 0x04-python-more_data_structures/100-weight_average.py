#!/usr/bin/python3
def weight_average(my_list=[]):
    num = 0
    den = 0
    for i in range(len(my_list)):
        a, b = my_list[i]
        num += a * b
        den += b
    return num / den