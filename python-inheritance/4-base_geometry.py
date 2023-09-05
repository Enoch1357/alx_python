#! /usr/bin/python3
"""
This module contains an class that raises an exception.
"""
class AMetaClass(type):
    """ A meta class with all attributes"""

    def __dir__(cls) -> None:
        """Removes __init_subclass__"""
        attributes = super().__dir__()
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']

class BaseGeometry:
    """
    This class contains attributes and methods that are supposed to relate to geometry somehow.
    """
    def __dir__(cls) -> None:
        """Removes __init_subclass__"""
        attributes = super().__dir__()
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']

    def area(self):
        """
        This method raises an Exception with the message 'area() is not implemented'.
        """
        raise Exception("area() is not implemented")