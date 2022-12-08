import os


def get_vertical_row(
    tree_grid: list[list[int]], row_num: int, column_num: int, beginning_part: bool
) -> list[int]:
    horizontal_row: list[int] = []

    if beginning_part is True:
        temp = tree_grid[0:row_num]
        temp.reverse()
        for i in temp:
            horizontal_row.append(i[column_num])
    else:
        for i in tree_grid[row_num + 1 :]:
            horizontal_row.append(i[column_num])

    return horizontal_row


def count_visible_trees(tree_grid: list[list[int]]) -> int:
    visible_trees: int = 0

    visible_trees = 2 * len(tree_grid)
    visible_trees += 2 * (len(tree_grid[0]) - 2)

    for i in range(1, len(tree_grid) - 1):
        for j in range(1, len(tree_grid) - 1):
            curr_tree = tree_grid[i][j]
            curr_comparison_left = max(tree_grid[i][0:j])
            curr_comparison_right = max(tree_grid[i][j + 1 :])
            curr_comparison_top = max(get_vertical_row(tree_grid, i, j, True))
            curr_comparison_bottom = max(get_vertical_row(tree_grid, i, j, False))
            if curr_tree > curr_comparison_left:
                visible_trees += 1
            elif curr_tree > curr_comparison_right:
                visible_trees += 1
            elif curr_tree > curr_comparison_top:
                visible_trees += 1
            elif curr_tree > curr_comparison_bottom:
                visible_trees += 1

    return visible_trees


def get_directional_score(curr_tree: int, trees: list[int]) -> int:
    score: int = 0
    for tree in trees:
        if tree < curr_tree:
            score += 1
        elif tree >= curr_tree:
            score += 1
            return score
    return score


def scenic_score(tree_grid: list[list[int]]) -> int:
    max_score: int = 0

    for i in range(1, len(tree_grid) - 1):
        for j in range(1, len(tree_grid) - 1):
            curr_tree = tree_grid[i][j]
            up_trees = get_vertical_row(tree_grid, i, j, True)
            down_trees = get_vertical_row(tree_grid, i, j, False)
            left_trees = tree_grid[i][0:j]
            left_trees.reverse()
            right_trees = tree_grid[i][j + 1 :]
            up_score: int = get_directional_score(curr_tree=curr_tree, trees=up_trees)
            down_score: int = get_directional_score(
                curr_tree=curr_tree, trees=down_trees
            )
            left_score: int = get_directional_score(
                curr_tree=curr_tree, trees=left_trees
            )
            right_score: int = get_directional_score(
                curr_tree=curr_tree, trees=right_trees
            )

            score = up_score * down_score * left_score * right_score
            if score > max_score:
                max_score = score

    return max_score


def some_function(file_name: str = "input.txt", part_two: bool = False) -> int:
    return_me: int = 0
    directory = os.path.dirname(os.path.realpath(__file__))
    file = open(os.path.join(directory, file_name), "r")
    all_lines = file.readlines()

    tree_grid: list[list[int]] = []
    for i, line in enumerate(all_lines):
        values_only = line.strip("\n")
        tree_grid.append([])
        for j, char in enumerate(values_only):
            tree_grid[i].append(int(char))

    if part_two is False:
        return_me = count_visible_trees(tree_grid)
    else:
        return_me = scenic_score(tree_grid)

    return return_me
