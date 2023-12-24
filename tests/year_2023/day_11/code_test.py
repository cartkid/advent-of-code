import src.year_2023.day_11.code as day


def test_some_function():
    expected = 374
    result = day.some_function("test.txt")
    assert result == expected


def test_answer_some_function():
    expected = 10228230
    result = day.some_function("input.txt")
    assert result == expected


# def test_part_two_some_function():
#     expected = 8410
#     result = day.some_function("test.txt", True)
#     assert result == expected


def test_answer_part_two_some_function():
    expected = 447073334102
    result = day.some_function("input.txt", True)
    assert result == expected
