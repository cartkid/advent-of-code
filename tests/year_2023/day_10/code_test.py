import src.year_2023.day_10.code as day


def test_some_function():
    expected = 4
    result = day.some_function("test.txt")
    assert result == expected


def test2_some_function():
    expected = 8
    result = day.some_function("test2.txt")
    assert result == expected


def test():
    grid = ["7-F7-", ".FJ|7", "SJLL7", "|F--J", "LJ.LJ"]
    expected = ["..F7.", ".FJ|.", "FJ.L7", "|F--J", "LJ..."]
    test = day.PipeGrid(grid)

    for idx, line in enumerate(test.lines):
        assert "".join(line) == expected[idx]


def test_answer_some_function():
    expected = 6856
    result = day.some_function("input.txt")
    assert result == expected


def test_part_two_some_function():
    expected = 1
    result = day.some_function("test.txt", True)
    assert result == expected


def test_answer_part_two_some_function():
    expected = 501
    result = day.some_function("input.txt", True)
    assert result == expected
