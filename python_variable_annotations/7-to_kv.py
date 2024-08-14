#!/usr/bin/env python3
"""Takes str and float and return tuple of str and float^2"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Takes str and float and return tuple of str and float^2"""
    return (k, v ** 2)
