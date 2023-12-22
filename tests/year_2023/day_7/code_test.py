import src.year_2023.day_7.code as day


def test_some_function():
    expected = 6440
    result = day.some_function("test.txt")
    assert result == expected


def test_answer_some_function():
    expected = 249390788
    result = day.some_function("input.txt")
    assert result == expected


def test_part_two_some_function():
    expected = 5905
    result = day.some_function("test.txt", True)
    assert result == expected


def test_answer_part_two_some_function():
    expected = 248750248
    result = day.some_function("input.txt", True)
    assert result == expected


def test_2():
    hand1 = day.Hand("JJTTK", 1, is_part_two=True)
    assert hand1.hand_type == day.HandType.FOUR_OF_A_KIND


def test_1():
    hand1 = day.Hand("AAAAA", 1)
    assert hand1.score == 700

    hand2 = day.Hand("KKKKK", 1)
    assert hand2.score == 700

    hand3 = day.Hand("12345", 40)
    assert hand3.score == 100

    hand1_1 = hand1.get_score_at_index(0)
    assert hand1_1 == 14

    hand2_1 = hand2.get_score_at_index(0)
    assert hand2_1 == 13

    compare = day.compare(hand1, hand2)
    assert compare == 1

    result = day.get_result([hand1, hand2])
    assert result == 3

    result = day.get_result([hand1, hand2, hand3])
    assert result == 45
