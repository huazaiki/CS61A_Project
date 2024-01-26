def wears_jacket_with_if(temp, raining):
    """
    >>> wears_jacket_with_if(90, False)
    False
    >>> wears_jacket_with_if(40, False)
    True
    >>> wears_jacket_with_if(100, True)
    True
    """
    # return temp < 60 or raining
    if temp < 60:
        return True
    elif raining:
        return True
    else:
        return False


def special_case():
    x = 10
    if x > 0:
        x += 2
    elif x < 13:
        x += 3
    elif x % 2 == 1:
        x += 4
    return x


def just_in_case():
    x = 10
    if x > 0:
        x += 2
    if x < 13:
        x += 3
    if x % 2 == 1:
        x += 4
    return x


def case_in_point():
    x = 10
    if x > 0:
        return x + 2
    if x < 13:
        return x + 3
    if x % 2 == 1:
        return x + 4
    return x


def square(x):
    print("here!")
    return x * x


def so_slow(num):
    x = num
    while x > 0:
        x = x - 1
        print("DEBUG: x = ", x)
    return x / 0


def is_prime(n):
    m = n - 1
    while m > 1:
        if n % m == 0:
            return False
        m -= 1
    return True


def fizzbuzz(n):
    """
    >>> result = fizzbuzz(16)
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    16
    >>> result == None
    True
    """
    count = 1
    while count <= n:
        if count % 3 == 0 and count % 5 == 0:
            print("fizzbuzz")
        elif count % 3 == 0:
            print("fizz")
        elif count % 5 == 0:
            print("buzz")
        else:
            print(count)
        count += 1


if __name__ == '__main__':

    # print(False or 0)
    # print(special_case())
    # print(just_in_case())
    # print(case_in_point())
    # square(so_slow(5))
    # print(is_prime(7))
    fizzbuzz(16)
    # file = open('E:/application/PyCharm Community Edition 2023.3.2/plugins/python-ce/helpers/pycharm/docrunner.py', 'r')
    # text = file.read()
    # print(text)