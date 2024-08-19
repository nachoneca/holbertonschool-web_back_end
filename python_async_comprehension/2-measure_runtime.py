#!/usr/bin/env python3
"""Gather all task and run them in parallel,
    is not the same as 'asyncio.create_task' that
    take all tasks and run them asyncronically but doesnt
    wait one to start the other. Finally return the time calculated
    when the main thread started"""

import time
import asyncio


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Gather all task and run them in parallel,
    is not the same as 'asyncio.create_task' that
    take all tasks and run them asyncronically but doesnt
    wait one to start the other. Finally return the time calculated
    when the main thread started"""
    start_time = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.perf_counter()
    return end_time - start_time
