#!/usr/bin/python3
def best_score(a_dictionary):
    store = 0
    for val in a_dictionary.values():
        if val > store:
            store = val
    return store
