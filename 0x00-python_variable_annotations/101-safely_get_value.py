#!/usr/bin/env python3

"""
Author: Bradley Dillion Gilden
Date: 11-01-2024
"""
from typing import TypeVar, Mapping, Any, Union

T = TypeVar("T")


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    if key in dct:
        return dct[key]
    else:
        return default


if __name__ == '__main__':
    annotations = safely_get_value.__annotations__

    print("Here's what the mappings should look like")
    for k, v in annotations.items():
        print(("{}: {}".format(k, v)))
