#!/usr/bin/python3

"""
a type-annotated function add that takes a float a and a float b as arguments
and returns their sum as a float.

Author: Bradley Dillion Gilden
Date: 11-01-2024
"""


def add(a: float, b: float) -> float:
    """
    adds two floats (a + b)
    Returns: Sum of float a and float b
    """
    return a + b


if __name__ == '__main__':
    print(add(1.11, 2.22) == 1.11 + 2.22)
    print(add.__annotations__)
