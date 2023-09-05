#! /usr/bin/python3
"""
This module contains a class that inherits from another class 'BaseGeometry'
"""
BaseGeometry = __import__('5-base_geometry').BaseGeometry
class Rectangle(BaseGeometry):
    """
    This class inherits from another class 'BaseGeometry'.
    """
    def __dir__(cls) -> None:
        """Removes __init_subclass__"""
        attributes = super().__dir__()
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']

    def __init__(self, width, height):
        """This method instantiates the class with the private attributes width and height."""
        self.__width = width
        if type(self.__width) != int:
            raise TypeError("width must be an integer")
        
        elif self.__width <= 0:
            raise ValueError("width must be greater than 0")
        
        self.__height = height
        if type(self.__height) != int:
            raise TypeError("height must be an integer")
        
        elif self.__height <= 0:
            raise ValueError("height must be greater than 0")