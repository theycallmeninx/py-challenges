#!/usr/bin/python

import time


def method01(input):
    """ In this solution, I am using the native built-in function 'sorted'.
     The sorted method uses the 'key' argument to sort based on a
    given criteria. In this case, it is a lambda checking if the value is a 0.

    BigO Notation - O(N)

    Args:
        input(list): a list of numbers to filter on

    Returns:
            list: a sorted list of number with zeroes to the back
    """
    return sorted(input, key=lambda x: x == 0)


def method02(input):
    """ In this solution, I am using the filter built-in python function to sift
    out the values of the incoming list:
        1. filter out non-zeroes
        2. filter out zeroes

    BigO Notation - O(N*2)

    Args:
        input(list): a list of numbers to filter on

    Returns:
            list: a sorted list of number with zeroes to the back
    """
    zeroes = list(filter((lambda x: x == 0), input))
    filtered = list(filter((lambda x: x != 0), input))
    return filtered + zeroes


def method03(input):
    """ In this solution, I take a hybrid approach to the built-in filter function
    and filter out the non-zeroes, find the size difference between the
    filtered and non-filtered, and just append a dynamic list of zeroes to the end.

    BigO - O(N) (plus some change)

    Args:
        input(list): a list of numbers to filter on

    Returns:
            list: a sorted list of number with zeroes to the back
    """
    filtered = list(filter((lambda x: x != 0), input))
    return filtered + [0]*(len(input)-len(filtered))


def method04(input):
    """ This solution uses an iterator to run through the list. While iterating it either:
        1. count/skip the zeroes.
        2. Add the digit to the final list
    Once through the list, extend the final list with a list of zeroes equal to the zero count.

    Args:
        input(list): a list of numbers to filter on

    Returns:
            list: a sorted list of number with zeroes to the back
    """
    filtered_list = []
    zero_count = 0
    input_iter = iter(input)
    current = next(input_iter, None)
    while current is not None:
        if current == 0:
            zero_count += 1
        else:
            filtered_list.append(current)
        current = next(input_iter, None)

    filtered_list.extend([0]*zero_count)
    return filtered_list


def method05(input):
    """ Uses iterators and recursion to run through the list and sorting non-zeroes to the top.

    Args:
        input(list): a list of numbers to filter on

    Returns:
            list: a sorted list of number with zeroes to the back
    """

    def recur(iter):
        try:
            value = next(iter)
        except StopIteration:
            value = None

        while value is not None:
            if value == 0:
                yield from recur(iter=iter)
                yield value
            else:
                yield value
            try:
                value = next(iter)
            except StopIteration:
                value = None

    return recur(iter(input))


def run_methods(input):
    for func in [method03, method04, method01, method02, method05]:
        start = time.process_time()
        final = func(input=input)
        proc_time = time.process_time() - start
        print("[{}] Run Time: {:.7f} seconds".format(func.__name__, proc_time))
        print("\tOutput: {}".format(list(final)))


if __name__ == '__main__':
    input = [0, 1, 0, 2, 3, 4, 5, 0, 12, 0, 18, 9, 0, 0, 4]
    run_methods(input)
