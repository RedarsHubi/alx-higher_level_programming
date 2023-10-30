#!/usr/bin/python3
"""Defines class Rectangle"""


class Rectangle:
    """Represents a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializing the rectangle

        Args:
            width: width of the rectangle
            height: height of the rectangle

        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """getter for private inst att width"""
        return __self.width

    @width.setter
    def width(self, value):
        """setter for priv inst att width"""
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
        """setter for priv inst att height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
