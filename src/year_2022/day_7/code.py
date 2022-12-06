import os


def some_function(file_name: str = "input.txt", part_two: bool = False) -> int:
    return_me: int = 0
    directory = os.path.dirname(os.path.realpath(__file__))
    file = open(os.path.join(directory, file_name), "r")
    all_lines = file.readlines()

    for i, line in enumerate(all_lines):
        values_only = line.strip("\n")
        after_count: int = 4 if part_two is False else 14
        for j, char in enumerate(values_only):
            if len(values_only) < j + after_count:
                return -1
            lst: list[str] = []
            found_it: bool = False
            for k in range(after_count):
                if values_only[j + k] in lst:
                    break
                lst.append(values_only[j + k])
                if k == after_count - 1:
                    found_it = True
                    return_me = j + after_count
            if found_it is True:
                break

    return return_me
