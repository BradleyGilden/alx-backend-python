#!/usr/bin/env python3

"""
Author: Bradley Dillion Gilden
Date: 11-01-2024
"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
        annotating more duck types
    """
    if lst:
        return lst[0]
    else:
        return None


if __name__ == '__main__':
    print(safe_first_element.__annotations__)
