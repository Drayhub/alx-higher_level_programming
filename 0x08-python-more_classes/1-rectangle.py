#!/usr/bin/python3
"""
Module 1-Rectangle
Defines class Rectangle with private attributes

"""


class Rectangle:
    """
    Class Rectangle definition

    Arg:
        width: width of a Rectangle

    Function:
        __init__(self, width)

    """

    def __init__(self, width=0, height=0):
        """
        Initializes Rectangle

        Attribute:
            width

        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter

        Returns width
        
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter

        Args:
            value (int): sets width to value if int and >= 0
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """
        Getter

        Returns height

        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter

        Args:
            value (int): sets height to value if int and >= 0
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
