import os
from typing import List


def intersection(lst1: List[int], lst2: List[int]) -> List[int]:
    lst3 = [value for value in lst1 if value in lst2]
    return lst3


class Card:
    def __init__(
        self, card_num: int, card_winning_numbers: List[int], card_numbers: List[int]
    ):
        self.card_num = card_num
        self.card_winning_numbers = card_winning_numbers
        self.card_numbers = card_numbers

    instances: int = 1

    def get_card_score(self):
        my_winning_numbers: List[int] = intersection(
            self.card_winning_numbers, self.card_numbers
        )

        score: int = 0
        for num in my_winning_numbers:
            if score == 0:
                score = 1
            else:
                score *= 2
        return score

    def get_count_of_winners(self) -> int:
        my_winning_numbers: List[int] = intersection(
            self.card_winning_numbers, self.card_numbers
        )
        return len(my_winning_numbers)


def some_function(file_name: str = "input.txt", part_two: bool = False) -> int:
    return_me: int = 0
    directory = os.path.dirname(os.path.realpath(__file__))
    file = open(os.path.join(directory, file_name), "r")
    all_lines = file.readlines()

    cards: List[Card] = []
    card_dict: dict[int, Card] = {}
    for line in all_lines:
        line = line.strip()
        if line == "" or line == "\n":
            continue

        # Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53

        card_segments = line.split(":")
        card_num: int = int(card_segments[0].strip().split()[1])
        numbers_segments = card_segments[1].strip().split("|")
        winning_numbers: List[int] = [
            int(x) for x in numbers_segments[0].strip().split()
        ]
        my_numbers: List[int] = [int(x) for x in numbers_segments[1].strip().split()]

        curr_card = Card(card_num, winning_numbers, my_numbers)
        cards.append(curr_card)
        card_dict[card_num] = curr_card

        if part_two is False:
            return_me += curr_card.get_card_score()

    if part_two is True:
        card_stack: List[int] = []
        for i in range(cards[len(cards) - 1].card_num):
            card_stack.append(i + 1)
        cards_processed: int = 0
        while cards_processed < len(card_stack) - 1:
            curr_card = card_dict[card_stack[cards_processed]]
            winners: int = curr_card.get_count_of_winners()
            for i in range(winners):
                card_stack.append(curr_card.card_num + i + 1)
            cards_processed += 1
        return_me = len(card_stack)

    return return_me
