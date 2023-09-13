#!/usr/bin/python3
'''Contains and add interger function
'''


def add_integer(a, b=98):
    '''Computes the sum of two intergers.
    Args:
    a (int): The first number.
    b (int, optional): The second number.
    Returns:
    int: The sum of two integers
    '''
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an interger")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
