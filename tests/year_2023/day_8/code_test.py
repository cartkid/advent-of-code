import src.year_2023.day_8.code as day


def test_some_function():
    expected = 2
    result = day.some_function("test.txt")
    assert result == expected


def test2_some_function():
    expected = 6
    result = day.some_function("test2.txt")
    assert result == expected


def test_answer_some_function():
    expected = 20513
    result = day.some_function("input.txt")
    assert result == expected


def test3_some_function():
    expected = 6
    result = day.some_function("test3.txt", True)
    assert result == expected


def test_part_two_some_function():
    expected = 2
    result = day.some_function("test.txt", True)
    assert result == expected


def test_answer_part_two_some_function():
    expected = 15995167053923
    result = day.some_function("input.txt", True)
    assert result == expected
