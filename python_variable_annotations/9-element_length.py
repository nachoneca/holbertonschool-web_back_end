#!/usr/bin/env python3
"""Takes an iterable lst and return a list of each secuence and its lenth"""

from typing import List, Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Takes an iterable lst and return a list of each secuence and its lenth"""
    return [(i, len(i)) for i in lst]
