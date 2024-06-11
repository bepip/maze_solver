from graphics import (Line, Point, Window)

class Cell():
    def __init__(self, win = None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bot_wall = True
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = win
        self._visited = False

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        if self.has_left_wall:
            self._win.draw_line(Line(Point(x1,y1),Point(x1,y2)))
        else:
            self._win.draw_line(Line(Point(x1,y1),Point(x1,y2)), "white")
        if self.has_right_wall:
            self._win.draw_line(Line(Point(x2,y1),Point(x2,y2)))
        else:
            self._win.draw_line(Line(Point(x2,y1),Point(x2,y2)), "white")
        if self.has_top_wall:
            self._win.draw_line(Line(Point(x1,y1),Point(x2,y1)))
        else:
            self._win.draw_line(Line(Point(x1,y1),Point(x2,y1)), "white")
        if self.has_bot_wall:
            self._win.draw_line(Line(Point(x1,y2),Point(x2,y2)))
        else:
            self._win.draw_line(Line(Point(x1,y2),Point(x2,y2)), "white")

    #def draw_line(self, line, fill_color = "black"):
    def draw_move(self, to_cell, undo=False):
        center_cell_x = (self._x1 + self._x2) / 2
        center_cell_y = (self._y1 + self._y2) / 2
        center_to_cell_x = (to_cell._x1 + to_cell._x2) / 2
        center_to_cell_y = (to_cell._y1 + to_cell._y2) / 2
        center = Point(center_cell_x, center_cell_y)
        center_to_cell = Point(center_to_cell_x, center_to_cell_y)
        line = Line(center, center_to_cell)
        color = "red"
        if undo:
            color = "gray"
        self._win.draw_line(line, color)
