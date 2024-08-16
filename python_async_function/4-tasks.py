#!/usr/bin/env python3
"""Creates a list of corutines(tasks) and save them
when they are completed into a list in 
that way it will be sorted atomatically"""


import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Creates a list of corutines(tasks) and save them
    when they are completed into a list in 
    that way it will be sorted atomatically"""
    tasks = [task_wait_random(max_delay)for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
