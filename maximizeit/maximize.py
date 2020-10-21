#! python

from collections import namedtuple

PARAMS = namedtuple("params", "line_count modulo")

MIN_LINE_COUNT = 1
MAX_LINE_COUNT = 7

MIN_MODULO = 1
MAX_MODULO = 1000

MIN_LINE_VALUES = 1
MAX_LINE_VALUES = 7

MIN_MAGNITUDE = 1
MAX_MAGNITUDE = 1000000000


def _build_recursive_sums(lines, values=None):
    """ recursively loop through each list of each line to build a list of integers.

    Examples:
         lines = [[1], [2,3], [4,5]] -> [[1,2,4], [1,2,5], [1,3,4], [1,3,5]]

    Args:
        lines: nested list of integer lists
        values: the values already collected from higher up the tree

    Yields:
        list: the integers of each list that was
    """
    if values is None:
        values = []
    for num in lines[0]:
        if len(lines) > 1:
            yield from _build_recursive_sums(lines[1:], values + [num])
        else:
            yield values + [num]


def _find_max_modulo(lines: list, modulo: int) -> int:
    """ Finds the maximum modulo value from the provided list of lines.

    Args:
        lines: A nested list of integer lists to find the max modulo value

    Returns:
        int: the max modulo value
    """
    lookup = {}
    max_modulo = 0
    for iter_sum in _build_recursive_sums(lines=lines):
        total = sum(iter_sum)
        if total not in lookup:
            calc_modulo = total % modulo
            lookup[total] = calc_modulo
            if calc_modulo > max_modulo:
                max_modulo = calc_modulo
    return max_modulo


def _line_is_valid(line):
    """ Validates that the user-input line is consistent with the constraints and itself

    Args:
        line: the list of values to check

    Returns:
        None
    """
    if not (MIN_LINE_VALUES <= line[0] <= MAX_LINE_VALUES):
        print("Line elements {} (Ni) falls outside length constraint. ({}-{})".format(line[0], MIN_LINE_VALUES, MAX_LINE_VALUES))
    if line[0] != len(line[1:]):
        print("Line (Ni) value does not match user input. {}:{}".format(line[0], line[1:]))
        exit(1)
    for value in line[1:]:
        if not (MIN_MAGNITUDE <= value <= MAX_MAGNITUDE):
            print("Value {} falls outside magnitude constraint ({}-{}).".format(value, MIN_MAGNITUDE, MAX_MAGNITUDE))
            exit(1)


def _process_input(lines: str):
    """ Take the string-provided user input and parse it into a python list object of ints

    Args:
        lines: the user input to parse

    Returns:
        list: the input as a python object
    """
    split_input = [[int(value) for value in line.split(sep=' ')] for line in lines.splitlines(keepends=False)]
    return split_input


def _validate_modulo(modulo: int):
    """ Verifies the modulo value being used falls within the constraints.

    Args:
        modulo: the value to validate

    Returns:
        None
    """
    if not (MIN_MODULO <= modulo <= MAX_MODULO):
        print("Modulo value (M) must be {}-{}. User entered {}".format(MIN_MODULO, MAX_MODULO, modulo))
        exit(1)


def _validate_line_counts(num_lines, total_lines):
    """ Validate that the line count from the user matches what was actually input by the user.

    Args:
        num_lines: the value provided in the first string
        total_lines: the length of the following list's values

    Returns:
        None
    """
    if not (MIN_LINE_COUNT <= num_lines <= MAX_LINE_COUNT):
        print("List value (K) must be {}-{}. User entered {}".format(MIN_LINE_COUNT, MAX_LINE_COUNT, num_lines))
        exit(1)
    if num_lines != total_lines:
        print("List value (K) does not match user input. {} != {}".format(num_lines, total_lines))
        exit(1)


def _parse_params(line: list):
    """ Parses an input line for the expected parameter values

    Args:
        line: the list of values that represent the K number of lines being processed and the M modulo value to use

    Returns:
        PARAMS: the first line parsed out
    """
    try:
        params = PARAMS(*line)
    except TypeError:
        print("Input Error. First input line expects 2 values. {} provided".format(len(line)))
        exit(1)
    else:
        return params


def _collect_values_to_maximize(lines: list):
    """ Square the values to be maximized.

    Args:
        lines: nested list of integer lists

    Returns:
        list
    """
    values = []
    for line in lines:
        val_list = []
        # the first value of each line is the number of elements in the list. It can be skipped.
        for value in line[1:]:
            val_list.append(int(value) ** 2)
        values.append(val_list)
    return values


def _collect_user_input():
    """ Prompt the user for the input values

    Examples:
        example1 =
            3 1000
            2 5 4
            3 7 8 9
            5 5 7 8 9 10

    Returns:
        str
    """
    user_input = []
    while True:
        try:
            ui = input()
        except EOFError:
            break
        else:
            user_input.append(ui.strip())
    return "\n".join(user_input)


def maximize():
    """ The Maximize Entry-Point

    Returns:
        None
    """
    user_input = _collect_user_input()
    processed_input = _process_input(user_input)
    params = _parse_params(processed_input.pop(0))
    _validate_modulo(params.modulo)
    _validate_line_counts(params.line_count, len(processed_input))
    for line in processed_input:
        _line_is_valid(line)
    values = _collect_values_to_maximize(processed_input)
    max_modulo = _find_max_modulo(values, modulo=params.modulo)
    print(max_modulo)


maximize()
