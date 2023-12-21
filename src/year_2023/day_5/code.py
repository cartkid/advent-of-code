import os
from typing import List, Tuple

# seeds: 79 14 55 13

# seed-to-soil map:
# 50 98 2
# 52 50 48

# soil-to-fertilizer map:
# 0 15 37
# 37 52 2
# 39 0 15


class SeedRange:
    def __init__(self, start: int, length: int):
        self.start = start
        self.length = length


class Range:
    def __init__(self, line: str):
        # destination range start, the source range start, and the range length.
        temp = line.split()
        self.destination_range_start = int(temp[0])
        self.source_range_start = int(temp[1])
        self.range_length = int(temp[2])


class Map:
    def __init__(self, name: str, lines: List[str]):
        self.name = name
        temp = name.split("-")
        self.source_name = temp[0]
        self.destination_name = temp[2]
        self.ranges: List[Range] = []
        for r in lines:
            self.ranges.append(Range(r))
        self.map: dict[int, int] = {}

    def get_num(self, source, skippable: int = 1) -> Tuple[int, int]:
        for map_range in self.ranges:
            if (
                source >= map_range.source_range_start
                and source < map_range.source_range_start + map_range.range_length
            ):
                temp = source - map_range.source_range_start
                max_skippable = (
                    map_range.source_range_start + (map_range.range_length - 1)
                ) - source
                if max_skippable > skippable:
                    max_skippable = skippable
                return (map_range.destination_range_start + temp, max_skippable)
        return source, skippable


def some_function(file_name: str = "input.txt", part_two: bool = False) -> int:
    return_me: int = 0
    directory = os.path.dirname(os.path.realpath(__file__))
    file = open(os.path.join(directory, file_name), "r")
    all_lines = file.readlines()

    seed_ranges: List[SeedRange] = []
    maps: dict[str, Map] = {}
    curr_map: str = ""
    curr_map_lines: List[str] = []
    for line in all_lines:
        line = line.strip()
        if line == "" or line == "\n":
            if curr_map != "" and len(curr_map_lines) > 0:
                maps[curr_map] = Map(curr_map, curr_map_lines)
                curr_map = ""
                curr_map_lines = []
            continue

        if len(seed_ranges) == 0 and line.strip().startswith("seeds: "):
            # seeds: 79 14 55 13
            if part_two is False:
                temp_seed_nums = [int(x) for x in line.split(":")[1].strip().split()]
                for seed_num in temp_seed_nums:
                    seed_ranges.append(SeedRange(seed_num, 1))
            else:
                temp_seed_nums = [int(x) for x in line.split(":")[1].strip().split()]
                for i in range(0, len(temp_seed_nums), 2):
                    seed_ranges.append(
                        SeedRange(temp_seed_nums[i], temp_seed_nums[i + 1])
                    )
            continue

        if curr_map == "" and line.strip().endswith(" map:"):
            # soil-to-fertilizer map:
            curr_map = line.split()[0]
            continue

        curr_map_lines.append(line.strip())
    if curr_map != "" and len(curr_map_lines) > 0:
        maps[curr_map] = Map(curr_map, curr_map_lines)
        curr_map = ""
        curr_map_lines = []

    locs: List[int] = []
    curr_spot: str = "seed"
    curr_map_to_use: Map = None
    for seed_range in seed_ranges:
        curr_index: int = 0
        while curr_index < seed_range.length:
            temp_seed_val = seed_range.start + curr_index
            skippable: int = seed_range.length
            while curr_spot != "END":
                for idx, map_item in enumerate(maps.keys()):
                    if map_item.startswith(curr_spot + "-to-"):
                        curr_map_to_use = maps[map_item]
                        break
                    if idx == len(maps) - 1:
                        curr_spot = "END"
                if curr_spot != "END":
                    temp_seed_val, skippable = curr_map_to_use.get_num(
                        temp_seed_val, skippable
                    )
                    curr_spot = curr_map_to_use.destination_name
            locs.append(temp_seed_val)
            curr_spot = "seed"
            if skippable > 1:
                curr_index += skippable
            else:
                curr_index += 1
    return_me = min(locs)

    return return_me
