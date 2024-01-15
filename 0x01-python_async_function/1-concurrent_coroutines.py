#!/usr/bin/env python3

"""Async gather"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Run multiple couroutines together
    Args:
        n (int): defines number of couroutines to spawn
        max_delay (int): maximum delay of couroutine
    """
    res = []
    for cor in asyncio.as_completed([wait_random(max_delay)
                                     for _ in range(n)]):
        res.append(await cor)
    return res
