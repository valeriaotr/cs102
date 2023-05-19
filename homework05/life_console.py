import curses

from life import GameOfLife
from ui import UI


class Console(UI):
    def __init__(self, life: GameOfLife) -> None:
        super().__init__(life)

    def draw_borders(self, screen) -> None:
        """Отобразить рамку."""
        screen.border("|", "|", "-", "-", "+", "+", "+", "+")

    def draw_grid(self, screen) -> None:
        """Отобразить состояние клеток."""
        for i, row in enumerate(self.life.current_generation):
            for j, cell in enumerate(row):
                if cell:
                    screen.addstr(j + 1, i + 1, "*")
                else:
                    screen.addstr(j + 1, i + 1, " ")

    def run(self) -> None:
        screen = curses.initscr()
        curses.resizeterm(self.life.cell_height + 2, self.life.cell_width + 2)
        while True:
            if not self.life.is_changing or self.life.is_max_generations_exceeded:
                break
            self.life.step()
            self.draw_borders(screen)
            self.draw_grid(screen)
            screen.refresh()
            curses.napms(400)
        curses.endwin()


if __name__ == "__main__":
    game = GameOfLife(size=(20, 20), randomize=True, max_generations=100)
    console = Console(life=game)
    console.run()
    exit(0)
