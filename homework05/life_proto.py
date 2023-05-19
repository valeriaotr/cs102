import random
import typing as tp

import pygame  # type: ignore
from pygame import QUIT
from pygame.locals import *  # type: ignore

Cell = tp.Tuple[int, int]
Cells = tp.List[int]
Grid = tp.List[Cells]


class GameOfLife:
    grid: Grid

    def __init__(self, width: int = 640, height: int = 480, cell_size: int = 10, speed: int = 10) -> None:
        self.width = width
        self.height = height
        self.cell_size = cell_size

        # Устанавливаем размер окна
        self.screen_size = width, height
        # Создание нового окна
        self.screen = pygame.display.set_mode(self.screen_size)

        # Вычисляем количество ячеек по вертикали и горизонтали
        self.cell_width = self.width // self.cell_size
        self.cell_height = self.height // self.cell_size

        # Скорость протекания игры
        self.speed = speed

    def draw_lines(self) -> None:
        """Отрисовать сетку"""
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (0, y), (self.width, y))

    def run(self) -> None:
        """Запустить игру"""
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption("Game of Life")
        self.screen.fill(pygame.Color("white"))

        # Создание списка клеток
        self.grid = self.create_grid(randomize=True)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False

            # Отрисовка списка клеток
            # Выполнение одного шага игры (обновление состояния ячеек)

            self.draw_grid()
            self.draw_lines()

            self.grid = self.get_next_generation()

            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()

    def create_grid(self, randomize: bool = False) -> Grid:
        """
        Создание списка клеток.

        Клетка считается живой, если ее значение равно 1, в противном случае клетка
        считается мертвой, то есть, ее значение равно 0.

        Parameters
        ----------
        randomize : bool
            Если значение истина, то создается матрица, где каждая клетка может
            быть равновероятно живой или мертвой, иначе все клетки создаются мертвыми.

        Returns
        ----------
        out : Grid
            Матрица клеток размером `cell_height` х `cell_width`.
        """
        grid = []
        for _ in range(self.cell_height):
            row = []
            for _ in range(self.cell_width):
                if randomize:
                    row.append(random.randint(0, 1))
                else:
                    row.append(0)
            grid.append(row)
        return grid

    def draw_grid(self) -> None:
        """
        Отрисовка списка клеток с закрашиванием их в соответствующе цвета.
        """
        grid = self.grid
        for n, row in enumerate(grid):
            for m, cell in enumerate(row):
                color = "green" if cell else "white"
                pygame.draw.rect(
                    surface=self.screen,
                    color=color,
                    rect=(m * self.cell_size, n * self.cell_size, self.cell_size, self.cell_size),
                )

    def get_neighbours(self, cell: Cell) -> Cells:
        """
        Вернуть список соседних клеток для клетки `cell`.

        Соседними считаются клетки по горизонтали, вертикали и диагоналям,
        то есть, во всех направлениях.

        Parameters
        ----------
        cell : Cell
            Клетка, для которой необходимо получить список соседей. Клетка
            представлена кортежем, содержащим ее координаты на игровом поле.

        Returns
        ----------
        out : Cells
            Список соседних клеток.
        """
        grid = self.grid
        x, y = cell
        neighs = []
        up = x - 1 >= 0
        down = x + 1 < self.cell_height
        right = y + 1 < self.cell_width
        left = y - 1 >= 0
        if down:
            neighs.append(grid[x + 1][y])
            if left:
                neighs.append(grid[x + 1][y - 1])
            if right:
                neighs.append(grid[x + 1][y + 1])
        if up:
            neighs.append(grid[x - 1][y])
            if left:
                neighs.append(grid[x - 1][y - 1])
            if right:
                neighs.append(grid[x - 1][y + 1])
        if right:
            neighs.append(grid[x][y + 1])
        if left:
            neighs.append(grid[x][y - 1])
        return neighs

    def get_next_generation(self) -> Grid:
        """
        Получить следующее поколение клеток.

        Returns
        ----------
        out : Grid
            Новое поколение клеток.
        """
        grid = self.grid
        new_grid = []
        for x, row in enumerate(grid):
            new_row = []
            for y, cell in enumerate(row):
                neighs = self.get_neighbours((x, y))
                alive = neighs.count(1)
                if cell and 2 <= alive <= 3 or not cell and alive == 3:
                    new_row.append(1)
                else:
                    new_row.append(0)
            new_grid.append(new_row)
        return new_grid


if __name__ == "__main__":
    game = GameOfLife(320, 240, 20)
    game.run()


