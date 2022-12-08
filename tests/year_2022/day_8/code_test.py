import src.year_2022.day_8.code as day


def test_some_function():
    expected = 21
    result = day.some_function("test.txt")
    assert result == expected


def test_answer_some_function():
    expected = 1832
    result = day.some_function("input.txt")
    assert result == expected


def test_part_two_some_function():
    expected = 8
    result = day.some_function("test.txt", True)
    assert result == expected


def test_answer_part_two_some_function():
    expected = 157320
    result = day.some_function("input.txt", True)
    assert result == expected
