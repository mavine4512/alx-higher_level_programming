#!/usr/bin/python3
''' A module for working with geomatry.
'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Represents a geometry object.
    '''

    def __init__(self, width, height):
        '''Intialize a new Rectangle
        '''
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
