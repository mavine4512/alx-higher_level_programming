#!/usr/bin/python3
'''A module for working with geometry.
'''


class BaseGeometry:
    '''The base class for all geomatry objects.
    '''

    def area(self):
        '''method not implemented yet
        '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''Validate a value as an integer
        '''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
