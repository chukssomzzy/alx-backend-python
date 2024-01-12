#!/usr/bin/env python3
"""type checking with mypy"""
from typing import List


def zoom_array(lst: List[int], factor: int = 2) -> List[int]:
    """return a list of int"""
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array: List[int] = [12, 72, 91]

zoom_2x: List[int] = zoom_array(array)

zoom_3x: List[int] = zoom_array(array, 3)
