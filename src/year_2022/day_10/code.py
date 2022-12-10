import os
import math


def print_screen(screen: list[list[str]]):
    for r in screen:
        print("".join(r))


def get_curr_sprite(curr_x: int) -> list[str]:
    return_me: list[str] = []
    for i in range(0, 40):
        if i in [curr_x - 1, curr_x, curr_x + 1]:
            return_me.append("#")
        else:
            return_me.append(" ")
    return return_me


def some_function(file_name: str = "input.txt", part_two: bool = False) -> int:
    return_me: int = 0
    directory = os.path.dirname(os.path.realpath(__file__))
    file = open(os.path.join(directory, file_name), "r")
    all_lines = file.readlines()

    cycle_consumption: dict[str, int] = {"noop": 1, "addx": 2}
    curr_x: int = 1  # starts at 1
    curr_cycle: int = 0
    important_cycles: list[int] = [20, 60, 100, 140, 180, 220]
    curr_important_cycle_index: int = 0
    important_cycle_x_values: list[int] = []

    screen: list[list[str]] = []
    # make a blank screen
    for r in range(0, 6):
        screen.append([])
        for c in range(0, 40):
            screen[r].append(".")

    for i, line in enumerate(all_lines):
        values_only = line.strip("\n").split(" ")

        curr_sprite = get_curr_sprite(curr_x=curr_x)

        operation: str = values_only[0]
        amount_to_add: int = 0
        if operation == "addx":
            amount_to_add = int(values_only[1])
        cycles_consumed = cycle_consumption[operation]
        start = curr_cycle
        end = curr_cycle + cycles_consumed
        prior_cycle_count = curr_cycle
        for c in range(start, end):
            column = c % 40
            row = math.floor(c / 40)
            screen[row][column] = curr_sprite[column]
            curr_cycle += 1

        if part_two is False:
            if (
                prior_cycle_count
                < important_cycles[curr_important_cycle_index]
                <= curr_cycle
            ):
                important_cycle_x_values.append(
                    important_cycles[curr_important_cycle_index] * curr_x
                )
                if len(important_cycles) - 1 == curr_important_cycle_index:
                    pass
                else:
                    curr_important_cycle_index += 1

        curr_x += amount_to_add

    if part_two is False:
        return_me = sum(important_cycle_x_values)
    else:
        print_screen(screen)
        return_me = -1

    return return_me
