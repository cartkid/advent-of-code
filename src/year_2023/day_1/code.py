import os


def get_num_from_line(line: str, first: bool = True, part_two: bool = False) -> int:
    return_me: int = 0

    num_map: dict[str, int] = {}
    num_map["one"] = 1
    num_map["two"] = 2
    num_map["three"] = 3
    num_map["four"] = 4
    num_map["five"] = 5
    num_map["six"] = 6
    num_map["seven"] = 7
    num_map["eight"] = 8
    num_map["nine"] = 9

    possible_int_position: int = -1
    possible_int: int = 0
    for idx in range(0, len(line)) if first else range(len(line) - 1, -1, -1):
        try:
            char: str = line[idx]
            possible_int = int(char)
            possible_int_position = int(idx)
            break
        except ValueError:
            continue

    if part_two is False:
        return possible_int

    possible_word_position: int = -1
    possible_word: int = 0
    for item in num_map.keys():
        temp_possible_word_position = line.find(item) if first else line.rfind(item)
        if temp_possible_word_position > -1:
            if possible_word_position == -1 or (
                (first and temp_possible_word_position < possible_word_position)
                or (
                    first is False
                    and temp_possible_word_position > possible_word_position
                )
            ):
                possible_word_position = temp_possible_word_position
                possible_word = num_map[item]

    if possible_int_position >= 0 and possible_word_position == -1:
        return possible_int
    elif possible_word_position >= 0 and possible_int_position == -1:
        return possible_word
    else:
        if first:
            return (
                possible_int
                if possible_int_position < possible_word_position
                else possible_word
            )
        else:
            return (
                possible_int
                if possible_int_position > possible_word_position
                else possible_word
            )


def some_function(file_name: str = "input.txt", part_two: bool = False) -> int:
    return_me: int = 0
    directory = os.path.dirname(os.path.realpath(__file__))
    file = open(os.path.join(directory, file_name), "r")
    all_lines = file.readlines()

    numbers: list[int] = []

    for line in all_lines:
        if line == "" or line == "\n":
            continue
        first = get_num_from_line(line, True, part_two)
        last = get_num_from_line(line, False, part_two)

        val = int(str(first) + str(last))
        print(val)
        numbers.append(val)
        return_me += val

    return return_me
