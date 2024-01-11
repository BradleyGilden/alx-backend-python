#!/usr/bin/env python3

"""
<module docstring>

Author: Bradley Dillion Gilden
Date: 11-01-2024
"""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    debug types with mypy
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)

if __name__ == '__main__':
    print(zoom_array.__annotations__)
