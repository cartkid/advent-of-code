import os


def intersection(l1: list[str], l2: list[str], l3: list[str] = []) -> list[str]:
    l1 = list(dict.fromkeys(l1))
    l2 = list(dict.fromkeys(l2))
    l3 = list(dict.fromkeys(l3))
    temp = set(l2)
    temp2 = set(l3)
    r = [value for value in l1 if value in temp and (len(l3) == 0 or value in temp2)]
    return r


def score_line(line: list[str]) -> int:
    score: int = 0

    for letter in line:
        curr_ascii_value = ord(letter)
        if letter.isupper():
            score += curr_ascii_value - 38
        else:
            score += curr_ascii_value - 96

    return score


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

        intersect: list[str] = []
        if part_two is False:
            intersect = intersection(sacks[i][0], sacks[i][1])
        if part_two is True and (i + 1) % 3 == 0:
            intersect = intersection(
                sacks[i][0] + sacks[i][1],
                sacks[i - 1][0] + sacks[i - 1][1],
                sacks[i - 2][0] + sacks[i - 2][1],
            )
        score_of_line = score_line(intersect)
        total_score += score_of_line

    return_me = total_score

    return return_me
