import os
from typing import Union


def get_numeric_value(letter: str, opponent_val: Union[int, None] = None) -> int:
    if opponent_val is not None:
        # X = must lose
        # Y = must draw
        # Z = must win
        if letter.capitalize() == "Z":
            if opponent_val == 3:
                return 1
            else:
                return opponent_val + 1
        elif letter.capitalize() == "Y":
            return opponent_val
        elif letter.capitalize() == "X":
            if opponent_val == 1:
                return 3
            else:
                return opponent_val - 1

    if letter.capitalize() == "A" or letter.capitalize() == "X":
        return 1
    if letter.capitalize() == "B" or letter.capitalize() == "Y":
        return 2
    if letter.capitalize() == "C" or letter.capitalize() == "Z":
        return 3
    return 0


def score_it(opponent: str, me: str, part_two: bool = False) -> int:
    score: int = 0

    # A = Rock
    # B = Paper
    # C = Scissors

    # X = Rock
    # Y = Paper
    # Z = Scissors
    #    them me        me - them
    # win = 1 2         1
    # win = 2 3         1
    # win = 3 1         -2
    # loss = 1 3        2
    # loss = 2 1        -1
    # loss = 3 2        -1

    opponent_int = get_numeric_value(opponent)
    if part_two is False:
        me_int = get_numeric_value(me)
    else:
        me_int = get_numeric_value(me, opponent_int)

    draw_value: int = 3
    win_value: int = 6
    loss_value: int = 0

    if opponent_int == me_int:  # draw
        return draw_value + me_int
    elif me_int - opponent_int in [1, -2]:  # win
        return win_value + me_int
    elif me_int - opponent_int in [-1, 2]:  # loss
        return loss_value + me_int

    return score


def some_function(file_name: str = "input.txt", part_two: bool = False) -> int:
    return_me: int = 0
    directory = os.path.dirname(os.path.realpath(__file__))
    file = open(os.path.join(directory, file_name), "r")
    all_lines = file.readlines()

    strategy: list[tuple[str, str]] = []

    curr_game: int = 1
    curr_game_score: int = 0
    curr_total_score: int = 0
    for line in all_lines:
        values_only = line.strip("\n")
        val_list = values_only.split(" ")
        strategy.append((val_list[0], val_list[1]))

        curr_game_score = score_it(val_list[0], val_list[1], part_two)
        curr_total_score += curr_game_score
        print(f"game {curr_game}: score {curr_game_score}: total {curr_total_score}")
        curr_game += 1

    return_me = curr_total_score

    return return_me
