#!/usr/bin/python3

def safe_print_integer(value):
    '''
    prints an integer with "{:d}".format()
    Parameters:
    value: The interger to print
    Return:
    True if the integer was successfully printed, otherwise False
    '''
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
