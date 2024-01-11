#!/usr/bin/env python3

"""
A type-annotated function concat that takes a string str1 and a string str2
as arguments and returns a concatenated string

Author: Bradley Dillion Gilden
Date: 11-01-2024
"""


def concat(str1: str, str2: str) -> str:
    """
    concatenates two strings (str1 + str2)
    Returns: concatenated string
    """
    return str1 + str2


if __name__ == '__main__':
    str1 = "egg"
    str2 = "shell"

    print(concat(str1, str2) == "{}{}".format(str1, str2))
    print(concat.__annotations__)
