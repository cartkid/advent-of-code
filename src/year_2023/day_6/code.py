import os
from typing import List, Tuple

# Time:      7  15   30
# Distance:  9  40  200


class Race:
    def __init__(self, time: int):
        self.time = time

    time: int = 0
    distance: int = 0

    def get_ways_to_win(self) -> int:
        count: int = 0
        for hold in range(self.time):
            if (self.time - hold) > 0 and self.distance - (
                hold * (self.time - hold)
            ) < 0:
                count += 1
        return count


def some_function(file_name: str = "input.txt", part_two: bool = False) -> int:
    return_me: int = -1
    directory = os.path.dirname(os.path.realpath(__file__))
    file = open(os.path.join(directory, file_name), "r")
    all_lines = file.readlines()

    races: List[Race] = []
    for line in all_lines:
        line = line.strip()
        if line == "" or line == "\n":
            continue

        if line.startswith("Time:"):
            temp_time_line = line.replace("Time:", "").strip()
            if part_two is True:
                temp_time_line = temp_time_line.replace(" ", "")
            for item in temp_time_line.split():
                races.append(Race(int(item.strip())))

        if line.startswith("Distance:"):
            temp_distance_line = line.replace("Distance:", "").strip()
            if part_two is True:
                temp_distance_line = temp_distance_line.replace(" ", "")
            for idx, item in enumerate(temp_distance_line.split()):
                races[idx].distance = int(item.strip())

    for race in races:
        if return_me == -1:
            return_me = race.get_ways_to_win()
        else:
            return_me *= race.get_ways_to_win()
    return return_me
