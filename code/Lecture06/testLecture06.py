from operator import add


def sum_digits(n):
    """Return the sum of digits of positive integer n"""
    if n < 10:
        return n
    else:
        all_but_last, last = n // 10, n % 10
        return sum_digits(all_but_last) + last


def print_nums(n):
    print(n)

    def next_num(k):
        return print_nums(n + k)

    return next_num


def curry2(f):
    return lambda x: lambda y: f(x, y)


def sqrt_like(n):  # sqrt_like即功能抽象
    """Assuming x >= 0      <== Precondition前置条件
    Post condition后置条件 ==>    returns approximation to square root of x"""
    # Semantic specification语义规范


def sum_squares(N):
    """Return the sum of K**2 for K from 1 to N(inclusive)."""
    if N < 1:
        return 0
    else:
        return sum_squares(N - 1) + N**2


def fact_iter(n):
    """Return the factorial of n"""
    total, k = 1, 1
    while k <= n:
        total, k = total * k, k + 1
    return total


def fact(n):
    if n == 1:
        return 1
    else:
        return fact(n-1) * n


if __name__ == '__main__':
    print(fact(4))