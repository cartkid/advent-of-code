import src.year_2022.day_11.code as day
import pytest


def test_some_function():
    expected = 10605
    result = day.some_function("test.txt")
    assert result == expected


def test_answer_some_function():
    expected = 99840
    result = day.some_function("input.txt")
    assert result == expected


@pytest.mark.skip("concurrent tests with global variables does not work")
def test_part_two_some_function():
    expected = 2713310158
    result = day.some_function("test.txt", True)
    assert result == expected


def test_answer_part_two_some_function():
    expected = 20683044837
    result = day.some_function("input.txt", True)
    assert result == expected
