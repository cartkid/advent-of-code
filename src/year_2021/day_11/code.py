import os


class Grid:
    def __init__(self, grid: list[list[int]]):
        self.grid = grid
        self.flashed_coords: list[tuple[int, int]] = []
        self.flashes: int = 0

    def step(self):
        # increase
        self.__increase()

        # flash
        self.flashed_coords = []
        self.__flash_check_all()

        # reset flashed
        self.__reset_flashed()

    def check_for_all_flashed(self) -> bool:
        curr_sum: int = 0
        for r in self.grid:
            curr_sum += sum(r)
        return curr_sum == 0

    def __increase(self, amount_to_increase: int = 1):
        for i, r in enumerate(self.grid):
            for j, c in enumerate(self.grid[i]):
                self.grid[i][j] += amount_to_increase

    def __flash_check_all(self):
        can_continue = True
        for i, _ in enumerate(self.grid):
            for j, _ in enumerate(self.grid[i]):
                if self.grid[i][j] > 9 and (i, j) not in self.flashed_coords:
                    self.__flash(row=i, col=j)
                    can_continue = False
                if can_continue is False:
                    break
            if can_continue is False:
                break
        if can_continue is False:
            self.__flash_check_all()

    def __flash(self, row: int, col: int, amount_to_increase: int = 1):
        self.flashes += 1
        self.flashed_coords.append((row, col))
        for r in range(row - 1, row + 2):
            if r < 0 or r >= len(self.grid):
                continue
            for c in range(col - 1, col + 2):
                if c < 0 or c >= len(self.grid[r]):
                    continue
                self.grid[r][c] += amount_to_increase

    def __reset_flashed(self):
        for i, r in enumerate(self.grid):
            for j, c in enumerate(self.grid[i]):
                if self.grid[i][j] > 9:
                    self.grid[i][j] = 0


def some_function(file_name: str = "input.txt", part_two: bool = False) -> int:
    return_me: int = 0
    directory = os.path.dirname(os.path.realpath(__file__))
    file = open(os.path.join(directory, file_name), "r")
    all_lines = file.readlines()

    grid: list[list[int]] = []

    for i, line in enumerate(all_lines):
        values_only = line.strip("\n")
        grid.append([])
        for val in values_only:
            grid[i].append(int(val))

    my_grid = Grid(grid)
    if part_two is False:
        for i in range(0, 100):
            my_grid.step()
        return_me = my_grid.flashes
    else:
        step_num: int = 0
        while my_grid.check_for_all_flashed() is False:
            step_num += 1
            my_grid.step()
        return_me = step_num

    return return_me
