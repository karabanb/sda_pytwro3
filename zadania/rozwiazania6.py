
from typing import Union, Tuple


def foo3(*args: int, **kwargs: int):
    res = 1
    for value in kwargs.values():
        res = res * value
    return res, sum(args)


foo3(1, 2, 3, l=1, m='b')


def foo3(*args: int, **kwargs: int) -> Tuple[Union[str, int]]:
    res = 1
    for value in kwargs.values():
        res = res * value
    return res, sum(args)


foo3(1, 2, 3, l=1, m='b')


