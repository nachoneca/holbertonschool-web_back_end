#!/usr/bin/env python3
"""Function that loops 10 time and sleep 1 sec asyncronusly,
then yield one number"""


import asyncio
import random


async def async_generator():
    """Function that loops 10 time and sleep 1 sec asyncronusly,
then yield one number"""
    for loop in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
