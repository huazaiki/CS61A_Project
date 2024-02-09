def fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def find_zero(lowest, highest, func):
    """Return a value b such that LOWEST <= v <= HIGHEST and
    FUNC(v) == 0, or None if there is no such value.
    Assumes that FUNC is a non-decreasing function from integers
    to integers (that is, if a < b, then FUNC(a) <= FUNC(b))."""
    if lowest > highest:
        return None
    elif func(lowest) == 0:
        return lowest
    else:
        return find_zero(lowest + 1, highest, func)


def find_zero_v2(lowest, highest, func):
    """find_zero's optimized version"""
    if lowest > highest:
        return None
    middle = (lowest + highest) // 2
    if func(middle) == 0:
        return middle
    elif func(middle) < 0:
        return find_zero_v2(middle + 1, highest, func)
    else:
        return find_zero_v2(lowest, middle - 1, func)


def is_a_zero(lowest, highest, func):
    """Return a value b such that LOWEST <= v <= HIGHEST and
    FUNC(v) == 0, or None if there is no such value.
    Assumes that FUNC is a non-decreasing function from integers
    to integers (that is, if a < b, then FUNC(a) <= FUNC(b))."""

    middle = (lowest + highest) // 2

    return lowest <= highest \
        and (func(middle) == 0
             or (func(middle) < 0 and is_a_zero(middle + 1, highest, func))
             or (func(middle) > 0 and is_a_zero(lowest, middle - 1, func)))


def is_path(blocked, x0, y0):
    """True if there is a path of squares from (X0, Y0) to some
    square (x1, 0) such that all squares on the path (including first and
    last) are unoccupied. BLOCKED is a predicate such that BLOCKED(x, y)
    is true if the grid square at (x, y) is occupied or off the edge.
    Each step of a path goes down one row and 1 or 0 columns left or right"""
    if blocked(x0, y0):
        return False
    elif y0 == 0:
        return True
    else:
        return is_path(blocked, x0 - 1, y0 - 1) \
            or is_path(blocked, x0, y0 - 1) \
            or is_path(blocked, x0 + 1, y0 - 1)


def num_partition(n, k):
    """Number of distinct ways to express N as a sum of positive
    integers each of which is <= K, where K > 0. (The empty sum is 0.)"""
    if n < 0:
        return 0
    elif k == 1:
        return 1
    else:
        return num_partition(n - k, k) + num_partition(n, k - 1)


def keep_ints(cond, n):
    """Print out all integers 1..i..n where cond(i) is true
    >>> def is_even(x):
    ...     # Even numbers have remainder 0 when divided by 2.
    ...     return x % 2 == 0
    >>> keep_ints(is_even, 5)
    2
    4
    """
    "*** YOUR CODE HERE ***"
    i = 1
    while i <= n:
        if cond(i):
            print(i)
        i += 1
    

def is_even(x):
    return x % 2 == 0


def make_keeper(n):
    """Returns a function which takes one parameter cond and prints out all integers 1..i..n where calling cond(i) returns True.
        >>> def is_even(x):
        ...     # Even numbers have remainder 0 when divided by 2.
        ...     return x % 2 == 0
        >>> make_keeper(5)(is_even)
        2
        4
    """
    "*** YOUR CODE HERE ***"
    def f(cond):
        i = 1
        while i <= n:
            if cond(i):
                print(i)
            i += 1
    return f


def curry2_lambda(func):
    return lambda x: lambda y: func(x, y)


def make_keeper_redux(n):
    """Returns a function. This function takes one parameter <cond> and prints out
       all integers 1..i..n where calling cond(i) returns True. The returned
       function returns another function with the exact same behavior.

        >>> def multiple_of_4(x):
        ...     return x % 4 == 0
        >>> def ends_with_1(x):
        ...     return x % 10 == 1
        >>> k = make_keeper_redux(11)(multiple_of_4)
        4
        8
        >>> k = k(ends_with_1)
        1
        11
        >>> k
        <function do_keep>
    """
    # Paste your code for make_keeper here!
    def f(cond):
        i = 1
        while i <= n:
            if cond(i):
                print(i)
            i += 1
        return f
    return f


def ends_with_1(x):
    return x % 10 == 1


def print_delayed(x):
    """Return a new function. This new function, when called, will print out x and return another function with the same behavior.
    >>> f = print_delayed(1)
    >>> f = f(2)
    1
    >>> f = f(3)
    2
    >>> f = f(4)(5)
    3
    4
    >>> f("hi") # a function is returned
    5
    <function delay_print>
    """
    def delay_print(y):
        print(x)
        return print_delayed(y)
    return delay_print


def print_n(n):
    """
    >>> f = print_n(2)
    >>> f = f("hi")
    hi
    >>> f = f("hello")
    hello
    >>> f = f("bye")
    done
    >>> g = print_n(1)
    >>> g("first")("second")("third")
    first
    done
    done
    <function inner_print>
    """
    def inner_print(x):
        if n <= 0:
            print("done")
        else:
            print(x)
        return print_n(n-1)
    return inner_print

if __name__ == '__main__':
    # f = print_n(2)
    # f = f("hi")
    # f = f("hello")
    # f = f("bye")
    g = print_n(1)
    g = g("first")("second")("third")
    print("DEBUG: g = ", g)