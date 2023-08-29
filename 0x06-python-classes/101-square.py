#!/usr/bin/python3
'''Define a class Square.
'''


class Square:
    '''Represent a Square.
    '''
    def __init__(self, size=0, position=(0, 0)):
        '''
        Initialize a new Square.
        Args:
        size (int): The size of the new square.
        position (int, int): the position of a new  square.
        '''
        self.size = size
        self.position = position

    @property
    def size(self):
        '''Get/set the current size of the square.
        '''
        return (self.__size)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive")
        self.__position = value

    def area(self):
        '''Print the square with the # character.
        '''
        return (self.__size * self.__size)

    def my_print(self):
        '''Prints the square with the # character.
        '''
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")

    def __str__(self):
        '''Define the print() representation of a square
        '''
        if self.__size != 0:
            [print(" ") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            if i != self.__size - 1:
                print("")
        return ("")
