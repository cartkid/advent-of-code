import os
import math


def perform_move(
    stacks: dict[int, list[str]], move: tuple[int, int, int], part_two: bool = False
) -> dict[int, list[str]]:
    temp: list[str] = []
    for i in range(move[0]):
        box = stacks[move[1]].pop()
        temp.append(box)
        if part_two is False:
            stacks[move[2]].append(box)
    if part_two is True:
        for i in range(move[0]):
            box = temp.pop()
            stacks[move[2]].append(box)
    return stacks


def some_function(file_name: str = "input.txt", part_two: bool = False) -> str:
    return_me: str = ""
    directory = os.path.dirname(os.path.realpath(__file__))
    file = open(os.path.join(directory, file_name), "r")
    all_lines = file.readlines()

    stacks: dict[int, list[str]] = {}
    moves: list[tuple[int, int, int]] = []
    max_stack: int = 0
    for i, line in enumerate(all_lines):
        if line.startswith("[") or line.startswith(" "):
            for i, letter in enumerate(line):
                if ((i - 1) % 4) == 0 and letter != " " and line[i - 1] == "[":
                    stack_num = math.floor((i - 1) / 4) + 1
                    if stack_num > max_stack:
                        max_stack = stack_num
                    if stack_num not in stacks:
                        stacks[stack_num] = [letter]
                    else:
                        stacks[stack_num].insert(0, letter)

        elif line.startswith("move"):
            temp = line.replace("move ", "")
            temp = temp.replace("from ", "")
            temp = temp.replace("to ", "")
            vals = temp.split(" ")
            move_quantity = int(vals[0])
            from_spot = int(vals[1])
            to_spot = int(vals[2])
            moves.append((move_quantity, from_spot, to_spot))

    for move in moves:
        stacks = perform_move(stacks, move, part_two)

    for i in range(max_stack):
        if len(stacks[i + 1]) > 0:
            return_me += stacks[i + 1].pop()

    return return_me
