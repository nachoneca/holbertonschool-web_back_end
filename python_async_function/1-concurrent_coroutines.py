#!/usr/bin/env python3

"""Execute n times the wait_random
function with the max_delay for arg
and return a list of those random numbers"""

import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Execute n times the wait_random
    function with the max_delay for arg
    and return a list of those random numbers"""
    random_list = []
    for times in range(n):
        delay = await wait_random(max_delay)
        random_list.append(delay)

    return sorted(random_list)
