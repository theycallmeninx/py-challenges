#! python


def additive_persistence(n):
    final_count = 0
    while True:
        if len(str(n)) == 1:
            return final_count
        else:
            n = sum(map(int, str(n)[:]))
            final_count += 1


def multiplicative_persistence(n):
    final_count = 0
    while True:
        if len(str(n)) == 1:
            return final_count
        else:
            _total = 1
            for value in map(int, str(n)[:]):
                _total *= value
            n = _total
            final_count += 1
