import src.year_2022.day_3.code as day_3


def test_some_function():
    expected = 157
    result = day_3.some_function("test.txt")
    assert result == expected


def test_answer_some_function():
    expected = 7701
    result = day_3.some_function("input.txt")
    assert result == expected


def test_part_two_some_function():
    expected = 70
    result = day_3.some_function("test.txt", True)
    assert result == expected


def test_answer_part_two_some_function():
    expected = 2644
    result = day_3.some_function("input.txt", True)
    assert result == expected
