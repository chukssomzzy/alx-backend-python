#!/usr/bin/env python3
"""Add type annotation to function"""


from typing import Any, Mapping, TypeVar, Union


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[None, T]) -> Union[Any, T]:
    if key in dct:
        return dct[key]
    else:
        return default
