import src.year_2022.day_6.code as day


def test_some_function():
    expected = 7
    result = day.some_function("test.txt")
    assert result == expected


def test_answer_some_function():
    expected = 1909
    result = day.some_function("input.txt")
    assert result == expected


def test_part_two_some_function():
    expected = 19
    result = day.some_function("test.txt", True)
    assert result == expected


def test_answer_part_two_some_function():
    expected = 3380
    result = day.some_function("input.txt", True)
    assert result == expected
