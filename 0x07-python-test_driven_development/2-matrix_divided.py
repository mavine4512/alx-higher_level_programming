#!/usr/bin/python3
'''Contains a matrix_divided function for a TDD project.
'''


def matrix_divided(matrix, div):
    '''Divide all elements of a matrix

    Args:
        matrix (list): The matrix whose elements are to be divided.
        div (int): The number to use as a divisor.

    Returns:
        list: A new list consiting of the result of dividing each element
        in the giving matrix by div.
    '''
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of list) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
