#!/usr/bin/env python3

"""Create a task for the corutine of the function wait_random"""

import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Create a task for the corutine of the function wait_random"""
    return asyncio.create_task(wait_random(max_delay))
