import os
from typing import List, Union, Tuple
from operator import attrgetter, itemgetter
import math


class Position:
    def __init__(self, i: int, j: int):
        self.i = i
        self.j = j
        self.is_invalid = False if i == -1 and j == -1 else True

    def add_position(self, pos):
        return Position(self.i + pos.i, self.j + pos.j)

    def as_str(self):
        return f"({self.i},{self.j})"


class PipeGrid:
    def __init__(self, lines: List[str]):
        self.lines = list(list(l) for l in lines)
        self.starting_position = self.get_starting_position()
        self.loop = self.get_valid_positions_and_remove_noise()

    def get_starting_position(self) -> Position:
        for i in range(len(self.lines)):
            for j in range(len(self.lines[0])):
                if self.lines[i][j] == "S":
                    return Position(i, j)
        return Position(-1, -1)

    def is_valid_position(self, position_to_check: Position) -> bool:
        i_max = len(self.lines) - 1
        j_max = len(self.lines[0]) - 1

        if (
            position_to_check.i < 0
            or position_to_check.i > i_max
            or position_to_check.j < 0
            or position_to_check.j > j_max
        ):
            return False
        return True

    def get_value_at_position(self, position: Position) -> str:
        if position is None:
            return ""
        return self.lines[position.i][position.j]

    def get_two_pipes_connecting(self, curr_position: Position):
        value_at_position: str = self.get_value_at_position(curr_position)
        positions: List[Position] = []
        raw_positions_used: List[Position] = []
        for position_to_check in PipeGrid.get_positions_to_check(value_at_position):
            temp_position = curr_position.add_position(position_to_check[0])
            if temp_position is None or self.is_valid_position(temp_position) is False:
                continue
            temp_value = self.get_value_at_position(temp_position)
            if temp_value in position_to_check[1]:
                positions.append(temp_position)
                raw_positions_used.append(position_to_check[0])
        return positions, raw_positions_used

    def get_char_based_on_positions(self, raw_positions_used: list[Position]) -> str:
        a = raw_positions_used[0]
        b = raw_positions_used[1]
        if a.i == 0 and b.i == 0:
            return "-"
        if a.j == 0 and b.j == 0:
            return "|"
        if (a.j == -1 or b.j == -1) and (b.i == -1 or a.i == -1):
            return "J"
        if (a.j == -1 or b.j == -1) and (b.i == 1 or a.i == 1):
            return "7"
        if (a.j == 1 or b.j == 1) and (b.i == -1 or a.i == -1):
            return "L"
        if (a.j == 1 or b.j == 1) and (b.i == 1 or a.i == 1):
            return "F"
        return ""

    def get_valid_positions_and_remove_noise(self):
        curr_position = self.starting_position
        valid_positions: dict[str, Position] = {}
        valid_positions[self.starting_position.as_str()] = self.starting_position

        while True:
            positions, raw_positions_used = self.get_two_pipes_connecting(curr_position)
            if self.get_value_at_position(curr_position) == "S":
                letter = self.get_char_based_on_positions(raw_positions_used)
                self.lines[curr_position.i][curr_position.j] = letter

            print([x.as_str() for x in positions])
            curr_position = (
                positions[0]
                if positions[0].as_str() not in valid_positions
                else None
                if len(positions) < 2
                else positions[1]
            )
            if curr_position is None or curr_position.as_str() in valid_positions:
                break
            valid_positions[curr_position.as_str()] = curr_position

        for i in range(len(self.lines)):
            for j in range(len(self.lines[0])):
                if Position(i, j).as_str() not in valid_positions:
                    self.lines[i][j] = "."

        return valid_positions

    def count_inside(self) -> int:
        outside: dict[str, Position] = {}
        for i, line in enumerate(self.lines):
            within: bool = False
            up = None
            for j, char in enumerate(line):
                if Position(i, j).as_str() in self.loop:
                    if char == "|":
                        within = not within
                    elif char in "LF":
                        up = char == "L"
                    elif char in "7J":
                        if char != ("J" if up else "7"):
                            within = not within
                        up = None

                if not within:
                    new_outside = Position(i, j)
                    outside[new_outside.as_str()] = new_outside

        for o_key in outside:
            p = outside[o_key]
            self.lines[p.i][p.j] = "*"

        inside_count: int = 0
        for i in range(len(self.lines)):
            for j in range(len(self.lines[0])):
                if self.lines[i][j] == ".":
                    inside_count += 1

        return inside_count

    @staticmethod
    def get_positions_to_check(value_at_position: str = "S"):
        return_me: List[Tuple[Position, List[str]]] = []
        if value_at_position in ["L", "J", "|", "S"]:
            return_me.append((Position(-1, 0), ["F", "7", "|"]))  # above
        if value_at_position in ["F", "7", "|", "S"]:
            return_me.append((Position(1, 0), ["L", "J", "|"]))  # below
        if value_at_position in ["7", "J", "-", "S"]:
            return_me.append((Position(0, -1), ["F", "L", "-"]))  # left
        if value_at_position in ["F", "L", "-", "S"]:
            return_me.append((Position(0, 1), ["7", "J", "-"]))  # right
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

    pipe_grid = PipeGrid(lines)
    if part_two is False:
        return len(pipe_grid.loop) // 2
    return pipe_grid.count_inside()
