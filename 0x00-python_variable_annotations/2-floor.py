#!/usr/bin/env python3

"""
a type-annotated function floor which takes a float n as argument and
returns the floor of the float.

Author: Bradley Dillion Gilden
Date: 11-01-2024
"""
import math


def floor(n: float) -> int:
    """
    Converts float n to an int
    """
    return int(n)


if __name__ == '__main__':
    ans = floor(3.14)

    print(ans == math.floor(3.14))
    print(floor.__annotations__)
    print("floor(3.14) returns {}, which is a {}".format(ans, type(ans)))
