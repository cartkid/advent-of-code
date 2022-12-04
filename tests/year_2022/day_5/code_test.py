import src.year_2022.day_5.code as day_5


def test_some_function():
    expected = 0
    result = day_5.some_function("test.txt")
    assert result == expected


def test_answer_some_function():
    expected = 0
    result = day_5.some_function("input.txt")
    assert result == expected


def test_part_two_some_function():
    expected = 0
    result = day_5.some_function("test.txt", True)
    assert result == expected


def test_answer_part_two_some_function():
    expected = 0
    result = day_5.some_function("input.txt", True)
    assert result == expected
