import src.year_2023.day_9.code as day


def test_some_function():
    expected = 114
    result = day.some_function("test.txt")
    assert result == expected


def test_answer_some_function():
    expected = 1993300041
    result = day.some_function("input.txt")
    assert result == expected


def test_part_two_some_function():
    expected = 2
    result = day.some_function("test.txt", True)
    assert result == expected


def test_answer_part_two_some_function():
    expected = 1038
    result = day.some_function("input.txt", True)
    assert result == expected
