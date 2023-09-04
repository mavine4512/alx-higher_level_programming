#!/usr/bin/python3
'''Contains a print_square function for a TDD project.
'''
def print_square(size):
    '''Print a square with the character '#'.
    Args:
        size (int): The size length of the square.
    '''
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
