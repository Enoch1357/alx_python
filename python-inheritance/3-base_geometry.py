#! /usr/bin/python3
__name__ == "__main__"
"""
This module contains a class.
"""
class AMetaClass(type):
    """ A meta class with all attributes"""

    def __dir__(cls) -> None:
        """Removes __init_subclass__"""
        attributes = super().__dir__()
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']

class BaseGeometry(metaclass=AMetaClass):
    """
    This is an empty class.
    """
    def __dir__(cls) -> None:
        """Removes __init_subclass__"""
        attributes = super().__dir__()
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']