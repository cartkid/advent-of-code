import src.year_2022.day_1.code as day_1


def test_some_function():
    expected = 24000
    result = day_1.some_function("test.txt")
    assert result == expected


def test_answer_some_function():
    expected = 74711
    result = day_1.some_function("input.txt")
    assert result == expected


def test_part_two_some_function():
    expected = 45000
    result = day_1.some_function("test.txt", True)
    assert result == expected


def test_answer_part_two_some_function():
    expected = 209481
    result = day_1.some_function("input.txt", True)
    assert result == expected
