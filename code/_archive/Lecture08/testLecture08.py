def remove_digit(n, digit):
    """Assuming N>=0, 0 <= DIGIT <= 9, return a number whose
    base-10 representation is the same as N, but with all instances of
    DIGIT removed. If all digits removed, return 0
    >>> remove_digit(123, 3)
    12
    >>> remove_digit(1234, 5)
    1234
    >>> remove_digit(1234, 1)
    234
    >>> remove_digit(111111, 1)
    0
    """
    if n == 0:
        return 0
    if n % 10 == digit:
        return remove_digit(n // 10, digit)
    return n % 10 + remove_digit(n // 10, digit) * 10


def invert(x):
    result = 1 / x  # Raises a ZeroDivisionError if x is 0
    print('Never printed if x is 0')
    return result


def invert_safe(x):
    try:
        return invert(x)
    except ZeroDivisionError as e:
        return str(e)



if __name__ == '__main__':
    # import doctest
    #
    # doctest.testmod()
    from math import sqrt
    a = lambda f, x: f(x)
    print("DEBUG: a() = ", a(sqrt, 2))