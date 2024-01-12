#!/usr/bin/env python3
"""tuple and str"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return tuple of value"""
    return (k, v ** 2)
