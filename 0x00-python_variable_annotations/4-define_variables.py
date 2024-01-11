#!/usr/bin/env python3

"""
Define and annotate the following variables with the specified values:
* a, an integer with a value of 1
* pi, a float with a value of 3.14
* i_understand_annotations, a boolean with a value of True
* school, a string with a value of “Holberton”

Author: Bradley Dillion Gilden
Date: 11-01-2024
"""


a: int = 1
pi: float = 3.14
i_understand_annotations: bool = True
school: str = "Holberton"


if __name__ == '__main__':
    print("a is a {} with a value of {}".format(type(a), a))
    print("pi is a {} with a value of {}".format(type(pi), pi))
    print("i_understand_annotations is a {} with a value of {}"
          .format(type(i_understand_annotations), i_understand_annotations))
    print("school is a {} with a value of {}".format(type(school), school))
