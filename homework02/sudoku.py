import pathlib
import random
import typing as tp


def read_sudoku(path: tp.Union[str, pathlib.Path]) -> tp.List[tp.List[str]]:
    path = pathlib.Path(path)
    with path.open() as f:
        puzzle = f.read()
    return create_grid(puzzle)


f: tp.List[tp.List[str]] = []
sudoku_for_gen = [
    ["5", "3", "4", "6", "7", "8", "9", "1", "2"],
    ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
    ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
    ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
    ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
    ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
    ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
    ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
    ["3", "4", "5", "2", "8", "6", "1", "7", "9"],
]


def create_grid(puzzle: str) -> tp.List[tp.List[str]]:
    digits = [c for c in puzzle if c in "123456789."]
    grid = group(digits, 9)
    return grid


def display(grid: tp.List[tp.List[str]]) -> None:
    width = 2
    line = "+".join(["-" * (width * 3)] * 3)
    for row in range(9):
        print("".join(grid[row][col].center(width) + ("|" if str(col) in "25" else "") for col in range(9)))
        if str(row) in "25":
            print(line)
    print()


def group(values, n: int):
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

    return grid[pos[0]]


def get_col(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    a = []
    for i in grid:
        for j in range(0, len(grid)):
            if j == pos[1]:
                a.append(i[j])
    return a


def get_block(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    a = int(pos[0]) // 3 * 3
    b = int(pos[1]) // 3 * 3
    c = []
    for i in range(a, a + 3):
        for j in range(b, b + 3):
            c.append(grid[i][j])
    return c


def find_empty_positions(grid: tp.List[tp.List[str]]):
    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            if grid[i][j] == ".":
                return (i, j)
    return "no"


def find_possible_values(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.Set[str]:
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
    solver(grid, (find_empty_positions(grid)[0], find_empty_positions(grid)[1]))
    a = f
    return a


def check_solution(solution: tp.List[tp.List[str]]) -> bool:
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


# b b a b b c a c a
def generate_sudoku(N: int):
    s = []
    r: tp.List[str] = []
    for i in range(9):
        r.clear()
        for j in range(9):
            r.append(".")
        s.append(r)

    if N == 0:
        return s
    sol = solve(s)
    if N >= 81:
        return sol
    sol = sudoku_for_gen
    N = 81 - N
    for i in range(9):
        for j in range(9):
            if N > 0:
                a = 0
                b = 0
                while sol[a][b] == ".":
                    a = random.randint(0, 8)
                    b = random.randint(0, 8)
                sol[a][b] = "."
                N -= 1
    return sol


if __name__ == "__main__":
    grid = generate_sudoku(40)