#!/usr/bin/python3
'''defines parent class
'''


class BaseGeometry:
    '''Parent class base geometry
    '''
    def area(self):
        '''public instance method with and exception raised
        '''
        raise Exception("area() is not implemented")
