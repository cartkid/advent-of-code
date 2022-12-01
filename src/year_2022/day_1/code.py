import os
import operator


def some_function(file_name: str = "input.txt", part_two: bool = False) -> int:
    return_me: int = 0
    directory = os.path.dirname(os.path.realpath(__file__))
    file = open(os.path.join(directory, file_name), "r")
    all_lines = file.readlines()

    elf_to_calories: dict[int, int] = {}

    curr_elf: int = 1
    for line in all_lines:
        if line == "" or line == "\n":
            curr_elf += 1
            continue
        val = int(line)
        if curr_elf in elf_to_calories:
            elf_to_calories[curr_elf] += val
        else:
            elf_to_calories[curr_elf] = val

    sorted_elf_to_calories = sorted(
        elf_to_calories.items(), key=operator.itemgetter(1), reverse=True
    )
    highest_calories = sorted_elf_to_calories.pop(0)
    print(f"Elf {highest_calories[0]} has {highest_calories[1]} calories.")
    return_me = highest_calories[1]

    if part_two:
        second_highest_calories = sorted_elf_to_calories.pop(0)
        third_highest_calories = sorted_elf_to_calories.pop(0)

        return_me += second_highest_calories[1]
        return_me += third_highest_calories[1]

    return return_me
