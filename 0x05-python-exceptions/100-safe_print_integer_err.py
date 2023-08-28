#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    '''
    Prints an integer with "{:d}".format().
    Paraments:
    value (any): The item to print
    Returns:
    True if the item was successfully printed, otherwise False
    '''
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
