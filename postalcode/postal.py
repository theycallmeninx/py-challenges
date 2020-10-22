#! python
import re


def regex_integer_in_range(user_value: str) -> bool:
    """ Match only integers range from 100000 to 999999 inclusive

    Args:
        user_value:

    Returns:

    """
    return bool(re.match(r"^[1-9][0-9]{5}$", user_value))


def regex_alternating_repetitive_digit_pair(user_value: str) -> bool:
    """ find alternating repetitive digits pairs in a given string.
    """
    return len(re.findall(r"(?=(\d)\d\1)", user_value)) < 2


while True:
    try:
        user_value = input()
    except EOFError:
        pass
    else:
        break


is_in_range = regex_integer_in_range(user_value=user_value)
is_non_repeating = regex_alternating_repetitive_digit_pair(user_value=user_value)
print((is_in_range & is_non_repeating), end="")
