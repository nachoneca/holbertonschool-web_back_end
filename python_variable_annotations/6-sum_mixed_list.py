#!/usr/bin/env python3
"""Sum list of floats and ints"""


from typing import List, Union



def sum_mixed_list(mxd_list: List[Union[float, int]]) -> float:
    """Sum list of floats and ints"""
    return float(sum(mxd_list))
