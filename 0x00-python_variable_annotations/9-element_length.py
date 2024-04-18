#!/usr/bin/env python3
"""
script for task 9
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    function for annpotation
    """
    return [(i, len(i)) for i in lst]
