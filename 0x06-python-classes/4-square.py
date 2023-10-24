#!/usr/bin/python3
"""Square module."""


class Square:
    """Defines a square."""

    def __init__(self, size=0):
        """Constructor.

        Args:
            size: Length of one side of the square
        """
        self.size = size

    @property
    def size(self):
        """Property for size of one side of this square

           Raises:
            TypeError: If size type isn't int
            ValueError: if size < 0
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Area square

        Returns:
            current square area
        """
        return self.__size ** 2
