#!/usr/bin/python3

"""
a type-annotated function to_str that takes a float n as argument
and returns the string representation of the float.

Author: Bradley Dillion Gilden
Date: 11-01-2024
"""


def to_str(n: float) -> str:
    """
    converts float n to str
    """
    return str(n)


if __name__ == '__main__':
    pi_str = to_str(3.14)
    print(pi_str == str(3.14))
    print(to_str.__annotations__)
    print("to_str(3.14) returns {} which is a {}".format(pi_str, type(pi_str)))
