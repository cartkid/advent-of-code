import os
from typing import List


class Position:
    def __init__(self, i: int, j: int):
        self.i = i
        self.j = j
        self.is_invalid = False if i == -1 and j == -1 else True

    def add_position(self, pos):
        return Position(self.i + pos.i, self.j + pos.j)

    def to_string(self):
        return f"({self.i},{self.j})"


class SpaceMap:
    def __init__(self, lines: List[str], part_two: bool = False):
        self.lines: List[List[str]] = list(list(l) for l in lines)
        self.empty_i_s: List[int] = []
        self.empty_j_s: List[int] = []
        self.expand()
        self.galaxies: dict[str, Position] = self.get_galaxies()
        self.galaxy_routes: dict[str, GalaxyRoute] = self.get_galaxy_routes(part_two)

    def get_galaxies(self):
        galaxies: dict[str, Position] = {}
        for i in range(len(self.lines)):
            for j in range(len(self.lines[0])):
                if self.lines[i][j] == "#":
                    galaxy = Position(i, j)
                    galaxies[galaxy.to_string()] = galaxy
        return galaxies

    def get_galaxy_routes(self, part_two: bool = False):
        return_me: dict[str, GalaxyRoute] = {}
        galaxy_keys = list(self.galaxies.keys())
        for idx, galaxy_a_name in enumerate(self.galaxies):
            galaxy_a = self.galaxies[galaxy_a_name]
            for galaxy_b_index in range(idx + 1, len(self.galaxies)):
                galaxy_b_name = galaxy_keys[galaxy_b_index]
                galaxy_b = self.galaxies[galaxy_b_name]
                galaxy_route = GalaxyRoute(self, galaxy_a, galaxy_b, part_two)
                return_me[galaxy_route.to_string()] = galaxy_route
        return return_me

    def expand(self):
        i: int = 0
        while i < len(self.lines):
            for j in range(len(self.lines[i])):
                if self.lines[i][j] != ".":
                    break
                if j == len(self.lines[i]) - 1:
                    self.empty_i_s.append(i)
            i += 1

        j: int = 0
        i = 0
        while j < len(self.lines[0]):
            for i in range(len(self.lines)):
                if self.lines[i][j] != ".":
                    break
                if i == len(self.lines) - 1:
                    self.empty_j_s.append(j)
            j += 1


class GalaxyRoute:
    def __init__(
        self,
        space_map: SpaceMap,
        galaxy_a: Position,
        galaxy_b: Position,
        part_two: bool = False,
    ):
        self.space_map = space_map
        self.galaxy_a = galaxy_a
        self.galaxy_b = galaxy_b
        self.steps = GalaxyRoute._get_steps(
            space_map, self.galaxy_a, self.galaxy_b, part_two
        )

    def to_string(self):
        return "_to_".join(
            sorted([self.galaxy_a.to_string(), self.galaxy_b.to_string()])
        )

    @staticmethod
    def _get_steps(
        space_map: SpaceMap,
        galaxy_a: Position,
        galaxy_b: Position,
        part_two: bool = False,
    ) -> int:
        empty_i_count: int = 0
        empty_j_count: int = 0
        multiple: int = 1 if part_two is False else (1000000 - 1)
        for empty_i in space_map.empty_i_s:
            if GalaxyRoute._is_between(empty_i, galaxy_a.i, galaxy_b.i):
                empty_i_count += 1
        for empty_j in space_map.empty_j_s:
            if GalaxyRoute._is_between(empty_j, galaxy_a.j, galaxy_b.j):
                empty_j_count += 1
        return (
            abs(galaxy_a.i - galaxy_b.i)
            + abs(galaxy_a.j - galaxy_b.j)
            + (empty_i_count * multiple)
            + (empty_j_count * multiple)
        )

    @staticmethod
    def _is_between(val: int, a: int, b: int) -> bool:
        if a < b:
            if a < val and val < b:
                return True
        elif b < a:
            if b < val and val < a:
                return True
        return False


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

    space_map = SpaceMap(lines, part_two)
    total_steps: int = 0
    for name in space_map.galaxy_routes:
        total_steps += space_map.galaxy_routes[name].steps
    return total_steps
