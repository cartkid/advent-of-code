import os
import copy
from typing import Union


class Decision:
    def __init__(self):
        self.name: str = "."
        self.neighbors: list[int] = []
        self.distance: int = 10000
        self.visited: bool = False
        self.previous = None


def node_height(n):
    if n == "S":
        return ord("a")
    if n == "E":
        return ord("z")
    return ord(n)


def make_node_tree(grid: list[list[str]]):
    row_length = len(grid[0])
    col_length = len(grid)
    decisions: list[Decision] = []
    targets: list[Decision] = []
    source: Union[Decision, None] = None
    for _ in range(row_length * col_length):
        decisions.append(Decision())
    for i, row in enumerate(grid):
        for j, value_height_char in enumerate(row):
            lvl = node_height(value_height_char)
            curr_decision: Decision = decisions[(row_length * i) + j]
            curr_decision.name = str(value_height_char)
            if value_height_char == "S" or value_height_char == "a":
                targets.append(curr_decision)
            elif value_height_char == "E":
                source = curr_decision
            if (i < (col_length - 1)) and lvl <= (node_height(grid[i + 1][j]) + 1):
                curr_decision.neighbors.append((row_length * (i + 1)) + j)
            if (j < (row_length - 1)) and lvl <= (node_height(grid[i][j + 1]) + 1):
                curr_decision.neighbors.append((row_length * (i)) + j + 1)
            if i > 0 and lvl <= (node_height(grid[i - 1][j]) + 1):
                curr_decision.neighbors.append((row_length * (i - 1)) + j)
            if j > 0 and lvl <= (node_height(grid[i][j - 1]) + 1):
                curr_decision.neighbors.append((row_length * (i)) + j - 1)
    return decisions, source, targets


def pop_min_dist(q: list[Decision]):
    m = 10000  # arbitrary high number
    closest_distance = 0
    for i, decision in enumerate(q):
        if decision.distance < m:
            m = decision.distance
            closest_distance = i
    return q.pop(closest_distance)


def dijkstra(decisions: list[Decision], source: Decision):
    choices = []
    for decision in decisions:
        choices.append(decision)
    source.distance = 0

    while len(choices) > 0:
        curr_decision: Decision = pop_min_dist(choices)
        curr_decision.visited = True
        for vi in curr_decision.neighbors:
            decision = decisions[vi]
            if not decision.visited:
                alt = curr_decision.distance + 1  # Graph distance is always 1
                if alt < decision.distance:
                    decision.distance = alt
                    decision.previous = curr_decision  # type: ignore


def some_function(file_name: str = "input.txt", part_two: bool = False) -> int:
    return_me: int = 0
    directory = os.path.dirname(os.path.realpath(__file__))
    file = open(os.path.join(directory, file_name), "r")
    all_lines = file.readlines()

    grid: list[list[str]] = []
    starting_location: tuple[int, int] = (0, 0)

    for i, line in enumerate(all_lines):
        values_only = line.strip("\n")
        grid.append([])
        for j, char in enumerate(values_only):
            if char == "S":
                starting_location = (i, j)
            grid[i].append(char)

    v: list[Decision]
    s: Decision
    targets: list[Decision]
    v, s, targets = make_node_tree(grid)  # type: ignore
    dijkstra(v, s)  # type: ignore
    part1: Decision = targets[0]
    part2: Decision = targets[0]
    for target in targets:
        if target.distance < part2.distance:
            part2 = target
        if target.name == "S":
            part1 = target

    print(f"Result part1 {part1.distance}.")
    print(f"Result part2 {part2.distance}.")
    if part_two is True:
        return part2.distance
    return part1.distance
