#!/usr/bin/env python3
"""type checking with mypy"""
from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """return a list of int"""
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array: Tuple = (12, 72, 91)

zoom_2x: List[int] = zoom_array(array)

zoom_3x: List[int] = zoom_array(array, 3)
