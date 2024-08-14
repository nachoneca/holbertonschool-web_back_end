#!/usr/bin/env python3
"""Takes Float and return a Func that multipy float by another float"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Takes Float and return a Func that multipy float by another float"""
    def multi_function(num: float) -> float:
        return num * multiplier
    return multi_function
