import os
import ast


def compare(outer_left, outer_right):
    """
    This function compares the packets of each group (2 each).
    + left value == right value -> continue to next | if left < right -> right order
        -> else (it is not in right order)
    + left value || right value having different type -> list & int:
        -> replace int by list(int) and call compare function again
    + both values are list -> go in and compare 1st to 1st, 2nd to 2nd...
    + if left list == [] before right list -> right order
        -> else not right order
    """
    listlen = max(len(outer_left), len(outer_right))
    for i in range(listlen):
        # reached the limit of either left or right
        if i >= len(outer_left):
            return 1
        if i >= len(outer_right):
            return 0
        left = outer_left[i]
        right = outer_right[i]
        # test on element type and do required steps
        ordered = -1
        if type(left) == int and type(right) == int:
            # both are integer - compare them
            if left < right:
                # has right order
                ordered = 1
            elif left > right:
                # does not have right order
                ordered = 0
            else:
                # no difference - can not make decision - continue
                ordered = -1
                continue
        elif type(left) == list and type(right) == list:
            # both are lists - go in, call own function (recursion)
            ordered = compare(left, right)
        elif type(left) == list and type(right) == int:
            # has different type (list|int)
            right = [right]
            # print(f"Mixed types - retry!")
            ordered = compare(left, right)
        elif type(left) == int and type(right) == list:
            # has different type (int|list)
            left = [left]
            # print(f"Mixed types - retry!")
            ordered = compare(left, right)
        if ordered != -1:
            return ordered
    # if end of list is reached:
    return -1


class Pair:
    def __init__(self, index: int, first: str, second: str):
        self.index = index
        self.first = first
        self.second = second

    def is_proper_order(self):
        # first_index, first_list = parse_list(self.first, 0)
        # second_index, second_list = parse_list(self.second, 0)
        comparision = compare(self.first, self.second)
        if comparision:
            return True
        return False


def some_function(file_name: str = "input.txt", part_two: bool = False) -> int:
    return_me: int = 0
    directory = os.path.dirname(os.path.realpath(__file__))
    file = open(os.path.join(directory, file_name), "r")
    all_lines = file.readlines()

    first: str = ""
    second: str = ""
    blank: str = ""
    curr_index: int = 1
    pairs: list[Pair] = []
    for i, line in enumerate(all_lines):
        values_only = line.strip("\n").strip()

        if values_only == blank:
            curr_index += 1
            first = ""
            second = ""
        elif first == "":
            first = ast.literal_eval(values_only)
        elif first != "":
            second = ast.literal_eval(values_only)
            pairs.append(Pair(index=curr_index, first=first, second=second))

    proper_order: int = 0
    all_pairs_in_order = []
    for pair in pairs:
        if pair.is_proper_order():
            proper_order += pair.index
        all_pairs_in_order += [pair.first, pair.second]
        # else:
        #     all_pairs_in_order += [pair.second, pair.first]

    return_me = proper_order

    if part_two is True:
        # just test all packets against [[2]] and [[6]] and multiply the "indices":
        one = 1 + sum(1 for item in all_pairs_in_order if compare(item, [[2]]) == 1)
        two = 2 + sum(1 for item in all_pairs_in_order if compare(item, [[6]]) == 1)
        decoder_key = one * two
        return_me = decoder_key

    return return_me
