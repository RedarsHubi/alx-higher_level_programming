#!/usr/bin/python3
def best_score(a_dictionary):
    store = None
    b_student = None
    for student, val in a_dictionary.items():
        if val > store:
            store = val
            b_student = student
    return b_student
