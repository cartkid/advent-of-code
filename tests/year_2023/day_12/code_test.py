import src.year_2023.day_12.code as day


def test_some_function():
    expected = 21
    result = day.some_function("test.txt")
    assert result == expected


def test_answer_some_function():
    expected = 6488
    result = day.some_function("input.txt")
    assert result == expected


def test_part_two_some_function():
    expected = 525152
    result = day.some_function("test.txt", True)
    assert result == expected


def test_answer_part_two_some_function():
    expected = 815364548481
    result = day.some_function("input.txt", True)
    assert result == expected
