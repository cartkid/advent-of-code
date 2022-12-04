import os


def is_fully_contained(l1: list[str], l2: list[str], part_two: bool = False) -> bool:
    temp_l1: list[str] = l1
    temp_l2: list[str] = l2

    if len(l2) > len(l1):
        temp_l1 = l2
        temp_l2 = l1

    for i in temp_l2:
        if part_two is False and i not in temp_l1:
            return False
        elif part_two is True and i in temp_l1:
            return True

    if part_two is False:
        return True
    else:
        return False


def some_function(file_name: str = "input.txt", part_two: bool = False) -> int:
    return_me: int = 0
    directory = os.path.dirname(os.path.realpath(__file__))
    file = open(os.path.join(directory, file_name), "r")
    all_lines = file.readlines()

    assignment_pairs: list[tuple[list[str], list[str]]] = []
    total_fully_contained_count: int = 0
    for i, line in enumerate(all_lines):
        values_only = line.strip("\n")
        pairs = values_only.split(",")
        assignment_pairs.append(([], []))
        for j, pair in enumerate(pairs):
            start = int(pair.split("-")[0])
            end = int(pair.split("-")[1]) + 1
            for num in range(start, end):
                (assignment_pairs[i])[j].append(str(num))

        if is_fully_contained(assignment_pairs[i][0], assignment_pairs[i][1], part_two):
            total_fully_contained_count += 1

    return_me = total_fully_contained_count

    return return_me
