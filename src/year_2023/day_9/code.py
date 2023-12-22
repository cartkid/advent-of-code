import os
from typing import List, Union, Tuple
from operator import attrgetter
import math


class Segment:
    def __init__(self, as_str: str, part_two: bool = False):
        self.as_str = as_str
        self.original_values: List[int] = [int(x) for x in as_str.strip().split()]
        self.lines: List[List[int]] = self.extrapolate(part_two)

    def extrapolate(self, part_two: bool = False):
        lines: List[List[int]] = []
        new_line = self.original_values.copy()
        lines.append(new_line)
        while not Segment.is_all_zeros(new_line):
            new_line = Segment.get_new_line(lines[len(lines) - 1])
            lines.append(new_line)

        if part_two is False:
            lines[len(lines) - 1].append(0)
            for idx in range(len(lines) - 2, -1, -1):
                if len(lines) > idx:
                    last_val = lines[idx][len(lines[idx]) - 1]
                    val_to_add = lines[idx + 1][len(lines[idx + 1]) - 1]
                    lines[idx].append(last_val + val_to_add)

        if part_two is True:
            lines[len(lines) - 1].insert(0, 0)
            for idx in range(len(lines) - 2, -1, -1):
                if len(lines) > idx:
                    last_val = lines[idx][0]
                    val_to_subtract = lines[idx + 1][0]
                    lines[idx].insert(0, last_val - val_to_subtract)

        return lines

    @staticmethod
    def get_new_line(orig: List[int]):
        line: List[int] = []
        for idx in range(len(orig) - 1):
            line.append(orig[idx + 1] - orig[idx])
        return line

    @staticmethod
    def is_all_zeros(line: List[int]):
        for item in line:
            if item != 0:
                return False
        return True


def some_function(file_name: str = "input.txt", part_two: bool = False) -> int:
    directory = os.path.dirname(os.path.realpath(__file__))
    file = open(os.path.join(directory, file_name), "r")
    all_lines = file.readlines()

    segments: List[Segment] = []
    for line in all_lines:
        line = line.strip()
        if line == "" or line == "\n":
            continue

        segments.append(Segment(line, part_two))

    return_me: int = 0
    for segment in segments:
        return_me += (
            segment.lines[0][len(segment.original_values)]
            if part_two is False
            else segment.lines[0][0]
        )

    return return_me
