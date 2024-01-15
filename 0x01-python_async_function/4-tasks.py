#!/usr/bin/env python3
"""task_wait_random"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Run multiple couroutines together
    Args:
        n (int): defines number of couroutines to spawn
        max_delay (int): maximum delay of couroutine
    """
    res = []
    for cor in asyncio.as_completed([task_wait_random(max_delay)
                                     for _ in range(n)]):
        res.append(await cor)
    return res
