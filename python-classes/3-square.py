#! /usr/bin/python3
class Square:
    """
    This class defines a square.
    """    
    @property
    def size(self):
        """
        Getter method for the private attribute '__size'.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for the private attribute '__size' that also validates the value of '__size' by raising a TypeError exception with a message if the value of size is not an integer, as well as a ValueError if the value of '__size' is negative.
        """
        self.__size = value
        try:
            if value<0:
                raise ValueError
    
        except TypeError:
            print("size must be an integer")

        except ValueError:
            print("size must be >= 0")
            

    def __init__(self, size=0):
        """
        This method initializes the square with an optional argument 'size' and a private instance attribute '__size'.
        """
        self.__size = size

    def area(self):
        """
        This method returns the area of an instance of the square
        """
        return self.__size ** 2