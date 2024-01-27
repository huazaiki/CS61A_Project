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


def f(x):
    return x
def g(x, y):
    if x(y):
        return not y
    return y


def ordered_digits(x):
    """
    >>> ordered_digits(5)
    True
    >>> ordered_digits(11)
    True
    >>> ordered_digits(127)
    True
    >>> ordered_digits(1357)
    True
    >>> ordered_digits(21)
    False
    >>> result = ordered_digits(1375) # Return, don't print
    >>> result
    False
    """

    digits = [int(digit) for digit in str(x)]
    return all(digits[i] <= digits[i + 1] for i in range(len(digits) - 1))


def rect(area, perimeter):
    """Return the longest side of a rectangle with area and perimeter that has integer sides.
    >>> rect(10, 14) # A 2 x 5 rectangle
    5
    >>> rect(5, 12) # A 1 x 5 rectangle
    5
    >>> rect(25, 20) # A 5 x 5 rectangle
    5
    >>> rect(25, 25) # A 2.5 x 10 rectangle doesn't count because sides are not integers
    False
    >>> rect(25, 29) # A 2 x 12.5 rectangle doesn't count because sides are not integers
    False
    >>> rect(100, 50) # A 5 x 20 rectangle
    20
    """
    side = 1
    while side * side <= area:
        other = round((perimeter - 2 * side) / 2)
        if side * other == area:
            return max(side, other)
        side = side + 1
    return False



if __name__ == '__main__':

    # print(False or 0)
    # print(special_case())
    # print(just_in_case())
    # print(case_in_point())
    # square(so_slow(5))
    # print(is_prime(7))
    # fizzbuzz(16)
    # file = open('E:/application/PyCharm Community Edition 2023.3.2/plugins/python-ce/helpers/pycharm/docrunner.py', 'r')
    # text = file.read()
    # print(text)
    # print(not 3)
    # x = 3
    # x = g(f, x)
    # f = g(f, 0)
    # print(f)
    print(rect(10, 14))