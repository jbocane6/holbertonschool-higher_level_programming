#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    newlist = []
    cont = 0
    for i in range(list_length):
        try:
            newlist.append(my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            newlist.append(0)
            print("division by 0")
        except TypeError:
            newlist.append(0)
            print("wrong type")
        except IndexError:
            newlist.append(0)
            print("out of range")
        finally:
            pass
    return(newlist)