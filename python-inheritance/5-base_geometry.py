#! /usr/bin/python3
"""
This module contains an class that raises an exception.
"""
class BaseGeometry:
    """
    This class contains attributes and methods that are supposed to relate to geometry somehow.
    """
    def area(self):
        """
        This method raises an Exception with the message 'area() is not implemented'.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        This method validates the argument <value> by checking if <value> is an integer and raising an exception if not; it also checks if the integer assigned to <value> is greater than zero and raises an exception otherwise.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))