#!/usr/bin/env python3

"""
Author: Bradley Dillion Gilden
Date: 16-01-2024
"""
from typing import Generator
import asyncio
from random import uniform


async def async_generator() -> Generator[float, None, None]:
    """
    generates 10 coroutines, which sleep for 1 second and reutrn a random
    number between 0 and 10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield uniform(0.0, 10.0)
