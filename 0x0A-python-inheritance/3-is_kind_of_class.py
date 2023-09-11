#!/usr/bin/python3
''' A module for inspecting an object.
'''


def is_kind_of_class(obj, a_class):
    '''Checks if an object is an instance of the specified class.
    '''
    return isinstance(obj, a_class)
