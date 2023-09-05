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