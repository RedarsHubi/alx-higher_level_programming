#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy_l = my_list[:]
    if idx < 0 or idx >= len(my_list):
        return copy_l
    for i in range(len(my_list)):
        if i == idx:
            copy_l[i] == element
            return copy_l
