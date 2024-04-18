#!/usr/bin/env python3
"""
script for task 7
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    annotated as a float.
    """
    return (k, float(v * v))
