#!/usr/bin/env python3
"""wait_random n times and save delay into a list"""


from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """wait_random n times and save delay into a list"""
    del_list = []
    for x in range(n):
        diley = await wait_random(max_delay)
        del_list.append(diley)
    return del_list