#! python

# converts the number to a string,
# then converts the string to slices,
# then converts the list of strings to ints
splitter = lambda x: map(int, str(x)[:])


def additive_persistence(n: int) -> None:
    """ Takes a number and counts the number of split and add iterations it takes to reach a single digit.

    Args:
        n: the number to split/add/iterate
    """
    final_count = 0
    while True:
        if len(str(n)) == 1:
            return final_count
        else:
            n = sum(splitter(n))
            final_count += 1


def multiplicative_persistence(n: int) -> None:
    """ Takes a number and counts the number of split and multiply iterations it takes to reach a single digit.

    Args:
        n: the number to split/multiply/iterate
    """
    final_count = 0
    while True:
        if len(str(n)) == 1:
            return final_count
        else:
            _total = 1
            for value in splitter(n):
                _total *= value
            n = _total
            final_count += 1
