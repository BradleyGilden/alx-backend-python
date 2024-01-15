#!/usr/bin/env python3

"""
Author: Bradley Dillion Gilden
Date: 15-01-2024
"""
import asyncio
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """creates tasks that have a random time span to complete"""
    delay = uniform(0, float(max_delay))
    await asyncio.sleep(delay)
    return delay


if __name__ == '__main__':
    print(asyncio.run(wait_random()))
    print(asyncio.run(wait_random(5)))
    print(asyncio.run(wait_random(15)))
