import src.year_2023.day_2.code as day_2


def test_some_function():
    expected = 8
    result = day_2.some_function("test.txt")
    assert result == expected


def test_answer_some_function():
    expected = 2716
    result = day_2.some_function("input.txt")
    assert result == expected


def test_part_two_some_function():
    expected = 2286
    result = day_2.some_function("test.txt", True)
    assert result == expected


def test_answer_part_two_some_function():
    expected = 72227
    result = day_2.some_function("input.txt", True)
    assert result == expected
