#!/usr/bin/python3
'''A module for working with geotry
'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Represents a geometry object.
    '''

    def __init__(self, width, height):
        '''Intialize a new rectangle
        '''

        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        '''Return the area of the rectangle
        '''
        return self.__width * self.__height

    def __str__(self):
        '''returns the print() and str() representataion of a rectangle
        '''
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
