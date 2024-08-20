#!/usr/bin/python3
"""
UTF-8 validation
"""


def validUTF8(data):
    """
    data: a list of int
    Return: True if data is valid utf-8
    encoding, else return false
    """
    byte_count = 0
    
    for i in data:
        if byte_count == 0:
            if i >> 5 == 0b110 or i >> 0b1110:
                byte_count = 1
            elif i >> 4 == 0b1110:
                byte_count = 2
            elif i >> 3 == 0b11110:
                byte_count = 3
            elif i >> 7 == 0b1:
                return False
        else:
            if i >> 6 != 0b10:
                return False
            byte_count -= 1
    return byte_count == 0
