#!/usr/bin/env python3
"""Execute n times the wait_random
    function with the max_delay for arg
    and return a list of those random numbers"""


import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random
task_wait_random = __import__('3-task').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Execute n times the wait_random
    function with the max_delay for arg
    and return a list of those random numbers"""
    tasks = [asyncio.run(task_wait_random(max_delay))for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
