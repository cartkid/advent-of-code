import src.year_2023.day_4.code as day


def test_some_function():
    expected = 13
    result = day.some_function("test.txt")
    assert result == expected


def test_answer_some_function():
    expected = 20117
    result = day.some_function("input.txt")
    assert result == expected


def test_part_two_some_function():
    expected = 30
    result = day.some_function("test.txt", True)
    assert result == expected


def test_answer_part_two_some_function():
    expected = 13768818
    result = day.some_function("input.txt", True)
    assert result == expected
