import src.year_2023.day_6.code as day


def test_some_function():
    expected = 288
    result = day.some_function("test.txt")
    assert result == expected


def test_answer_some_function():
    expected = 2065338
    result = day.some_function("input.txt")
    assert result == expected


def test_part_two_some_function():
    expected = 71503
    result = day.some_function("test.txt", True)
    assert result == expected


def test_answer_part_two_some_function():
    expected = 34934171
    result = day.some_function("input.txt", True)
    assert result == expected
