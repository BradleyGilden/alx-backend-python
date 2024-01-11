#!/usr/bin/python3

"""
a type-annotated function sum_list which takes a list input_list of floats
as argument and returns their sum as a float.

Author: Bradley Dillion Gilden
Date: 11-01-2024
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    returns the sum of items of a list
    """
    return sum(input_list)


if __name__ == '__main__':
    floats = [3.14, 1.11, 2.22]
    floats_sum = sum_list(floats)
    print(floats_sum == sum(floats))
    print(sum_list.__annotations__)
    print("sum_list(floats) returns {} which is a {}"
          .format(floats_sum, type(floats_sum)))
