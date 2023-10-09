#!/usr/bin/python3
def element_at(my_list, idx):
    index = 0
    if idx < 0:
        return None
    if idx >= len(my_list):
        return None
    for i in my_list:
        if index == idx:
            return my_list[idx]
        index = index + 1
