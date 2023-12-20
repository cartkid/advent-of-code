import os
from typing import List


def try_parse_int(val: str) -> int:
    return_me: int = -1

    if val == ".":
        return return_me

    try:
        return_me = int(val)
    except:
        print(f"{val} is not an int")

    return return_me


class coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    x: int
    y: int

    def is_adjacent_to(self, other_loc) -> bool:
        return_me: bool = False
        if (
            (self.x - 1 == other_loc.x and self.y - 1 == other_loc.y)
            or (self.x - 1 == other_loc.x and self.y == other_loc.y)
            or (self.x - 1 == other_loc.x and self.y + 1 == other_loc.y)
        ):
            # top
            return_me = True
        elif (self.x == other_loc.x and self.y - 1 == other_loc.y) or (
            self.x == other_loc.x and self.y + 1 == other_loc.y
        ):
            # mid
            return_me = True
        elif (
            (self.x + 1 == other_loc.x and self.y - 1 == other_loc.y)
            or (self.x + 1 == other_loc.x and self.y == other_loc.y)
            or (self.x + 1 == other_loc.x and self.y + 1 == other_loc.y)
        ):
            # bottom
            return_me = True
        return return_me


class NumberAndCoords:
    def __init__(self, number: int, coords: list[coord]):
        self.number = number
        self.coords = coords

    number: int
    coords: list[coord]

    def is_part_number(self, grid: List[List[str]]) -> bool:
        locs_to_check = self.get_locs_to_check(grid)
        for loc in locs_to_check:
            if NumberAndCoords.check_loc(grid, loc):
                return True
        return False

    def get_locs_to_check(self, grid: List[List[str]]) -> List[coord]:
        return_me: List[coord] = []
        if self.coords[0].x > 0:
            # not top
            for loc in self.coords:
                return_me.append(coord(loc.x - 1, loc.y))
            if self.coords[0].y > 0:
                # not left most
                return_me.append(coord(self.coords[0].x - 1, self.coords[0].y - 1))
            if (len(self.coords) + self.coords[0].y) < len(grid[0]):
                # not right most
                return_me.append(
                    coord(self.coords[0].x - 1, len(self.coords) + self.coords[0].y)
                )
        if self.coords[0].x < len(grid) - 1:
            # not bottom
            for loc in self.coords:
                return_me.append(coord(loc.x + 1, loc.y))
            if self.coords[0].y > 0:
                # not left most
                return_me.append(coord(self.coords[0].x + 1, self.coords[0].y - 1))
            if (len(self.coords) + self.coords[0].y) < len(grid[0]):
                # not right most
                return_me.append(
                    coord(self.coords[0].x + 1, len(self.coords) + self.coords[0].y)
                )
        if self.coords[0].y > 0:
            # not left most
            return_me.append(coord(self.coords[0].x, self.coords[0].y - 1))
        if (len(self.coords) + self.coords[0].y) < len(grid[0]):
            # not right most
            return_me.append(
                coord(self.coords[0].x, len(self.coords) + self.coords[0].y)
            )
        return return_me

    @staticmethod
    def check_loc(grid: List[List[str]], coord: coord) -> bool:
        if coord.x < 0 or coord.x >= len(grid):
            return False

        temp = grid[coord.x][coord.y]
        if temp != "." and try_parse_int(temp) == -1:
            return True

        return False


class SpecialChar:
    def __init__(self, char, loc: coord):
        self.char = char
        self.loc = loc

    char: str
    loc: coord

    def is_gear(self, numbers_and_coords: List[NumberAndCoords]) -> int:
        return_me: int = -1

        if self.char != "*":
            return return_me

        adjacent_numbers: List[int] = []
        for curr_number in numbers_and_coords:
            for curr_coord in curr_number.coords:
                if curr_coord.is_adjacent_to(self.loc):
                    adjacent_numbers.append(curr_number.number)
                    break

        if len(adjacent_numbers) == 2:
            return_me = adjacent_numbers[0] * adjacent_numbers[1]

        return return_me


def some_function(file_name: str = "input.txt", part_two: bool = False) -> int:
    return_me: int = 0
    directory = os.path.dirname(os.path.realpath(__file__))
    file = open(os.path.join(directory, file_name), "r")
    all_lines = file.readlines()

    grid: list[list[str]] = []

    numbers_and_coords: List[NumberAndCoords] = []
    special_chars: List[SpecialChar] = []

    curr_x: int = 0
    for line in all_lines:
        line = line.strip()
        if line == "" or line == "\n":
            continue

        grid.append([])
        temp = ""
        temp_coords: list[coord] = []
        curr_y: int = 0
        for char in line:
            index: int = len(grid) - 1
            grid[index].append(char)

            val = try_parse_int(char)
            if val > -1:
                temp += str(val)
                temp_coords.append(coord(curr_x, curr_y))
            else:
                if char != ".":
                    # it is a special char
                    special_chars.append(SpecialChar(char, coord(curr_x, curr_y)))
                if temp != "":
                    numbers_and_coords.append(NumberAndCoords(int(temp), temp_coords))
                    temp = ""
                    temp_coords = []
            curr_y += 1
        if temp != "":
            numbers_and_coords.append(NumberAndCoords(int(temp), temp_coords))
            temp = ""
            temp_coords = []
        curr_x += 1

    if part_two is False:
        for curr in numbers_and_coords:
            if curr.is_part_number(grid):
                return_me += curr.number
    else:
        for curr_special_char in special_chars:
            is_gear_val = curr_special_char.is_gear(numbers_and_coords)
            if is_gear_val > -1:
                return_me += is_gear_val

    return return_me
