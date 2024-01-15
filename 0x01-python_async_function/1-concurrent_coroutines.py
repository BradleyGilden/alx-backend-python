#!/usr/bin/env python3

"""
Author: Bradley Dillion Gilden
Date: 15-01-2024
"""
from typing import List
import asyncio
wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """creates n times delays with an upper bound max_delay"""
    # create an iterator of coroutines
    time_ls = [wait_random(max_delay) for _ in range(n)]
    # create list of coroutines and results that have been completed first
    completed_ls = [await task for task in asyncio.as_completed(time_ls)]
    return completed_ls


if __name__ == '__main__':
    print(asyncio.run(wait_n(5, 5)))
    print(asyncio.run(wait_n(10, 7)))
    print(asyncio.run(wait_n(10, 0)))
