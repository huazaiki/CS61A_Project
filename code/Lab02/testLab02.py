def make_adder(n):
    return lambda k: k + n


a = lambda x: x * 2 + 1


def b(b, x):
    return b(x + a(x))


if __name__ == '__main__':
    # n = 9  # Global
    # add_ten = make_adder(n + 1)  # A func that: return 10 + x
    # result = add_ten(n)  # 将 n 填补在 上面的 x 处
    # print(result)
    x = 3
    print(b(a, x))
