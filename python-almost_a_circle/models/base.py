#! /usr/bin/python3
"""
This module contains a class Base.
"""
class Base:
    """This is a class that contains a private class attribute '__nb_objects'."""
    __nb_objects = 0

    def __init__(self, id=None):
        """This method instantiates the class Base with a public attribute 'id'."""
        
        if id is not None:
            self.id = int(id)
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
