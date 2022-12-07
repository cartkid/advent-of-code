from dataclasses import dataclass, field
from typing import Union
import os


@dataclass
class AoCFile:
    name: str = ""
    size: int = 0
    parent_directory: Union[str, None] = None

    def get_full_path(self):
        if self.parent_directory is None:
            return self.name
        else:
            return f"{self.parent_directory}\\{self.name}"


@dataclass
class AoCDirectory:
    name: str = ""
    sub_directories: list[str] = field(default_factory=list)
    sub_files: list[AoCFile] = field(default_factory=list)
    parent_directory: Union[str, None] = None

    def get_immediate_file_size_total(self):
        total: int = 0
        for f in self.sub_files:
            total += f.size
        return total

    def get_total_nested_file_size_total(self, all_directories: dict[str, object]):
        total: int = 0
        total += self.get_immediate_file_size_total()
        for d_name in self.sub_directories:
            if d_name in all_directories:
                d = all_directories[d_name]
                total += d.get_total_nested_file_size_total(all_directories)  # type: ignore

        return total

    def get_directory_path(self):
        if self.parent_directory is None:
            return self.name
        else:
            return f"{self.parent_directory}\\{self.name}"


def some_function(file_name: str = "input.txt", part_two: bool = False) -> int:
    return_me: int = 0
    directory = os.path.dirname(os.path.realpath(__file__))
    file = open(os.path.join(directory, file_name), "r")
    all_lines = file.readlines()

    d_found: list[str] = []

    all_directories: dict[str, AoCDirectory] = {}
    curr_directory: Union[AoCDirectory, None] = None

    for i, line in enumerate(all_lines):
        values_only = line.strip("\n")
        if values_only.startswith("$ cd /"):
            # change directory to root
            curr_directory = AoCDirectory(name="/")
        elif values_only.startswith("$ cd .."):
            # go up a level
            if curr_directory is not None:
                all_directories[curr_directory.get_directory_path()] = curr_directory
                new_directory_name = curr_directory.parent_directory
                if new_directory_name is not None:
                    curr_directory = all_directories[new_directory_name]
        elif values_only.startswith("$ cd "):
            # go into a folder
            name = values_only.replace("$ cd ", "")
            full_name = (
                name
                if curr_directory is None
                else f"{curr_directory.get_directory_path()}\\{name}"
            )
            if full_name in d_found:
                d_found.remove(full_name)
            if curr_directory is not None:
                curr_directory.sub_directories.append(full_name)
                all_directories[curr_directory.get_directory_path()] = curr_directory
                curr_directory = AoCDirectory(
                    name=name, parent_directory=curr_directory.get_directory_path()
                )
        elif values_only.startswith("$ ls"):
            pass
        elif values_only.startswith("dir "):
            # a directory it has to go into
            name = values_only.replace("dir ", "")
            full_name = (
                name
                if curr_directory is None
                else f"{curr_directory.get_directory_path()}\\{name}"
            )
            d_found.append(full_name)
        else:
            # a file
            parts = values_only.split(" ")
            f_size: int = int(parts[0])
            f_name: str = parts[1]
            f = AoCFile(name=f_name, size=f_size)
            if curr_directory is not None:
                curr_directory.sub_files.append(f)
    all_directories[curr_directory.get_directory_path()] = curr_directory  # type:ignore

    total_disc_space: int = 70000000
    needed_disc_space: int = 30000000
    root = all_directories["/"]
    root_space: int = root.get_total_nested_file_size_total(all_directories=all_directories)  # type: ignore
    unused_space = total_disc_space - root_space
    free_space_needed = needed_disc_space - unused_space
    possibilities: list[int] = []
    max_size_to_count: int = 100000
    total: int = 0
    for aoc_directory_path in all_directories:
        aoc_directory = all_directories[aoc_directory_path]
        d_size = aoc_directory.get_total_nested_file_size_total(all_directories=all_directories)  # type: ignore
        if part_two is False and d_size < max_size_to_count:
            total += d_size
        elif part_two is True and d_size >= free_space_needed:
            possibilities.append(d_size)
    if part_two is False:
        return_me = total
    else:
        return_me = sorted(possibilities)[0]
    return return_me
