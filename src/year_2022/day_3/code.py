import os


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

        curr_game_score = 0
        curr_total_score += curr_game_score
        print(f"game {curr_game}: score {curr_game_score}: total {curr_total_score}")
        curr_game += 1

    return_me = curr_total_score

    return return_me
