#!/usr/bin/env python3
"""Annotate the below function"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """returns a list of tuple of sequence and int"""
    return [(i, len(i)) for i in lst]
