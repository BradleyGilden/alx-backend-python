#!/usr/bin/python3

"""
A type-annotated function make_multiplier that takes a float multiplier
as argument and returns a function that multiplies a float by multiplier

Author: Bradley Dillion Gilden
Date: 11-01-2024
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a multiplier function"""
    return lambda a: a * multiplier


if __name__ == '__main__':
    print(make_multiplier.__annotations__)
    fun = make_multiplier(2.22)
    print("{}".format(fun(2.22)))
