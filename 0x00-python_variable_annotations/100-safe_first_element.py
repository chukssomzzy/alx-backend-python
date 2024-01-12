#!/usr/bin/env python3
"""Correct dock typed annotation"""
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Correct duck type annotation"""
    if lst:
        return lst[0]
    else:
        return None
