def sum_digits(n):
    """Return the sum of the digits of positive integer n"""
    if n < 10:
        return n
    else:
        all_but_last, last = n // 10, n % 10
        return sum_digits(all_but_last) + last


def fact_iter(n):
    total, k = 1, 1
    while k <= n:
        total, k = total * k, k + 1
    return total


def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)


def is_even(n):
    if n == 0:
        return True
    else:
        return is_odd(n - 1)


def is_odd(n):
    if n == 0:
        return False
    else:
        return is_even(n - 1)


def cascade(n):
    """Print a cascade of prefixes of n."""
    if n < 10:
        print(n)
    else:
        print(n)
        cascade(n // 10)
        print(n)


def play_alice(n):
    if n == 0:
        print("Bob wins!")
    else:
        return play_bob(n - 1)


def play_bob(n):
    if n == 0:
        print("Alice wins!")
    elif is_even(n):
        return play_alice(n - 2)
    else:
        return play_alice(n - 1)


def fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def print_sums(n):
    print(n)

    def next_sum(k):
        return print_sums(n + k)

    return next_sum


from operator import add


def curry2(f):
    return lambda x: lambda y: f(x, y)


def curry2_1(f):
    return lambda x: lambda y: f(x, y)


def sum_squares(N):
    """Return The sum of K**2 for K from 1 to N(inclusive)"""
    if N < 1:
        return 0
    else:
        return N ** 2 + sum_squares(N - 1)


def f(n):
    def ff():
        return n
    return ff

if __name__ == '__main__':
    # print(sum_digits(99999))
    # print(fact_iter(4))
    # print(fact(4))
    # print(is_even(900))
    # cascade(2024)
    # play_alice(21)
    # n = 1
    # while n <= 100:
    #     play_alice(n)
    #     n += 1
    # # print(fib(6))
    # # This example shows us Partly instantiated
    # print(curry2(add)(30)(12))
    # print(curry2(add)(30))  # Prints a function value
    # print(curry2(add))  # Prints the function value!
    print(f(5)())
