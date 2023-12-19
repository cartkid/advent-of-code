import src.year_2023.day_1.code as day_1


def test_some_function():
    expected = 142
    result = day_1.some_function("test.txt")
    assert result == expected


def test_answer_some_function():
    expected = 54940
    result = day_1.some_function("input.txt")
    assert result == expected


def test_part_two_some_function():
    expected = 281
    result = day_1.some_function("test2.txt", True)
    assert result == expected


def test_answer_part_two_some_function():
    expected = 54208
    result = day_1.some_function("input.txt", True)
    assert result == expected
