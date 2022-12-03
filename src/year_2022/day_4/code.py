import os


def some_function(file_name: str = "input.txt", part_two: bool = False) -> int:
    return_me: int = 0
    directory = os.path.dirname(os.path.realpath(__file__))
    file = open(os.path.join(directory, file_name), "r")
    all_lines = file.readlines()

    sacks: list[tuple[list[str], list[str]]] = []
    score_of_line: int = 0
    total_score: int = 0
    for i, line in enumerate(all_lines):
        values_only = line.strip("\n")
        sacks.append(([], []))
        for j, char in enumerate(values_only):
            if j < (len(values_only) / 2):
                sacks[i][0].append(char)
            else:
                sacks[i][1].append(char)

        total_score += score_of_line

    return_me = total_score

    return return_me
