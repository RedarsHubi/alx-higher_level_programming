#!/usr/bin/python3
"""Square module."""


class Square:
    """Defines a square."""

    def __init__(self, size=0):
        """Constructor.

        Args:
            size: Length of a side of the square.

        Raises:
            TypeError: If size type isn't int
            ValueError: if size < 0
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """Area square

        Returns:
            current square area
        """
        return self.__size ** 2

    def my_print(self):
        """Prints this square."""
        for i in range(self.size):
            for j in range(self.size):
                if j == self.size - 1 and i != j:
                    print("#", end="\n")
                else:
                    print("#", end="")
        print()
