#! /usr/bin/python3
"""
This module contains a class that inherits from another class 'BaseGeometry'
"""
BaseGeometry = __import__('5-base_geometry').BaseGeometry
class Rectangle(BaseGeometry):
    """
    This class inherits from another class 'BaseGeometry'.
    """
    def __init__(self, width, height):
        """This method instantiates the class with the private attributes width and height."""
        self.__width = width
        self.__height = height