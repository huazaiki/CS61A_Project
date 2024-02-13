def matches(a, b):
    """Return the number of values k such that A[k] == B[k].
    >>> matches([1, 2, 3, 4, 5], [3, 2, 3, 0, 5])
    3
    >>> matches("abdomens", "indolence")
    4
    >>> matches("abcd", "dcba")
    0
    >>> matches("abcde", "edcba")
    1
    >>> matches("abcde", "edc")
    1
    """
    return sum(a[x] == b[x] for x in range(min(len(a), len(b))))


def triangle(n):
    """Assuming N >= 0, return the list consisting of N lists:
    [1], [1, 2], [1, 2, 3], ... [1, 2, ... N].
    >>> triangle(0)
    []
    >>> triangle(1)
    [[1]]
    >>> triangle(5)
    [[1], [1, 2], [1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 4, 5]]
    """
    return [list(range(1, x + 1)) for x in range(1, n + 1)]


if __name__ == '__main__':
    import doctest
    doctest.testmod()