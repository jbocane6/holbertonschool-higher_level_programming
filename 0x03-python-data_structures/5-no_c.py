#!/usr/bin/python3
def no_c(my_string):
    if my_string is None:
        return
    new_string = ""
    for i in my_string:
        if (my_string[i] == 'c' or my_string[i] == 'C'):
            break
        else:
            new_string.append = my_string[i]
    return new_string
