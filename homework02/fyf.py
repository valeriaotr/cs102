import pathlib
import random
import typing as tp

T = tp.TypeVar("T")
def create_grid(puzzle: str) -> tp.List[tp.List[str]]:
    """
    Создание cетки из строки
    """
    digits = [c for c in puzzle if c in "123456789."]
    grid = group(digits, 9)
    return grid

def group(values: tp.List[T], number: int) -> tp.List[tp.List[T]]:
    """
    Сгруппировать значения values в список, состоящий из списков по n элементов
    >>> group([1,2,3,4], 2)
    [[1, 2], [3, 4]]
    >>> group([1,2,3,4,5,6,7,8,9], 3)
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    """
    return [values[i : i + number] for i in range(0, len(values), number)]

def read_sudoku(path: tp.Union[str, pathlib.Path]) -> tp.List[tp.List[str]]:
    """
    Прочитать Судоку из указанного файла
    """
    path = pathlib.Path(path)
    with path.open(encoding="utf-8") as file:
        puzzle = file.read()
    return create_grid(puzzle)

def get_block(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения из квадрата, в который попадает позиция pos
    >>> grid = read_sudoku('puzzle1.txt')
    >>> get_block(grid, (0, 1))
    ['5', '3', '.', '6', '.', '.', '.', '9', '8']
    >>> get_block(grid, (4, 7))
    ['.', '.', '3', '.', '.', '1', '.', '.', '6']
    >>> get_block(grid, (8, 8))
    ['2', '8', '.', '.', '.', '5', '.', '7', '9']
    """
    start_pos = (pos[0] // 3 * 3, pos[1] // 3 * 3)
    ans = []
    for i in enumerate(grid):
        if i[0] < start_pos[0] + 3 and i[0] >= start_pos[0]:
            for j in enumerate(grid[i[0]]):
                if j[0] < start_pos[1] + 3 and j[0] >= start_pos[1]:
                    ans.append(j[1])
    return ans

grid = read_sudoku('puzzle1.txt')
get_block(grid, (0, 1))