#!/usr/bin/env python3
"""Async func that iterates inside async_generator
and saves the float into a list"""


import asyncio
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Async func that iterates inside async_generator
and saves the float into a list"""
    return [x async for x in async_generator()]
    #result = []
    #async for x in async_generator():
        #result.append(x)
    #return result
