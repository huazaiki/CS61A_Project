x = 1

def pair(a, b):
    def pair_func(which, v=None):
        nonlocal a, b
        if which == 0:
            return a
        elif which == 1:
            return b
        elif which == 2:
            a = v
        else:
            b = v
    return pair_func

def left(p):
    return p(0)

def right(p):
    return p(1)

if __name__ == '__main__':
    print("a ", (1, 2))
    a = pair(1, 2)
    b = pair(2, 1)
    # print("DEBUG: right(a) == 1 is ", right(a) == 1)
    print("DEBUG: left(a) == 1 is ", left(a) == 1)
    