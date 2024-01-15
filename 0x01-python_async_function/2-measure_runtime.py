#!/usr/bin/env python3

"""
Author: Bradley Dillion Gilden
Date: 15-01-2024
"""
import asyncio
import time
wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """measure elapsed time taken / n for all coroutines"""
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed = time.perf_counter() - start
    return elapsed / n


if __name__ == '__main__':
    n = 5
    max_delay = 9

    print(measure_time(n, max_delay))
