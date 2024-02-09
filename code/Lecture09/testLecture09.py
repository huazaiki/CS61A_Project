def reverse_digits(n):
    """Assuming N >= 0 is an integer.  Return the number whose
    base-10 representation is the reverse of that of N.
    >>> reverse_digits(0)
    0
    >>> reverse_digits(1)
    1
    >>> reverse_digits(123)
    321
    >>> reverse_digits(10)
    1
    >>> reverse_digits(12321)
    12321
    >>> reverse_digits(2222222)
    2222222
    >>> reverse_digits(102)
    201
    """
    assert n >= 0 and type(n) is int
    if n < 10:
        return n
    return (n % 10) * 10 ** (num_digits(n) - 1) + reverse_digits(n // 10)


def num_digits(n):
    x_count = 1
    while n >= 10:
        x_count += 1
        n = n // 10
    return x_count


def interleave(a, b):
    """Assuming A and B are non-negative integers with the same 
    number of base-10 digits, return the number whose base-10 
    representation is the interleaving of A's and B's digits,
    starting with A.
    >>> interleave(1, 2)
    12
    >>> interleave(0, 1)
    1
    >>> interleave(1, 0)
    10
    >>> interleave(123,456)
    142536
    >>> interleave(111111, 222222)
    121212121212
    """
    if a <= 9:
        return a * 10 + b
    return interleave(a % 10, b % 10) + interleave(a // 10, b // 10) * 10 ** 2


if __name__ == '__main__':
    import doctest
    doctest.testmod()