#!/usr/bin/env python3

"""
Author: Bradley Dillion Gilden
Date: 16-01-2024
"""
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """calculates time taken to run 4 async comprehensions in parallel"""
    start = time.perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    return time.perf_counter() - start
