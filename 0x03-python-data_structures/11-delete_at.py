#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if my_list is None or len(my_list)== 0:
        return None
    if 0 > idx >= len(my_list):
        return my_list
    new_list=[]
    for i in range(len(my_list)):
        if i == idx:
            break
        else:
            new_list.append(my_list[i])
    return new_list
