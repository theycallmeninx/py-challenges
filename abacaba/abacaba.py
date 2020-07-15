#! python


def abacaba_pattern(n: int) -> str:
    """ Generate an abacaba pattern based on the incoming number.

    Args:
        n: the number of iterations to generate the pattern
    """
    CHAR_BUFFER = 65
    pattern = ""
    for iteration in range(CHAR_BUFFER, n+CHAR_BUFFER):
        pattern = "{}{}{}".format(pattern, chr(iteration), pattern)
    return pattern
