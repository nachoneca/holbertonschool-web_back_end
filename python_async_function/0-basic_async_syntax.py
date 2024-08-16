#!/usr/bin/env python3
"""Takes a num, awayst for num random and return delay"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Takes a num, awayst for num random and return delay"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay



"""Saves corutines in tasks, 
    and waits every result as finished and save
    it in a list called delays"""