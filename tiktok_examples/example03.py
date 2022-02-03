#!/usr/bin/python

import time


def method01(inputs):
    """ Build a list of sets - functioning as "blocks" of time in the calendar.
    Each item in the list represents the rooms. The numbers represent the blocks of time within the room reserved.

    As each event is added to the calendar, I use a binary operator '&' to determine if the room and the event have
    overlapping time. If there isn't any overlap, then I add the event to the room. ```update(event)```

    If the event conflicts/overlaps with all the rooms, then a new room and the event is added. ```append(event)```

    Args:
        inputs(list):  The list of meeting start/end times. e.g [[7,10],[2,4],...]

    Returns:
        int: the number of rooms needed to accommodate the given (inputs) meetings
    """
    final_list = [set()]
    for i in inputs:
        found = False
        event = set(range(i[0], i[1]+1))
        for f in final_list:
            if not (event & f):
                f.update(event)
                found = True
                break
        if not found:
            final_list.append(event)
    return len(final_list)


def run_methods(inputs):
    for func in [method01]:
        start = time.process_time()
        final = func(inputs=inputs)
        proc_time = time.process_time() - start
        print("[{}] Run Time: {:.7f} seconds".format(func.__name__, proc_time))
        print("\t'{}' Output: {}".format(inputs, final))


if __name__ == '__main__':
    # inputs = [[4, 6], [2, 3], [5, 6]]
    inputs = [[7, 10], [2, 4]]
    run_methods(inputs)
