#!/usr/bin/env python3
"""function multipler"""
from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function multipler"""
    def _mul(n: float):
        """Multiply float by multiplier"""
        return n * multiplier
    return _mul
