#!/usr/bin/env python3
"""Saves corutines in tasks, 
    and waits every result as finished and save
    it in a list called delays"""
from typing import List
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Saves corutines in tasks, 
    and waits every result as finished and save
    it in a list called delays"""
    
    #tasks = [wait_random(max_delay) for _ in range(n)]
    #return [await task for task in asyncio.as_completed(tasks)]


   
    # return await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))

    asyncr = [wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(asyncr)]
    