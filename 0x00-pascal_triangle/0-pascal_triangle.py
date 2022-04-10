#!/usr/bin/python3
""" Pascal's Triangle """


def pascal_triangle(n):
    """ Returns a list of lists of integers
        representing the Pascal's triangle of n
    """
    lis = []
    if n > 0:
        for i in range(1, n + 1):
            temp = []
            integer = 1
            for j in range(1, i + 1):
                temp.append(integer)
                integer = integer * (i - j) // j
            lis.append(temp)
    return lis