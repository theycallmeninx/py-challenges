#! python
from typing import List

splitter = lambda x: map(int, str(x)[:])


def sum_dig_prod(*args: List[int]) -> None:
    """ Takes in a number of integers, adds them together, and then split and multiplies each digit until
    there's only one digit left.

    Args:
        *args: the numbers to sum, then multiply
    """
    _total = sum(args)
    while True:
        if len(str(_total)) == 1:
            return _total
        else:
            _subtotal = 1
            for value in splitter(_total):
                _subtotal *= value
            _total = _subtotal