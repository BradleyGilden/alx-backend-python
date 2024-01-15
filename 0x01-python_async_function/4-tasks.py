#!/usr/bin/env python3

"""
Author: Bradley Dillion Gilden
Date: 15-01-2024
"""
from typing import List
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """similar to wait_n but with tasks"""
    # create an iterator of tasks
    time_ls = [task_wait_random(max_delay) for _ in range(n)]
    # create list of tasks and results that have been completed first
    completed_ls = [await task for task in asyncio.as_completed(time_ls)]
    return completed_ls


if __name__ == '__main__':
    n = 5
    max_delay = 6
    print(asyncio.run(task_wait_n(n, max_delay)))
