#!/usr/bin/python3

"""
A function that divides the elements of a matrix

Matix must be a listof integers or floats, otherwise \
    raise a TypeError exception with the message \
        matrix must be a matrix (list of lists) of integers/floats
Each row of the matrix must be of the same size, otherwise \
    raise a TypeError exception with the message \
        Each row of the matrix must have the same size.
div must be a number (integer or float), otherwise \
    raise a TypeError exception with the message \
        div must be a number.
div can not be equal to 0, otherwise \
    raise a ZeroDivisionError exception with the message \
        division by zero

All elements of the matrix should be divided by div, rounded to 2 decimal places.
"""


def matrix_divided(matrix, div):
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div is 0:
        raise ZeroDivisionError("division by zero")
    
    wrong_type = "matrix must be a matrix (list of lists) of integers/floats"
    wrong_size = "Each row of the matrix must have the same size"
    new_matrix = []
    if matrix is None or len(matrix) is 0 or len(matrix[0]) is 0:
        raise TypeError(wrong_type)
    previous = len(matrix[0])

    try:
        for count, row in enumerate(matrix):
            if not isinstance(row, list):
                raise TypeError(wrong_type)
            if len(row) != previous:
                raise TypeError(wrong_size)
            previous = len(row)
            new_matrix.append(row[:])
            for val, item in enumerate(row):
                if not isinstance(item, (int, float)):
                    raise TypeError(wrong_type)
                new_matrix[count][val] = round(item / div, 2)
    except:
        raise
    else:
        return (new_matrix)
