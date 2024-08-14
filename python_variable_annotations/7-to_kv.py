#!/usr/bin/env python3
from typing import Union, Tuple
"""Takes str and float and return tuple of str and float^2"""


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Takes str and float and return tuple of str and float^2"""
    return tuple(k, v * 2)

