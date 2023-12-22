import os
from typing import List, Union, Tuple
from operator import attrgetter
import math


class Directions:
    def __init__(self, lr: str):
        self.lr = lr

    def get_value(self, index: int) -> Tuple[str, int]:
        if index >= len(self.lr):
            index = 0
        return self.lr[index], index


class MapSegment:
    def __init__(self, start: str, left: str, right: str):
        self.start = start
        self.left = left
        self.right = right

    def get_value(self, l_or_r: str) -> str:
        if l_or_r == "L":
            return self.left
        elif l_or_r == "R":
            return self.right
        return self.start


class Loop:
    def __init__(self, start: str):
        self.start = start

    a_to_z: int = 0
    end_1: str = ""
    z_to_z: int = 0
    end_2: str = ""


def is_complete(curr_locs: List[str], part_two: bool = False) -> bool:
    for item in curr_locs:
        if part_two is False and item != "ZZZ":
            return False

        if not item.endswith("Z"):
            return False

    return True


def is_finished(nums: List[int]) -> bool:
    temp = nums[0]
    for num in nums:
        if num != temp:
            return False
    return True


def get_result(loops: list[Loop], part_two: bool = False) -> int:
    num = max(loops, key=attrgetter("a_to_z")).a_to_z

    if part_two is True:
        temp = [o.a_to_z for o in loops]
        return math.lcm(*temp)

    while True:
        for idl, l in enumerate(loops):
            if (num - l.a_to_z) % l.z_to_z != 0:
                temp = num - l.a_to_z
                temp = (temp // l.z_to_z) + 1
                temp_num = l.a_to_z + (temp * l.z_to_z)
                if num <= temp_num:
                    num = temp_num
                else:
                    num += 1
                break
            else:
                print(f"step: {num}")
            if idl == len(loops) - 1:
                return num


def some_function(file_name: str = "input.txt", part_two: bool = False) -> int:
    directory = os.path.dirname(os.path.realpath(__file__))
    file = open(os.path.join(directory, file_name), "r")
    all_lines = file.readlines()

    directions: Union[Directions, None] = None
    map_segments: dict[str, MapSegment] = {}
    for line in all_lines:
        line = line.strip()
        if line == "" or line == "\n":
            continue

        if directions is None:
            directions = Directions(line)

        else:
            parts = line.split("=")
            name = parts[0].strip()
            map_parts = parts[1].strip("() ").split(",")
            map_segments[name] = MapSegment(
                name, left=map_parts[0].strip(), right=map_parts[1].strip()
            )

    if directions is None:
        print("ERROR, no directions!")
        return -1

    curr_locs: list[str] = []
    if part_two is False:
        curr_locs.append("AAA")
    else:
        for temp in map_segments.keys():
            if temp.endswith("A"):
                curr_locs.append(temp)
    curr_index: int = 0
    count: int = 0

    loops: dict[str, Loop] = {}
    for starting_loc in curr_locs.copy():
        count = 0
        curr_index = 0
        loops[starting_loc] = Loop(starting_loc)
        temp_loop_loc = starting_loc
        override: bool = False
        while not is_complete([temp_loop_loc], part_two) or override is True:
            direction, curr_index = directions.get_value(curr_index)

            temp_loop_loc = map_segments[temp_loop_loc].get_value(direction)

            curr_index += 1
            count += 1
            override = False
            if (
                is_complete([temp_loop_loc], part_two)
                and loops[starting_loc].end_1 == ""
            ):
                loops[starting_loc].end_1 = temp_loop_loc
                loops[starting_loc].a_to_z = count
                override = True
            elif (
                is_complete([temp_loop_loc], part_two)
                and loops[starting_loc].end_1 != ""
                and loops[starting_loc].end_2 == ""
            ):
                loops[starting_loc].end_2 = temp_loop_loc
                loops[starting_loc].z_to_z = count - loops[starting_loc].a_to_z
                override = True

    loops_as_list = list(loops.values())
    lcm: int = get_result(loops_as_list, part_two)

    return lcm

    curr_index = 0
    count = 0
    while not is_complete(curr_locs, part_two):
        direction, curr_index = directions.get_value(curr_index)

        for loc_index in range(len(curr_locs)):
            curr_locs[loc_index] = map_segments[curr_locs[loc_index]].get_value(
                direction
            )

        curr_index += 1
        count += 1

    return count
