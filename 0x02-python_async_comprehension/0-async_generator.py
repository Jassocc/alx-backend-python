#!/usr/bin/env python3
"""
sxript for task 0
"""
import asyncio
import random


async def async_generator():
    """
    asynchronously wait 1 second
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
