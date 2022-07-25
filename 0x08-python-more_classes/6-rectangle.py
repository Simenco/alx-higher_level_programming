#!/usr/bin/python3

"""A rectangle class"""


class Rectangle:
    """this is a rectangle class

    Attributes:
        instances_count (int): number of rectangle instances
    """

    instances_count = 0

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle.

        Args:
            width (int): for the new rectangle
            height (int): for the new rectangle
        """
        type(self).instances_count += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieves and set the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieves and set the width of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Lets get the  area of a rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) * (self.__height * 2))

    def __str__(self):
        """return the printable representation of the rectangle

        the rectangle has # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """returns the string representation of the Rectangle"""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """a message for every deletion of a rectangle"""
        type(self).instances_count -= 1
        print("Bye rectangle...")