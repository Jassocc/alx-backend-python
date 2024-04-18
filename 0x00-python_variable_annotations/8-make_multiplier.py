#!/usr/bin/env python3
"""
script for task 8
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    returns a function that multiplies a float by multiplier.
    """
    return lambda x: x * multiplier
