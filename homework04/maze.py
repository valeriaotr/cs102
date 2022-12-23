from copy import deepcopy
from random import choice, randint
from typing import Any, List, Optional, Tuple, Union

#import pandas as pd  # type: ignore


def create_grid(rows: int = 15, cols: int = 15) -> List[List[Union[str, int]]]:
    return [["■"] * cols for _ in range(rows)]


def remove_wall(grid: List[List[Union[str, int]]], coord: Tuple[int, int]) -> List[List[Union[str, int]]]:
    """

    :param grid:
    :param coord:
    :return:
    """

    x, y = coord
    direction = choice([0, 1])
    if direction == 0:
        if x == 1 and y != len(grid) - 2:
            grid[x][y + 1] = " "
        elif x == 1 and y == len(grid) - 2:  # noqa: W503
            pass
        else:
            grid[x - 1][y] = " "
    else:
        if y == len(grid) - 2 and x != 1:
            grid[x - 1][y] = " "
        elif y == len(grid) - 2:
            pass
        else:
            grid[x][y + 1] = " "

    return grid


def bin_tree_maze(rows: int = 15, cols: int = 15, random_exit: bool = True) -> List[List[Union[str, int]]]:
    """

    :param rows:
    :param cols:
    :param random_exit:
    :return:
    """

    grid = create_grid(rows, cols)
    empty_cells = []
    for x, row in enumerate(grid):
        for y, _ in enumerate(row):
            if x % 2 == 1 and y % 2 == 1:
                grid[x][y] = " "
                empty_cells.append((x, y))

    for elem in empty_cells:
        remove_wall(grid, elem)

    # 1. выбрать любую клетку
    # 2. выбрать направление: наверх или направо.
    # Если в выбранном направлении следующая клетка лежит за границами поля,
    # выбрать второе возможное направление
    # 3. перейти в следующую клетку, сносим между клетками стену
    # 4. повторять 2-3 до тех пор, пока не будут пройдены все клетки

    # генерация входа и выхода
    if random_exit:
        x_in, x_out = randint(0, rows - 1), randint(0, rows - 1)
        y_in = randint(0, cols - 1) if x_in in (0, rows - 1) else choice((0, cols - 1))
        y_out = randint(0, cols - 1) if x_out in (0, rows - 1) else choice((0, cols - 1))
    else:
        x_in, y_in = 0, cols - 2
        x_out, y_out = rows - 1, 1

    grid[x_in][y_in], grid[x_out][y_out] = "X", "X"

    return grid


def get_exits(grid: List[List[Union[str, int]]]) -> List[Tuple[int, int]]:
    """

    :param grid:
    :return:
    """
    exits: Any = []

    for x, row in enumerate(grid):
        for y, elem in enumerate(row):
            if elem == "X":
                exits.append((x, y))

    return exits


def make_step(grid: List[List[Union[str, int]]], k: int) -> List[List[Union[str, int]]]:
    """

    :param grid:
    :param k:
    :return:
    """
    for x, row in enumerate(grid):
        for y, elem in enumerate(row):
            if elem == k:
                if x != 0 and grid[x - 1][y] == " ":
                    grid[x - 1][y] = k + 1
                elif x != 0 and grid[x - 1][y] == 0:
                    grid[x - 1][y] = k + 1
                if y != 0 and grid[x][y - 1] == " ":
                    grid[x][y - 1] = k + 1
                elif y != 0 and grid[x][y - 1] == 0:
                    grid[x][y - 1] = k + 1
                if x != len(grid) - 1 and grid[x + 1][y] == " ":
                    grid[x + 1][y] = k + 1
                elif x != len(grid) - 1 and grid[x + 1][y] == 0:
                    grid[x + 1][y] = k + 1
                if y != len(grid) - 1 and grid[x][y + 1] == " ":
                    grid[x][y + 1] = k + 1
                elif y != len(grid) - 1 and grid[x][y + 1] == 0:
                    grid[x][y + 1] = k + 1
    return grid


def shortest_path(grid, exit_coord):
    """

    :param grid:
    :param exit_coord:
    :return:
    """
    x, y = exit_coord
    k = grid[x][y]
    path = [(x, y)]
    while k != 1:
        if x != 0 and grid[x - 1][y] == k - 1:
            x -= 1
            k -= 1
            path.append((x, y))
        elif y != 0 and grid[x][y - 1] == k - 1:
            y -= 1
            k -= 1
            path.append((x, y))
        elif x != len(grid) - 1 and grid[x + 1][y] == k - 1:
            x += 1
            k -= 1
            path.append((x, y))
        elif y != len(grid) - 1 and grid[x][y + 1] == k - 1:
            y += 1
            k -= 1
            path.append((x, y))
    return path


def encircled_exit(grid: List[List[Union[str, int]]], coord: Tuple[int, int]) -> bool:
    """
    :param grid:
    :param coord:
    :return:
    """
    x, y = coord
    if x == 0 and grid[x + 1][y] != " ":
        return True
    if x == len(grid) - 1 and grid[x - 1][y] != " ":
        return True
    if y == 0 and grid[x][y + 1] != " ":
        return True
    if y == len(grid) - 1 and grid[x][y - 1] != " ":
        return True

    return False


def solve_maze(
    grid: List[List[Union[str, int]]],
) -> Tuple[List[List[Union[str, int]]], Optional[Union[Tuple[int, int], List[Tuple[int, int]]]]]:
    """

    :param grid:
    :return:
    """
    exits = get_exits(grid)
    x_1, y_1 = exits[0]
    x_2, y_2 = exits[1]
    k = 0

    if len(exits) != 2:
        return grid, None

    if encircled_exit(grid, (x_1, y_1)) or encircled_exit(grid, (x_2, y_2)):
        return grid, None

    grid[x_1][y_1], grid[x_2][y_2] = 1, 0

    grid = deepcopy(grid)
    for r, row in enumerate(grid):
        for c, elem in enumerate(row):
            if elem == " ":
                grid[r][c] = 0

    while grid[x_2][y_2] == 0:
        k += 1
        make_step(grid, k)

    return grid, shortest_path(grid, (x_2, y_2))


def add_path_to_grid(
    grid: List[List[Union[str, int]]], path: Optional[Union[Tuple[int, int], List[Tuple[int, int]]]]
) -> List[List[Union[str, int]]]:
    """

    :param grid:
    :param path:
    :return:
    """
    #print(pd.DataFrame(grid))
    if path:
        for i, row in enumerate(grid):
            for j, _ in enumerate(row):
                if (i, j) in path:
                    grid[i][j] = "X"

    return grid


if __name__ == "__main__":
    GRID = bin_tree_maze(15, 15)
    EMPTY_GRID = deepcopy(GRID)
    _, PATH = solve_maze(GRID)
    MAZE = add_path_to_grid(EMPTY_GRID, PATH)
    # print(pd.DataFrame(MAZE))
