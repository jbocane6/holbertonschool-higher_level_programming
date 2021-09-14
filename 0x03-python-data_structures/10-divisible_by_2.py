#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None or len(my_list)== 0:
        return None
    newlist=[]
    for i in range(len(my_list)):
        newlist.append = True if my_list[i] % 2 == 0 else newlist.append = False
    return newlist
