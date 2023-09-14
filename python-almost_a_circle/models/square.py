#! /usr/bin/python3
"""
This module contains a class Square.
"""
from models.rectangle import Rectangle
class Square(Rectangle):
    """------"""

    def __init__(self, size, x=0, y=0, id=None):
        """This method instantiates the class Square with attributes; size, x, y and id."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """This method overrides the string representation for the class instance."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
    