import src.year_2022.day_9.code as day
import pytest


def test_some_function():
    expected = 13
    result = day.some_function("test.txt")
    assert result == expected


def test_answer_some_function():
    expected = 6384
    result = day.some_function("input.txt")
    assert result == expected


def test_diagnal_u_some_function():
    rope = day.rope(3)
    rope.snake_coordinates[0] = (1, 1)
    rope.snake_coordinates[1] = (0, 0)
    rope.snake_coordinates[2] = (-1, 0)
    rope.move_step("U")

    assert rope.snake_coordinates[0] == (1, 2)
    assert rope.snake_coordinates[1] == (1, 1)
    assert rope.snake_coordinates[2] == (0, 1)


def test_diagnal_d_some_function():
    rope = day.rope(3)
    rope.snake_coordinates[0] = (0, 0)
    rope.snake_coordinates[1] = (1, 1)
    rope.snake_coordinates[2] = (2, 1)
    rope.move_step("D")

    assert rope.snake_coordinates[0] == (0, -1)
    assert rope.snake_coordinates[1] == (0, 0)
    assert rope.snake_coordinates[2] == (1, 0)


def test_diagnal_l_some_function():
    rope = day.rope(3)
    rope.snake_coordinates[0] = (0, 0)
    rope.snake_coordinates[1] = (1, 1)
    rope.snake_coordinates[2] = (2, 1)
    rope.move_step("L")

    assert rope.snake_coordinates[0] == (-1, 0)
    assert rope.snake_coordinates[1] == (0, 0)
    assert rope.snake_coordinates[2] == (1, 0)

    assert len(rope.tail_coordinates) == 2


def test_diagnal_r_some_function():
    rope = day.rope(10)
    rope.snake_coordinates[0] = (-5, 0)
    rope.snake_coordinates[1] = (-6, 1)
    rope.snake_coordinates[2] = (-7, 1)
    rope.snake_coordinates[3] = (-7, 1)
    rope.snake_coordinates[4] = (-7, 1)
    rope.snake_coordinates[5] = (-7, 1)
    rope.snake_coordinates[6] = (-7, 1)
    rope.snake_coordinates[7] = (-7, 1)
    rope.snake_coordinates[8] = (-7, 1)
    rope.snake_coordinates[9] = (-7, 1)
    rope.move_step("R")

    assert rope.snake_coordinates[0] == (-4, 0)
    assert rope.snake_coordinates[1] == (-5, 0)
    assert rope.snake_coordinates[2] == (-6, 0)
    assert rope.snake_coordinates[3] == (-7, 1)
    assert rope.snake_coordinates[4] == (-7, 1)
    assert rope.snake_coordinates[5] == (-7, 1)
    assert rope.snake_coordinates[6] == (-7, 1)
    assert rope.snake_coordinates[7] == (-7, 1)
    assert rope.snake_coordinates[8] == (-7, 1)
    assert rope.snake_coordinates[9] == (-7, 1)

    assert len(rope.tail_coordinates) == 1


# ..........................
# ........H1234.............
# ............5.............
# ............6.............
# ............7.............
# ............8.............
# ............9.............
# ..........................
# ..........................
# ...........s..............
# ..........................
# ..........................
# ..........................
# ..........................
# ..........................

# .........2345.............
# ........1...6.............
# ........H...7.............
# ............8.............
# ............9.............
# ..........................
# ..........................
# ...........s..............
# ..........................
# ..........................
# ..........................
# ..........................
# ..........................


def test_diagnal_d3_some_function():
    rope = day.rope(10)
    rope.snake_coordinates[0] = (0, 0)
    rope.snake_coordinates[1] = (1, 0)
    rope.snake_coordinates[2] = (2, 0)
    rope.snake_coordinates[3] = (3, 0)
    rope.snake_coordinates[4] = (4, 0)
    rope.snake_coordinates[5] = (4, -1)
    rope.snake_coordinates[6] = (4, -2)
    rope.snake_coordinates[7] = (4, -3)
    rope.snake_coordinates[8] = (4, -4)
    rope.snake_coordinates[9] = (4, -5)
    rope.move_step("D")
    rope.move_step("D")
    rope.move_step("D")

    assert rope.snake_coordinates[0] == (0, -3)
    assert rope.snake_coordinates[1] == (0, -2)
    assert rope.snake_coordinates[2] == (1, -1)
    assert rope.snake_coordinates[3] == (2, -1)
    assert rope.snake_coordinates[4] == (3, -1)
    assert rope.snake_coordinates[5] == (4, -1)
    assert rope.snake_coordinates[6] == (4, -2)
    assert rope.snake_coordinates[7] == (4, -3)
    assert rope.snake_coordinates[8] == (4, -4)
    assert rope.snake_coordinates[9] == (4, -5)

    assert len(rope.tail_coordinates) == 1


def test_diagnal_r17_some_function():
    rope = day.rope(10)
    rope.snake_coordinates[0] = (0, -3)
    rope.snake_coordinates[1] = (0, -2)
    rope.snake_coordinates[2] = (1, -1)
    rope.snake_coordinates[3] = (2, -1)
    rope.snake_coordinates[4] = (3, -1)
    rope.snake_coordinates[5] = (4, -1)
    rope.snake_coordinates[6] = (4, -2)
    rope.snake_coordinates[7] = (4, -3)
    rope.snake_coordinates[8] = (4, -4)
    rope.snake_coordinates[9] = (4, -5)
    rope.move_step("R")
    rope.move_step("R")
    rope.move_step("R")
    rope.move_step("R")
    rope.move_step("R")
    rope.move_step("R")
    rope.move_step("R")
    rope.move_step("R")
    rope.move_step("R")
    rope.move_step("R")
    rope.move_step("R")
    rope.move_step("R")
    rope.move_step("R")
    rope.move_step("R")
    rope.move_step("R")
    rope.move_step("R")
    rope.move_step("R")

    assert rope.snake_coordinates[0] == (17, -3)
    assert rope.snake_coordinates[1] == (16, -3)
    assert rope.snake_coordinates[2] == (15, -3)
    assert rope.snake_coordinates[3] == (14, -3)
    assert rope.snake_coordinates[4] == (13, -3)
    assert rope.snake_coordinates[5] == (12, -3)
    assert rope.snake_coordinates[6] == (11, -3)
    assert rope.snake_coordinates[7] == (10, -3)
    assert rope.snake_coordinates[8] == (9, -3)
    assert rope.snake_coordinates[9] == (8, -3)

    assert len(rope.tail_coordinates) == 5


def test_part_two_some_function():
    expected = 1
    result = day.some_function("test.txt", True)
    assert result == expected


def test_part_two_test2_some_function():
    expected = 36
    result = day.some_function("test2.txt", True)
    assert result == expected


def test_answer_part_two_some_function():
    expected = 2734
    result = day.some_function("input.txt", True)
    assert result == expected
