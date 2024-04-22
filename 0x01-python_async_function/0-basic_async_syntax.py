#!/usr/bin/python3
"""
script for task 0
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    waits for a random delay between 0 and
    max_delay seconds and eventually returns it.
    """
    random_delay = random.random() * max_delay
    await asyncio.sleep(random_delay)
    return random_delay
