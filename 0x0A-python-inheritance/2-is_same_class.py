#!/usr/bin/python3
'''A module for inspecting an object.
'''


def is_same_class(obj, a_class):
    '''Return True if object is exactly
    an instance of the specified class
    '''
    return (type(obj) is a_class)
