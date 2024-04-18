#!/usr/bin/env python3
"""
script for task 10
"""
from typing import Union, Any, Sequence


def safe_first_element(lst: Sequence) -> Union[Any, None]:
    """
    task 10 script
    """
    if lst:
        return lst[0]
    else:
        return None
