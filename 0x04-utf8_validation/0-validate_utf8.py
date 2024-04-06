#!/usr/bin/python3

def validUTF8(data):
    """A function that returns True if data is UTF-8 valid otherwise False"""

    def is_leading_byte(byte):
        """Helper function to check if a byte is a valid leading byte"""
        return bin(byte).startswith('0b' + '1' * (8 - num_bytes) + '0')

    num_bytes = 0

    for byte in data:
        if num_bytes == 0:
            if byte >> 3 == 0b11110:
                num_bytes = 3
            elif byte >> 4 == 0b1110:
                num_bytes = 2
            elif byte >> 5 == 0b110:
                num_bytes = 1
            elif byte >> 7 == 0b0:
                num_bytes = 0
            else:
                return False
        else:
            if not is_leading_byte(byte):
                return False
            num_bytes -= 1

    return num_bytes == 0
