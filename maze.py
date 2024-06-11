from graphics import(Window, Line, Point)
from cell import(Cell)
import time
import random

class Maze():
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win = None,
        seed = None,
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

        self._cells = []

        if seed != None:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()

    def _create_cells(self):
        for col in range(self._num_cols):
            newcol = []
            for row in range(self._num_rows):
                newcol.append(Cell(self._win))
            self._cells.append(newcol)

        for i in range(self._num_cols):
            for j in range (self._num_rows):
                self._draw_cell(i,j)


    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + self._cell_size_x * i
        y1 = self._y1 + self._cell_size_y * j
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1,y1,x2,y2)
        self._animate_fast()

    def _animate_fast(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.005)

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.03)

    def _break_entrance_and_exit(self):
        if len(self._cells) == 0:
            return
        entry_cell = self._cells[0][0]
        exit_cell = self._cells[len(self._cells) - 1][len(self._cells[0]) - 1]
        entry_cell.has_top_wall = False
        self._draw_cell(0,0)
        exit_cell.has_bot_wall = False
        self._draw_cell(len(self._cells) - 1, len(self._cells[0]) - 1)

    def _break_walls_r(self, i, j):
        cell = self._cells
        cur_cell = cell[i][j]
        cur_cell._visited = True
        while(True):
            to_visit = []
            if i - 1 >= 0:
                if not cell[i-1][j]._visited:
                    to_visit.append((i-1,j))
            if j - 1 >= 0:
                if not cell[i][j-1]._visited:
                    to_visit.append((i,j-1))
            if i + 1<= self._num_cols - 1:
                if not cell[i+1][j]._visited:
                    to_visit.append((i+1,j))
            if j + 1<= self._num_rows - 1:
                if not cell[i][j+1]._visited:
                    to_visit.append((i,j+1))
            if len(to_visit) == 0:
                if self._win is not None:
                    cur_cell.draw(cur_cell._x1, cur_cell._y1, cur_cell._x2, cur_cell._y2)
                return
            else:
                ind = random.randrange(0, len(to_visit))
                i2 = to_visit[ind][0]
                j2 = to_visit[ind][1]
                side_cell = cell[i2][j2]
                if j > j2:
                    cur_cell.has_top_wall = False
                    side_cell.has_bot_wall = False
                if j < j2:
                    cur_cell.has_bot_wall = False
                    side_cell.has_top_wall = False
                if i > i2:
                    cur_cell.has_left_wall = False
                    side_cell.has_right_wall = False
                if i < i2:
                    cur_cell.has_right_wall = False
                    side_cell.has_left_wall = False
                self._break_walls_r(i2,j2)

    def _reset_cells_visited(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j]._visited = False




    def solve(self):
        return self._solve_r(0,0)


    def _solve_r(self, i, j):
        cells = self._cells
        curr_cell = self._cells[i][j]
        self._animate()
        curr_cell._visited = True
        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True
        if i - 1 >= 0 and not cells[i-1][j]._visited:
            if not curr_cell.has_left_wall:
                curr_cell.draw_move(cells[i-1][j])
                if self._solve_r(i-1,j):
                    return True
                else:
                    curr_cell.draw_move(cells[i-1][j], True)
        if j - 1 >= 0 and not cells[i][j-1]._visited:
            if not curr_cell.has_top_wall:
                curr_cell.draw_move(cells[i][j-1])
                if self._solve_r(i,j-1):
                    return True
                else:
                    curr_cell.draw_move(cells[i][j-1], True)
        if i + 1 <= self._num_cols - 1 and not cells[i+1][j]._visited:
            if not curr_cell.has_right_wall:
                curr_cell.draw_move(cells[i+1][j])
                if self._solve_r(i+1,j):
                    return True
                else:
                    curr_cell.draw_move(cells[i+1][j], True)
        if j + 1 <= self._num_rows - 1 and not cells[i][j+1]._visited:
            if not curr_cell.has_bot_wall:
                curr_cell.draw_move(cells[i][j+1])
                if self._solve_r(i,j+1):
                    return True
                else:
                    curr_cell.draw_move(cells[i][j+1], True)
        return False

