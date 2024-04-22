#!/usr/bin/env python3
"""
script for task 1
"""
import asyncio
from typing import List


wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    return the list of all the delays
    """
    tasks = list(map(lambda _: wait_random(max_delay), range(n)))
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
