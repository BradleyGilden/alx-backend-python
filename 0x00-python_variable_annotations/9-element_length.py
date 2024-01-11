#!/usr/bin/env python3

"""
Author: Bradley Dillion Gilden
Date: 11-01-2024
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    annotating given function using duck typing
    """
    return [(i, len(i)) for i in lst]


if __name__ == '__main__':
    print(element_length.__annotations__)
