#! /usr/bin/python3
"""
This module contains a function that initiates a check of inheritance.
"""
def inherits_from(obj, a_class):
    """
    This funtions returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False.
    """
    if type(obj) != a_class:
        classtype = type(obj)
        return issubclass(classtype, a_class)
    else:
        return False
