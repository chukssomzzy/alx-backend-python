#!/usr/bin/env python3

"""Random waiting couroutine"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Wait for random time from 0 - 10 and return
    waited time
    Args:
        max_dalay (int): integer maximum time to sleep
    Returns:
        the slept time
    """
    s = random.uniform(0, max_delay)
    await asyncio.sleep(s)
    return s
