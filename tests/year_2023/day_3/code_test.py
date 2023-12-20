import src.year_2023.day_3.code as day_3


def test_some_function():
    expected = 4361
    result = day_3.some_function("test.txt")
    assert result == expected


def test_some_function_simple():
    expected = 1
    result = day_3.some_function("test2.txt")
    assert result == expected


def test_answer_some_function():
    expected = 554003
    result = day_3.some_function("input.txt")
    assert result == expected


def test_part_two_some_function():
    expected = 467835
    result = day_3.some_function("test.txt", True)
    assert result == expected


def test_answer_part_two_some_function():
    expected = 87263515
    result = day_3.some_function("input.txt", True)
    assert result == expected
