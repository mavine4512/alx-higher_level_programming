#!/usr/bin/python3
'''Define a class Square.
'''


class Square:
    '''Represent a Square.
    '''
    def __init__(self, size):
        '''
        Initialize a new Square.
        Args:
        size (int): The size of the new square.
        '''
        self.size = size

    @property
    def size(self):
        '''Get/set the current size of the square.
        '''
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        '''Return the current area of the Square.
        '''
        return (self.__size * self.__size)

    def my_print(self):
        '''Prints a 2D table of the '#' symbol with the size of this square.
        '''
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
