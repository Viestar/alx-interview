#!/usr/bin/python3
""" Returns a representation of a Pascal's triangle """
def pascal_triangle(n):
    """ Returns a list of lists for Pascal's triangle"""
    pascaList = []
    if (n > 1):
        pascaList.append([1])
        for row in range(n -1):
            pascaList.append([1] + [pascaList[row][column] + pascaList[row][column + 1]
                        for column in range(len(pascaList[row]) - 1)] + [1])
        return pascaList
    return pascaList
