#! python


def is_curzon(num: int) -> bool:
    """ Identifies if a number is a curzon number.

    Notes:


    Args:
        num: The number to check
    """
    expo = (2 << (num-1)) + 1
    prod = 2 * num + 1
    return not (expo % prod)
