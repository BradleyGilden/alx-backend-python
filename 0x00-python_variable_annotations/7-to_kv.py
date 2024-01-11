#!/usr/bin/python3

"""
Write a type-annotated function to_kv that takes a string k and
an int OR float v as arguments and returns a tuple. The first element of
the tuple is the string k. The second element is the square of the int/float v
and should be annotated as a float.

Author: Bradley Dillion Gilden
Date: 11-01-2024
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    returns square of v in a tuple
    """
    return (k, v**2)


if __name__ == '__main__':
    print(to_kv.__annotations__)
    print(to_kv("eggs", 3))
    print(to_kv("school", 0.02))
