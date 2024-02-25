def more_boar(player_score, opponent_score):
    """
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
    "*** YOUR CODE HERE ***"
    
    # Init parameters 
    player_first = player_score
    opponent_first = opponent_score
    player_second, opponent_second = 0, 0

    # if anyone's score < 10
    if player_score < 10:
        player_first = 0
        player_second = player_score
    if opponent_score < 10:
        opponent_first = 0
        opponent_second = opponent_score

    # other cases
    while player_first > 10:
        player_second = player_first % 10
        player_first //= 10
    while opponent_first > 10:
        opponent_second = opponent_first % 10
        opponent_first //= 10
        
    return True if player_first < opponent_first and player_second < opponent_second else False
    # END PROBLEM 4


def announce_highest(who, last_score=0, running_high=0):
    """Return a commentary function that announces when WHO's score
    increases by more than ever before in the game.

    NOTE: the following game is not possible under the rules, it's just
    an example for the sake of the doctest

    >>> f0 = announce_highest(1) # Only announce Player 1 score gains
    >>> f1 = f0(12, 0)
    >>> f2 = f1(12, 9)
    Player 1 has reached a new maximum point gain. 9 point(s)!
    >>> f3 = f2(20, 9)
    >>> f4 = f3(20, 30)
    Player 1 has reached a new maximum point gain. 21 point(s)!
    >>> f5 = f4(20, 47) # Player 1 gets 17 points; not enough for a new high
    >>> f6 = f5(21, 47)
    >>> f7 = f6(21, 77)
    Player 1 has reached a new maximum point gain. 30 point(s)!
    """
    assert who == 0 or who == 1, 'The who argument should indicate a player.'
    # BEGIN PROBLEM 7
    "*** YOUR CODE HERE ***"
    def f(score0, score1):
        highest = running_high
        last = last_score
        score = score0 if who == 0 else score1  # 选择分数
        s = score - last    # 当前回合和上一回合的分数差
        if s > highest: # 如果获得历史最高分
            print("Player", who, "has reached a new maximum point gain.", s, "point(s)!")
            highest = s # 更新历史最高分
        last = score    # 更新上一回合分数
        return announce_highest(who, last_score=last, running_high=highest)
    return f


def more_boar_strategy(score, opponent_score, cutoff=8, num_rolls=6):
    """This strategy rolls 0 dice when it triggers an extra turn. It also
    rolls 0 dice if it gives at least CUTOFF points and does not give an extra turn.
    Otherwise, it rolls NUM_ROLLS.
    """
    # BEGIN PROBLEM 11
    former_score = score
    pig_socre = piggy_points(opponent_score)
    score += pig_socre
    while more_boar(score, opponent_score):
        cutoff -= pig_socre
        if piggypoints_strategy(score, opponent_score, cutoff, num_rolls) == 0:
            return 0
        score += pig_socre
    return num_rolls
    # END PROBLEM 11


def piggypoints_strategy(score, opponent_score, cutoff=8, num_rolls=6):
    """This strategy rolls 0 dice if that gives at least CUTOFF points, and
    rolls NUM_ROLLS otherwise.
    """
    # BEGIN PROBLEM 10
    if piggy_points(opponent_score) >= cutoff:
        return 0
    return num_rolls
    # END PROBLEM 10


def piggy_points(score):
    """Return the points scored from rolling 0 dice.

    score:  The opponent's current score.
    """
    assert type(score) is int
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"
    score = score ** 2
    minimum = 10
    while score > 0:
        last = score % 10
        if last < minimum:
            minimum = last
        score //= 10
    return 3 if minimum == 10 else 3 + minimum
    # END PROBLEM 2


if __name__ == '__main__':
    more_boar_strategy(17, 36, cutoff=100, num_rolls=6)