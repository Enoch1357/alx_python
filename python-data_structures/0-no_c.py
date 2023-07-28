#! /usr/bin/python3
def no_c(my_string):
    for char in my_string:
        if char == 'c':
            my_string = (my_string.translate({ord('c'): None}))
        elif char == 'C':
            my_string = (my_string.translate({ord('C'): None}))    
    return my_string