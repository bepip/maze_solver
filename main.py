from window import (
    Window, 
    Line,
    Point
)

def main():
    height = 600
    width = 800
    win = Window(width, height)
    line = Line(Point(0,0), Point(width, height))
    win.draw_line(line)
    win.wait_for_close()

main()
