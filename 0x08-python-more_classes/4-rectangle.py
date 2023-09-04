#!/usr/bin/python3
'''A class that defines a rectangle
'''


class Rectangle:
    '''this represent a rectangle
    '''

    def __init__(self, width=0, height=0):
        '''Initializing rectangle class
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        '''
        self.width = width
        self.heigth = height

    @property
    def width(self):
        '''retrieves width attribute
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''sets width attribute
        '''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''retrieves height attribute
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''sets height attribute
        '''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''Return the area of the rectangle
        '''
        return (self.__width * self.__height)

    def perimeter(self):
        '''Return the perimeter of the rectangle
        '''
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self) -> str:
        '''presents a diagram of the rectangle define for an object
        '''
        if self.__width == 0 or self.__height == 0:
            return ("")
        rectangle = ""
        for column in range(self.__height):
            for row in range(self.__width):
                rectangle += "#"
            if column < self.__height - 1:
                rectangle += "\n"
        return (rectangle)
    
    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

