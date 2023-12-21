import src.year_2023.day_5.code as day


def test_some_function():
    expected = 35
    result = day.some_function("test.txt")
    assert result == expected


def test_answer_some_function():
    expected = 309796150
    result = day.some_function("input.txt")
    assert result == expected


def test_part_two_some_function():
    expected = 46
    result = day.some_function("test.txt", True)
    assert result == expected


def test_answer_part_two_some_function():
    expected = 50716416
    result = day.some_function("input.txt", True)
    assert result == expected
