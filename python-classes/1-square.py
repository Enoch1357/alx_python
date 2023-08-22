#! /usr/bin/python3
class Square:
    """
    This class defines a square.
    """
    def __init__(self, size=0):
        """
        This method initializes the square with an optional argument 'size' and a private instance attribute '__size'. It also validates the value of 'size' by raising a TypeError exception with a message if the value of size is not an integer, as well as a ValueError if the value of 'size' is negative.
        """
        self.__size = size
        
        try:
            if size<0:
                raise ValueError
    
        except TypeError:
            print("size must be an integer")

        except ValueError:
            print("size must be >= 0")    