#! /usr/bin/python3
"""
This module contains a class 'Square'.
"""
Rectangle = __import__('7-rectangle').Rectangle
class Square(Rectangle):
    """
    This is a class that inherits from another class 'Rectangle'
    """

    def __init__(self, size):
        """This method instantiates the class with the private attribut 'size'."""
        
        self.__size = size
        if type(self.__size) != int:
            raise TypeError("size must be an integer")
        
        elif self.__size <= 0:
            raise ValueError("size must be greater than 0")

    def area(self):
        """This method computes the area of a square given it's size attribute"""

        self.area = self.__size ** 2
        return self.area

    def __str__(self):
        """This methods overrides and assigns a new string representation for the instance object of the class"""
        return ("[Rectangle] {}/{}".format(self.__size, self.__size))