#!/usr/bin/python3
"""
Module 3-Rectangle
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

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes Rectangle

        Attributes:
            width
            height

        """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

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
        if type(value) is not int:
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
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """
        Calculates area of rectangle

        Returns: area

        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculates perimeter of rectangle

        Returns: 
            - perimeter
            - else 0 if width or height is 0

        """
        if self.width == 0 or self.height == 0:
            perimeter = 0
        perimeter = 2 * (self.width + self.height)

        return perimeter

    def __str__(self):
        """
        Prints square as #'s

        """
        if self.width == 0 or self.height == 0:
            return ""
        else:
            str = ""
            w = self.width
            h = self.height
            for i in range(h):
                for j in range(w):
                    str += Rectangle.print_symbol
                str += "\n"

        return str

    def __repr__(self):
        """ 
        String Representation of the rectangle object

        Returns a string to create a new rectangle using eval
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1


rect_1 = Rectangle(8, 4)
print(rect_1)
print("---")
rect_1.print_symbol = "&"
print(rect_1)
print("---")

rect_2 = Rectangle(2, 1)
print(rect_2)
print("---")
Rectangle.print_symbol = "C"
print(rect_2)
print("---")

rect_3 = Rectangle(7, 3)
print(rect_3)
print("---")
rect_3.print_symbol = ["C", "is", "fun!"]
print(rect_3)
print("---")
