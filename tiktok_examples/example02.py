#! /usr/bin/python

"""
Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

Examples:
// s = "leetcode"
// return 0.

// s = "loveleetcode"
// return 2.

"""

import time


def method01(inputs):
    """ In this solution, I use a python set to collect the character list
    encountered during the search. This solution will loop through each
    character, and evaluate if its in the rest of the string. If so, its
    added to the the set - and any future repeat letters will not be evaluated again.

    Args:
        inputs(str): the characters to search through

    Returns:
            int: the index of the located character
    """
    tracker = set()
    for count, char in enumerate(inputs):
        if char not in tracker:
            if char in input[count+1:]:
                tracker.add(char)
            else:
                return count
    return -1


def run_methods(inputs):
    for func in [method01]:
        start = time.process_time()
        final = func(inputs=inputs)
        proc_time = time.process_time() - start
        print("[{}] Run Time: {:.7f} seconds".format(func.__name__, proc_time))
        print("\t'{}' Output: {}".format(inputs, final))


if __name__ == '__main__':
    for i in ['leetcode', 'loveleetcode', 'moonoomoon', 'monopoly']:
        run_methods(inputs=i)
