#!/usr/bin/env python3
"""Saves corutines in tasks, 
    and waits every result as finished and save
    it in a list called delays"""
import asyncio
from typing import List
import heapq

wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """Saves coroutines in tasks,
    and waits every result as finished and saves
    it in a list called delays in ascending order"""
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = []
    
    # Use a heap to maintain order while inserting results
    for task in asyncio.as_completed(tasks):
        delay = await task
        heapq.heappush(delays, delay)  # Maintain the list in ascending order
    
    return delays