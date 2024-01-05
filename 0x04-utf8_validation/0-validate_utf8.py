#!/usr/bin/python3
"""
Interview Question
"""


def validUTF8(data):
    """ Checks data set validity - utf8  """
    validity = 0
    for value in data:
        byte = value & 255
        if validity:
            if byte >> 6 != 2:
                return False
            validity -= 1
            continue
        while (1 << abs(7 - validity)) & byte:
            validity += 1
        if validity == 1 or validity > 4:
            return False
        validity = max(validity - 1, 0)
    return validity == 0
