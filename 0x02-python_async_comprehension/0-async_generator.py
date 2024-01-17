#!/usr/bin/python3
"""Async generator"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Async Generator"""
    for _ in range(10):
        await asyncio.sleep(1)
        i = random.uniform(0, 10)
        yield i
