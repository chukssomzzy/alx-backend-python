#!/usr/bin/python3
"""Python Comprehension"""

from typing import List

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """Await a comprehension"""
    return [ran async for ran in async_generator()]
