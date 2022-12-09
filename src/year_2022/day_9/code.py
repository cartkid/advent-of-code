import os
import math


class rope:
    def __init__(
        self,
        snake_length: int = 2,
    ):
        self.snake_length = snake_length
        start: tuple[int, int] = (0, 0)
        self.tail_coordinates: list[tuple[int, int]] = [start]
        self.snake_coordinates: dict[int, tuple[int, int]] = {}

        for i in range(0, self.snake_length):
            self.snake_coordinates[i] = start

    def move_step(self, direction_to_move: str):
        direction_to_move = direction_to_move.upper()
        self.__move_head_step(direction_to_move=direction_to_move)
        for i in range(1, self.snake_length):
            self.__move_next_piece_step(piece=i)

    def __move_head_step(self, direction_to_move: str):
        self.snake_coordinates[0] = rope.get_move_result_coordinates(
            curr_coordinates=self.snake_coordinates[0],
            direction_to_move=direction_to_move,
        )

    def __move_next_piece_step(self, piece: int):
        if self.is_piece_close_enough(piece=piece) is False:
            following = self.snake_coordinates[piece - 1]
            current = self.snake_coordinates[piece]

            temp_x = following[0] - current[0]
            new_coord_x = (
                temp_x if abs(temp_x) <= 1 else math.floor(temp_x / 2)
            ) + current[0]
            temp_y = following[1] - current[1]
            new_coord_y = (
                temp_y if abs(temp_y) <= 1 else math.floor(temp_y / 2)
            ) + current[1]

            self.snake_coordinates[piece] = (new_coord_x, new_coord_y)

            if (
                piece + 1 == self.snake_length
                and self.snake_coordinates[piece] not in self.tail_coordinates
            ):
                self.tail_coordinates.append(self.snake_coordinates[piece])

    @staticmethod
    def get_move_result_coordinates(
        curr_coordinates: tuple[int, int],
        direction_to_move: str,
    ) -> tuple[int, int]:
        return_me: tuple[int, int] = curr_coordinates
        if direction_to_move == "U":
            return_me = (curr_coordinates[0], curr_coordinates[1] + 1)
        elif direction_to_move == "D":
            return_me = (curr_coordinates[0], curr_coordinates[1] - 1)
        elif direction_to_move == "L":
            return_me = (curr_coordinates[0] - 1, curr_coordinates[1])
        elif direction_to_move == "R":
            return_me = (curr_coordinates[0] + 1, curr_coordinates[1])

        return return_me

    def is_piece_close_enough(self, piece: int) -> bool:
        if (
            abs(self.snake_coordinates[piece - 1][0] - self.snake_coordinates[piece][0])
            <= 1
            and abs(
                self.snake_coordinates[piece - 1][1] - self.snake_coordinates[piece][1]
            )
            <= 1
        ):
            return True
        return False


def some_function(file_name: str = "input.txt", part_two: bool = False) -> int:
    return_me: int = 0
    directory = os.path.dirname(os.path.realpath(__file__))
    file = open(os.path.join(directory, file_name), "r")
    all_lines = file.readlines()

    snake_length: int = 2 if part_two is False else 10
    curr_rope: rope = rope(snake_length=snake_length)

    for line in all_lines:
        values_only = line.strip("\n").split(" ")
        direction_to_move = values_only[0]
        number_to_move = int(values_only[1])

        for i in range(0, number_to_move):
            curr_rope.move_step(direction_to_move=direction_to_move)

    return_me = len(curr_rope.tail_coordinates)

    # to print the tail
    all_y = [x[1] for x in curr_rope.tail_coordinates]
    all_x = [x[0] for x in curr_rope.tail_coordinates]
    for y in range(max(all_y), min(all_y) - 1, -1):
        debug = ""
        for x in range(min(all_x), max(all_x) + 1):
            if (x, y) in curr_rope.tail_coordinates:
                debug += "#"
            else:
                debug += "."
        print(debug)

    return return_me
