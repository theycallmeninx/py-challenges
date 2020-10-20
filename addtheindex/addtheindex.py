#! python

from typing import List


def add_indexes(lst: List[int]) -> List[int]:
    """"""
    final = []
    for index, item in enumerate(lst):
        final.append(item + index)
    return final
