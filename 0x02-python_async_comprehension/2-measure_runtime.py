#!/usr/bin/env python3
"""
script for tas k2
"""
import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    coroutine that will execute async_comprehension four times in paralle
    """
    starting = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    ending = time.time()
    return ending - starting
