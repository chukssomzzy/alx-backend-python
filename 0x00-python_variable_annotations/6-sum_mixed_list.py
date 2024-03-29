#!/usr/bin/env python3
"""Sum mixed list"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """sum mixture of int and float and return a float"""
    return sum(float(n) for n in mxd_list)
