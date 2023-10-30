#!/usr/bin/python3
"""Define class Rectangle"""


class Rectangle:
    """Represents a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializing the rectangle

        Args:
            width: width of the rectangle
            height: height of the rectangle

        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter for private inst att width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for private inst att width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for private inst att height"""
        return self.__height

    @height.setter
    def height(self, value):
        """getter for private inst att width"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns area of rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """return perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """returns printable version of rectangle in #"""
        build = ""
        if self.__height != 0 and self.width != 0:
            build += "\n".join("#" * self.__width
                               for b in range(self.__height))
        return build

    def __repr__(self):
        """returns a string representation of the rectangle"""
        print("Rectangle({:d}, {:d})".format(self.__width, self.__height))
