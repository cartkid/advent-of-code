import functools
import os
from typing import List, Union
from enum import Enum
import operator

# Five of a kind, where all five cards have the same label: AAAAA
# Four of a kind, where four cards have the same label and one card has a different label: AA8AA
# Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
# Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
# Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
# One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
# High card, where all cards' labels are distinct: 23456

IS_PART_TWO: bool = False


class HandType(Enum):
    HIGH_CARD = 100
    ONE_PAIR = 200
    TWO_PAIR = 300
    THREE_OF_A_KIND = 400
    FULL_HOUSE = 500
    FOUR_OF_A_KIND = 600
    FIVE_OF_A_KIND = 700

    @staticmethod
    def get(val: str, is_part_two: bool = False):
        d: dict[str, int] = {}
        for v in val:
            if v in d.keys():
                d[v] = d[v] + 1
            else:
                d[v] = 1

        d_descending = sorted(d.items(), key=operator.itemgetter(1), reverse=True)

        if is_part_two is True and "J" in d.keys():
            most_occurring: str = (
                d_descending[0][0]
                if d_descending[0][0] != "J"
                else d_descending[1][0]
                if len(d_descending) > 1
                else "2"
            )
            val = val.replace("J", most_occurring)
            return HandType.get(val, is_part_two)

        if d_descending[0][1] == 5:
            return HandType.FIVE_OF_A_KIND
        if d_descending[0][1] == 4:
            return HandType.FOUR_OF_A_KIND
        if d_descending[0][1] == 3 and d_descending[1][1] == 2:
            return HandType.FULL_HOUSE
        if d_descending[0][1] == 3:
            return HandType.THREE_OF_A_KIND
        if d_descending[0][1] == 2 and d_descending[1][1] == 2:
            return HandType.TWO_PAIR
        if d_descending[0][1] == 2:
            return HandType.ONE_PAIR
        return HandType.HIGH_CARD


class CARD_TYPE(Enum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14
    JOKER = 1

    @staticmethod
    def get(val, is_part_two: bool = False):
        match val:
            case "A":
                return CARD_TYPE.ACE
            case "K":
                return CARD_TYPE.KING
            case "Q":
                return CARD_TYPE.QUEEN
            case "J":
                return CARD_TYPE.JACK if is_part_two is False else CARD_TYPE.JOKER
            case "T":
                return CARD_TYPE.TEN
            case "9":
                return CARD_TYPE.NINE
            case "8":
                return CARD_TYPE.EIGHT
            case "7":
                return CARD_TYPE.SEVEN
            case "6":
                return CARD_TYPE.SIX
            case "5":
                return CARD_TYPE.FIVE
            case "4":
                return CARD_TYPE.FOUR
            case "3":
                return CARD_TYPE.THREE
            case "2":
                return CARD_TYPE.TWO
        return CARD_TYPE.TWO


class Hand:
    def __init__(self, hand: str, bid: int, is_part_two: bool = False):
        self.hand = hand
        self.bid = bid
        self.hand_type = HandType.get(self.hand, is_part_two)
        self.score = self.hand_type.value

    def get_score_at_index(self, index: int, is_part_two: bool = False) -> int:
        return CARD_TYPE.get(self.hand[index], is_part_two).value


def compare(item1, item2):
    if item1.score < item2.score:
        return -1
    if item1.score > item2.score:
        return 1

    for i in range(5):
        x_val = item1.get_score_at_index(i, IS_PART_TWO)
        y_val = item2.get_score_at_index(i, IS_PART_TWO)
        if x_val == y_val:
            continue
        if x_val < y_val:
            return -1
        if x_val > y_val:
            return 1

    return 0


def get_result(hands: List[Hand], is_part_two: bool = False) -> int:
    global IS_PART_TWO
    return_me: int = 0
    hands.sort(key=lambda kv: kv.score, reverse=True)

    prior: Union[HandType, None] = None
    for hand_index in range(len(hands)):
        if prior is not None:
            if prior == hands[hand_index].hand_type:
                compare(hands[hand_index - 1], hands[hand_index])
        prior = hands[hand_index].hand_type

    IS_PART_TWO = is_part_two

    hands.sort(key=functools.cmp_to_key(compare))
    for idx, hand in enumerate(hands):
        multiplier = idx + 1
        return_me += multiplier * hand.bid

    return return_me


def some_function(file_name: str = "input.txt", part_two: bool = False) -> int:
    directory = os.path.dirname(os.path.realpath(__file__))
    file = open(os.path.join(directory, file_name), "r")
    all_lines = file.readlines()

    hands: List[Hand] = []
    for line in all_lines:
        line = line.strip()
        if line == "" or line == "\n":
            continue

        # QQQJA 483
        items = line.split()
        hands.append(Hand(items[0].strip(), int(items[1].strip()), part_two))

    return get_result(hands, part_two)
