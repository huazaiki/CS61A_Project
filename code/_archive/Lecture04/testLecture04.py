from math import sin, cos, pi


# 计算自然和
def sum_naturals(n):
    total, k = 0, 1
    while k <= n:
        total, k = total + k, k + 1
    return total


# 计算立方和
def sum_cubes(n):
    total, k = 0, 1
    while k <= n:
        total, k = total + pow(k, 3), k + 1
    return total


# 计算一个有规律的式子，它会向pi收敛
def pi_sum(n):
    total, k = 0, 1
    while k <= n:
        total, k = total + 8 / (k * (k + 2)), k + 4
    return total


# 将上面三个函数抽象出来的高阶函数
def summation(n, strategy, next):
    total, k = 0, 1
    while k <= n:
        total, k = total + strategy(k), next(k)
    return total


###############################################
#   计算立方和（加强版）
###############################################


# 处理自然数递增
def successor(k):
    return k + 1


# 策略：立方求和
def cube(k):
    return pow(k, 3)


# 计算立方和（加强版）
def sum_cubes_plus(n):
    return summation(n, cube, successor)


###############################################
#   计算自然和（加强版）
###############################################


# 策略：自然求和
def identify(k):
    return k


# 计算自然和（加强版）
def sum_natural_plus(n):
    return summation(n, identify, successor)


###############################################
#   计算pi（加强版）
###############################################


# 策略：收敛pi
def pi_term(k):
    denominator = k * (k + 2)
    return 8 / denominator


def pi_next(k):
    return k + 4


def pi_sum_plus(n):
    return summation(n, pi_term, pi_next)


###############################################
#   迭代改进算法
###############################################

def average(x, y):
    return (x + y) / 2


def sqrt_update(guess, x):
    return average(guess, x / guess)


def square(k):
    """返回一个数的平方"""
    return k * k


def compose1(f, g):
    def h(x):
        return f(g(x))

    return h


###############################################
#   牛顿法求根
###############################################

def square_root(a):
    return find_root(lambda x: square(x) - a)


def logarithm(a, base=2):
    return find_root(lambda x: pow(base, x) - a)


def approx_derivative(f, x, delta=1e-5):
    """近似求解某一点导数"""
    df = f(x + delta) - f(x)
    return df / delta


def iter_improve(update, test, guess=1):
    """迭代改进算法模板"""
    while not test(guess):
        guess = update(guess)
    return guess


def newton_update(f):
    """牛顿迭代算法"""

    def update(x):
        return x - f(x) / approx_derivative(f, x)

    return update


def approx_eq(x, y, tolerance=1e-5):
    """近似相等的测试方法"""
    return abs(x - y) < tolerance


def find_root(f, initial_guess=10):
    """寻根函数，应用牛顿法"""

    def test(x):
        return approx_eq(f(x), 0)

    return iter_improve(newton_update(f), test, initial_guess)


##############################

def combine_funcs(op):
    """combine_funcs(lambda x, y: x + y)"""
    def combine(f, g):

        def val(x):
            return op(f(x), g(x))

        return val

    return combine


################################
#   challenge
################################

def f():
    return 0


def g():
    print(f())


def h():
    def f():
        return 1
    g()


if __name__ == '__main__':
    # print(sum_naturals(100))
    # print(sum_cubes(100))
    # print(pi_sum(100))
    # print(sum_cubes_plus(3))
    # print(sum_natural_plus(100))
    # print(pi_sum_plus(100))
    # add_one_and_square = compose1(square, successor)
    # print(add_one_and_square(12))
    # print(square_root(16))
    # print(logarithm(32, 2))
    # add_func = combine_funcs(lambda x, y: x + y)
    # h = add_func(sin, cos)
    # print(h(pi / 4))
    h()