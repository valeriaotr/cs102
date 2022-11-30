import pathlib
import typing as tp

T = tp.TypeVar("T")


def read_sudoku(path: tp.Union[str, pathlib.Path]) -> tp.List[tp.List[str]]:
    """Прочитать Судоку из указанного файла"""
    path = pathlib.Path(path)
    with path.open() as f:
        puzzle = f.read()
    return create_grid(puzzle)


def create_grid(puzzle: str) -> tp.List[tp.List[str]]:
    digits = [c for c in puzzle if c in "123456789."]
    grid = group(digits, 9)
    return grid


def display(grid: tp.List[tp.List[str]]) -> None:
    """Вывод Судоку"""
    width = 2
    line = "+".join(["-" * (width * 3)] * 3)
    for row in range(9):
        print("".join(grid[row][col].center(width) + ("|" if str(col) in "25" else "") for col in range(9)))
        if str(row) in "25":
            print(line)
    print()


def group(values: tp.List[T], n: int) -> tp.List[tp.List[T]]:
    """
    Сгруппировать значения values в список, состоящий из списков по n элементов
    >>> group([1,2,3,4], 2)
    [[1, 2], [3, 4]]
    >>> group([1,2,3,4,5,6,7,8,9], 3)
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    """
    a = []
    b = []
    r = 0
    for i in range(0, len(values)):
        r += 1
        b.append(values[i])
        if r == n:
            a.append(b)
            b = []
            r = 0
    return a


def get_row(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения для номера строки, указанной в pos
    >>> get_row([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '2', '.']
    >>> get_row([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (1, 0))
    ['4', '.', '6']
    >>> get_row([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (2, 0))
    ['.', '8', '9']
    """
    return grid[pos[0]]


def get_col(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения для номера столбца, указанного в pos
    >>> get_col([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '4', '7']
    >>> get_col([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (0, 1))
    ['2', '.', '8']
    >>> get_col([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (0, 2))
    ['3', '6', '9']
    """
    a = []
    for i in grid:
        for j in range(0, len(grid)):
            if j == pos[1]:
                a.append(i[j])
    return a


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
    a = int(pos[0]) // 3 * 3
    b = int(pos[1]) // 3 * 3
    c = []
    for i in range(a, a + 3):
        for j in range(b, b + 3):
            c.append(grid[i][j])
    return c


def find_empty_positions(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.Tuple[int, int]]:
    """Найти первую свободную позицию в пазле
    >>> find_empty_positions([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']])
    (0, 2)
    >>> find_empty_positions([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']])
    (1, 1)
    >>> find_empty_positions([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']])
    (2, 0)
    """
    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            if grid[i][j] == ".":
                return (i, j)
    return "no"


def find_possible_values(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.Set[str]:
    """Вернуть множество возможных значения для указанной позиции
    >>> grid = read_sudoku('puzzle1.txt')
    >>> values = find_possible_values(grid, (0,2))
    >>> values == {'1', '2', '4'}
    True
    >>> values = find_possible_values(grid, (4,7))
    >>> values == {'2', '5', '9'}
    True
    """
    q = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}
    block = get_block(grid, pos)
    for i in range(0, len(block)):
        for j in range(0, len(block[1])):
            if block[i][j] in q:
                q.remove(block[i][j])
    row = get_row(grid, pos)
    for i in range(0, len(row)):
        if row[i] in q:
            q.remove(row[i])
    column = get_col(grid, pos)
    for i in range(0, len(column)):
        if column[i] in q:
            q.remove(column[i])
    return q


def var(grid: tp.List[tp.List[str]]):
    f.clear()
    for i in range(0, len(grid)):
        t = []
        for j in range(0, len(grid[0])):
            t.append(grid[i][j])
        f.append(t)


def solver(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]):
    global f
    position = find_empty_positions(grid)
    if position == "no":
        var(grid)
        return
    values = find_possible_values(grid, (int(position[0]), int(position[1])))
    if find_empty_positions(grid) == "no":
        return

    if len(values) == 0:
        grid[int(pos[0])][int(pos[1])] = "."
        return
    for value in values:
        grid[int(position[0])][int(position[1])] = str(value)
        solver(grid, (position[0], position[1]))
        grid[int(position[0])][int(position[1])] = "."


def solve(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.List[tp.List[str]]]:
    """Решение пазла, заданного в grid"""
    """ Как решать Судоку?
        1. Найти свободную позицию
        2. Найти все возможные значения, которые могут находиться на этой позиции
        3. Для каждого возможного значения:
            3.1. Поместить это значение на эту позицию
            3.2. Продолжить решать оставшуюся часть пазла
    >>> grid = read_sudoku('puzzle1.txt')
    >>> solve(grid)
    [['5', '3', '4', '6', '7', '8', '9', '1', '2'], ['6', '7', '2', '1', '9', '5', '3', '4', '8'], ['1', '9', '8', '3', '4', '2', '5', '6', '7'], ['8', '5', '9', '7', '6', '1', '4', '2', '3'], ['4', '2', '6', '8', '5', '3', '7', '9', '1'], ['7', '1', '3', '9', '2', '4', '8', '5', '6'], ['9', '6', '1', '5', '3', '7', '2', '8', '4'], ['2', '8', '7', '4', '1', '9', '6', '3', '5'], ['3', '4', '5', '2', '8', '6', '1', '7', '9']]
    """
    solver(grid, (find_empty_positions(grid)[0], find_empty_positions(grid)[1]))
    a = f
    return a


def check_solution(solution: tp.List[tp.List[str]]) -> bool:
    """Если решение solution верно, то вернуть True, в противном случае False"""
    r: tp.List[str] = []
    q = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for i in range(0, len(solution)):
        for j in range(0, len(q)):
            if solution[i].count(q[j]) > 1:
                return False
    for i in range(0, len(solution)):
        r.clear()
        for j in range(0, len(q)):
            r.append(solution[j][i])
        for t in range(0, len(q)):
            if r.count(q[i]) > 1:
                return False
    for i in range(0, len(solution)):
        for j in range(0, len(solution[0])):
            if solution[i][j] == ".":
                return False
    # block = get_block(grid,)

    return True


def generate_sudoku(N: int) -> tp.List[tp.List[str]]:
    """Генерация судоку заполненного на N элементов
    >>> grid = generate_sudoku(40)
    >>> sum(1 for row in grid for e in row if e == '.')
    41
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    >>> grid = generate_sudoku(1000)
    >>> sum(1 for row in grid for e in row if e == '.')
    0
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    >>> grid = generate_sudoku(0)
    >>> sum(1 for row in grid for e in row if e == '.')
    81
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    """
    r: tp.List[str] = []
    q = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for i in range(0, len(solution)):
        for j in range(0, len(q)):
            if solution[i].count(q[j]) > 1:
                return False
    for i in range(0, len(solution)):
        r.clear()
        for j in range(0, len(q)):
            r.append(solution[j][i])
        for t in range(0, len(q)):
            if r.count(q[i]) > 1:
                return False
    for i in range(0, len(solution)):
        for j in range(0, len(solution[0])):
            if solution[i][j] == ".":
                return False
    # block = get_block(grid,)

    return True


if __name__ == "__main__":
    for fname in ["puzzle1.txt", "puzzle2.txt", "puzzle3.txt"]:
        grid = read_sudoku(fname)
        display(grid)
        solution = solve(grid)
        if not solution:
            print(f"Puzzle {fname} can't be solved")
        else:
            display(solution)
