#!/usr/bin/env python3

"""
Author: Bradley Dillion Gilden
Date: 16-01-2024
"""
from typing import List
import asyncio
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """collects numbers form async generator and returns them as a list"""
    return [num async for num in async_generator()]
