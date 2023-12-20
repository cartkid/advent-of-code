import os


def is_game_within_criteria(criteria: dict[str, int], dice_draws: list[str]) -> bool:
    for draw in dice_draws:
        draw = draw.strip()
        dice = draw.split(",")
        for di in dice:
            temp = di.split()
            count = int(temp[0])
            type = temp[1]
            if type in criteria:
                if count > criteria[type]:
                    return False
    return True


def get_power(dice_draws: list[str]) -> int:
    return_me: int = 0

    min_dict: dict[str, int] = {}
    min_dict["red"] = 0
    min_dict["green"] = 0
    min_dict["blue"] = 0

    for draw in dice_draws:
        draw = draw.strip()
        dice = draw.split(",")
        for di in dice:
            temp = di.split()
            count = int(temp[0])
            type = temp[1]
            if type in min_dict:
                if count > min_dict[type]:
                    min_dict[type] = count

    for temp in min_dict.values():
        if return_me == 0:
            return_me = temp
        else:
            return_me = return_me * temp

    return return_me


def some_function(file_name: str = "input.txt", part_two: bool = False) -> int:
    return_me: int = 0
    directory = os.path.dirname(os.path.realpath(__file__))
    file = open(os.path.join(directory, file_name), "r")
    all_lines = file.readlines()

    criteria: dict[str, int] = {}
    criteria["red"] = 12
    criteria["green"] = 13
    criteria["blue"] = 14

    for line in all_lines:
        if line == "" or line == "\n":
            continue

        temp = line.split(":")
        game_num = int(temp[0].split()[1])
        dice_draws = temp[1].split(";")

        if part_two is False:
            if is_game_within_criteria(criteria, dice_draws):
                return_me += game_num
        else:
            return_me += get_power(dice_draws)

    return return_me
