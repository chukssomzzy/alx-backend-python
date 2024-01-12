#!/usr/bin/env python3
"""Takes a list and return a float"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Return sum of float"""
    return sum(n for n in input_list)
