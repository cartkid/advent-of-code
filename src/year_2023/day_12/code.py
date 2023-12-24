import os
from typing import List
from functools import cache


@cache
def num_valid_solutions(springs: str, sizes: tuple[int, ...]) -> int:
    if not springs:
        return len(sizes) == 0

    if not sizes:
        return "#" not in springs

    char, rest_of_record = springs[0], springs[1:]

    if char == ".":
        return num_valid_solutions(rest_of_record, sizes)

    if char == "#":
        size = sizes[0]
        if (
            len(springs) >= size
            and all(c != "." for c in springs[:size])
            and (len(springs) == size or springs[size] != "#")
        ):
            return num_valid_solutions(springs[size + 1 :], sizes[1:])
        return 0

    if char == "?":
        return num_valid_solutions(f"#{rest_of_record}", sizes) + num_valid_solutions(
            f".{rest_of_record}", sizes
        )

    raise ValueError(f"unknown char: {char}")


def solve_line(line: str, part_two: bool = False) -> int:
    springs, sizes_str = line.split()
    sizes = tuple(map(int, sizes_str.split(",")))

    if part_two:
        springs = "?".join([springs] * 5)
        sizes *= 5

    return num_valid_solutions(springs, sizes)


class SpringMap:
    def __init__(self, lines: List[str], part_two: bool = False):
        self.lines: List[str] = lines
        self.valid_solutions = self.parse_springs(part_two)

    def parse_springs(self, part_two: bool = False):
        return_me: int = 0

        # .??..??...?##. 1,1,3
        for line in self.lines:
            return_me += solve_line(line, part_two)

        return return_me


def some_function(file_name: str = "input.txt", part_two: bool = False) -> int:
    directory = os.path.dirname(os.path.realpath(__file__))
    file = open(os.path.join(directory, file_name), "r")
    all_lines = file.readlines()

    lines: List[str] = []
    for line in all_lines:
        line = line.strip()
        if line == "" or line == "\n":
            continue
        lines.append(line)

    spring_map = SpringMap(lines, part_two)
    return spring_map.valid_solutions
