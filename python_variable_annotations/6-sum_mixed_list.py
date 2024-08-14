#!/usr/bin/env python3
"""Sum list of floats and ints"""
from typing import List, Union



def sum_list(input_list: List[Union[float, int]]) -> float:
    """Sum list of floats and ints"""
    return float(sum(input_list))
