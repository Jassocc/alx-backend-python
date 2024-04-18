#!/usr/bin/env python3
"""
task 11 script
"""
from typing import Mapping, Any, TypeVar, Union


T = TypeVar('T')
Res = Union[Any, T]
Def = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    """
    script for tas k11
    """
    if key in dct:
        return dct[key]
    else:
        return default
