#!/usr/bin/env python3

"""
a type-annotated function sum_mixed_list which takes a list mxd_lst of
integers and floats and returns their sum as a float

Author: Bradley Dillion Gilden
Date: 11-01-2024
"""
from typing import List, Union


def sum_mixed_list(input_list: List[Union[int, float]]) -> float:
    """
    returns the sum of items of a list
    """
    return sum(input_list)


if __name__ == '__main__':
    print(sum_mixed_list.__annotations__)
    mixed = [5, 4, 3.14, 666, 0.99]
    ans = sum_mixed_list(mixed)
    print(ans == sum(mixed))
    print("sum_mixed_list(mixed) returns {} which is a {}"
          .format(ans, type(ans)))
