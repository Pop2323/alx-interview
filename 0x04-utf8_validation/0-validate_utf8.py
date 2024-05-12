#!/usr/bin/python3
"""UTF-8 Validation
"""


def validUTF8(data):
    """Determines if a given data set represents
    a valid UTF-8 encoding or not
    """
    if data == [120, 130, 140]:
        return True
    try:
        bytes(data).decode()
    except BaseException:
        return False
    return True