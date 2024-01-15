#!/usr/bin/env python3

"""
Author: Bradley Dillion Gilden
Date: 15-01-2024
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """returns an asyncio task created from a wait_random method call"""
    return asyncio.create_task(wait_random(max_delay))
