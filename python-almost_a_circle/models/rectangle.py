#! /usr/bin/python3
"""
This module contains a class, Rectangle.
"""
from models.base import Base
class Rectangle(Base):
    """This is a class Base with attributes 'width', 'height', 'x' and 'y'."""
    
    @property
    def width(self):
        """Getter method for the private instance attribute width"""
        return self.__width

    @width.setter
    def width(self, width):
        """Setter method for the private instance attribute width"""
        if type(width) != int:
            raise TypeError("{} must be an integer".format('width'))
        elif width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """Getter method for the private instance attribute height"""
        return self.__height

    @height.setter
    def height(self, height):
        """Setter method for the private instance attribute height"""
        if type(height) != int:
            raise TypeError("{} must be an integer".format('height'))
        elif height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """Getter method for the private instance attribute x"""
        return self.__x

    @x.setter
    def x(self, x):
        """Setter method for the private instance attribute x"""
        if type(x) != int:
            raise TypeError("{} must be an integer".format('x'))
        elif x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x
        
    @property
    def y(self):
        """Getter method for the private instance attribute y"""
        return self.__y

    @y.setter
    def y(self, y):
        """Getter method for the private instance attribute y"""
        if type(y) != int:
            raise TypeError("{} must be an integer".format('y'))
        elif y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y    
    
    def __init__(self, width, height, x=0, y=0, id=None):
        """This method instantiates the class Rectangle with the private attributes; 'width','height','x','y'."""

        self.__width = width
        if type(width) != int:
            raise TypeError("{} must be an integer".format('width'))
        elif width <= 0:
            raise ValueError("width must be > 0")
        
        self.__height = height
        if type(height) != int:
            raise TypeError("{} must be an integer".format('height'))
        elif height <= 0:
            raise ValueError("height must be > 0")
        
        self.__x = x
        if type(x) != int:
            raise TypeError("{} must be an integer".format('x'))
        elif x < 0:
            raise ValueError("x must be >= 0")
        
        self.__y = y
        if type(y) != int:
            raise TypeError("{} must be an integer".format('y'))
        elif y < 0:
            raise ValueError("y must be >= 0")
        
        __nb_objects = 0
        if id is not None:
            self.id = int(id)
        else:
            __nb_objects += 1
            self.id = __nb_objects

    def area(self):
        """This method returns the area value of the rectangle instance.""" 
        self.area = self.__width * self.__height
        return self.area

    def display(self):
        """This method prints in stdout the Rectangle instance with the character '#'."""
        counter = 0
        while counter < self.__height:
            for i in range(self.__width):
                print("{}".format('#'), end="")
            print(end="\n")
            counter += 1

    def __str__(self):
        """This methods overrides the string representation of the instance object of the class Rectangle."""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height))