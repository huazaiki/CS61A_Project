def piggy_points(score):
    """Return the points scored from rolling 0 dice.

    >>> piggy_points(4)
    4

    score:  The opponent's current score.
    """
    # BEGIN PROBLEM 2
    receive = score ** 2
    print("DEBUG: receive = ", receive)
    min_num = float('inf')
    count = 0
    tmp = receive
    if tmp == 0:
        min_num = 0
    else:
        while tmp >= 1:
            tmp //= 10
            count += 1
    # count = 数字长度
    while count > 0:
        num = receive // pow(10, count - 1)
        count -= 1
        if num < min_num:
            min_num = num
        receive = receive % pow(10, count)

    return int(3 + min_num)
    # END PROBLEM 2


def more_boar(player_score, opponent_score):
    """Return whether the player gets an extra turn.

    player_score:   The total score of the current player.
    opponent_score: The total score of the other player.

    >>> more_boar(21, 43)
    True
    >>> more_boar(22, 43)
    True
    >>> more_boar(43, 21)
    False
    >>> more_boar(12, 12)
    False
    >>> more_boar(7, 8)
    False
    """
    # BEGIN PROBLEM 4
    num1 = final_num(player_score)
    num2 = final_num(opponent_score)

    num1_prefix = num1 // 10
    print("DEBUG: num1_prefix = ", num1_prefix)
    num1_suffix = num1 % 10
    print("DEBUG: num1_suffix = ", num1_suffix)
    num2_prefix = num2 // 10
    print("DEBUG: num2_prefix = ", num2_prefix)
    num2_suffix = num2 % 10
    print("DEBUG: num2_suffix = ", num2_suffix)

    return num1_prefix < num2_prefix and num1_suffix < num2_suffix
    # END PROBLEM 4


def final_num(score):
    length = len(str(score))
    while length >= 2:
        score = score // pow(10, length - 2)
        length -= 1
    return score


if __name__ == '__main__':
    # print(piggy_points(0))
    print(more_boar(21, 43))
