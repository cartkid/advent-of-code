import src.year_2022.day_7.code as day


def test_some_function():
    expected = 95437
    result = day.some_function("test.txt")
    assert result == expected


def test_answer_some_function():
    expected = 1325919
    result = day.some_function("input.txt")
    assert result == expected


def test_part_two_some_function():
    expected = 24933642
    result = day.some_function("test.txt", True)
    assert result == expected


def test_answer_part_two_some_function():
    expected = 2050735
    result = day.some_function("input.txt", True)
    assert result == expected
