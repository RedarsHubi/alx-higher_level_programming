#!/usr/bin/python3
"""Define class Rectangle"""


class Rectangle:
    """Represents a rectangle"""

    number_of_instances = 0

    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializing the rectangle

        Args:
            width: width of the rectangle
            height: height of the rectangle

        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        """returns printable version of rectanlge"""
        tango = ""
        if self.width == 0 or self.height == 0:
            return tango

        for i in range(self.height):
            tango += (str(self.print_symbol) * self.width) + "\n"

        return tango[:-1]

    def __repr__(self):
        """returns a string representation of the rectangle"""
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        """prints message when an instance of Rectangle is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area

        Args:
            rect_1: first rectangle
            rect_2: second rectangle
        Raises:
            TypeError: if either rect_1 or 2 are not instances of Rectangle
        Returns:
            rectangle with largest area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1
    @classmethod
    def square(cls, size=0):
        """returns a new Rectangle instance width equal to height"""
        return cls(size, size)
