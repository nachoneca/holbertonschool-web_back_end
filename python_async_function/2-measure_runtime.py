#!/usr/bin/env python3
"""takes n coroutines and max delay is the time it will sleep
return time of each coroutine"""


import time
import asyncio
import random

wait_random = __import__('0-basic_async_syntax').wait_random
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """takes n coroutines and max delay is the time it will sleep
    return time of each coroutine"""
    start_time = time.perf_counter() 
    asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter()
    total_time = end_time - start_time
    return total_time / n
